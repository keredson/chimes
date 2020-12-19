

from __future__ import print_function, division
import gc
import io
import time
import string
import struct
from numbers import Integral

from ..messages import Message, SPEC_BY_STATUS
from .meta import (MetaMessage, build_meta_message, meta_charset,
                   encode_variable_int)

from .tracks import MidiTrack, merge_tracks, fix_end_of_track
from .units import tick2second

# The default tempo is 120 BPM.
# (500000 microseconds per beat (quarter note).)
DEFAULT_TEMPO = 500000
DEFAULT_TICKS_PER_BEAT = 480

# Maximum message length to attempt to read.
MAX_MESSAGE_LENGTH = 1000000


def print_byte(byte, pos=0):
    char = chr(byte)
    if char.isspace() or char not in string.printable:
        char = '.'

    print('  {:06x}: {:02x}  {}'.format(pos, byte, char))


class DebugFileWrapper(object):
    def __init__(self, file):
        self.file = file

    def read(self, size):
        data = self.file.read(size)

        for byte in data:
            # Iterating gives us byte strings instead of ints in
            # Python 2.
            if isinstance(byte, str):
                byte = ord(byte)

            print_byte(byte, self.file.tell())

        return data

    def tell(self):
        return self.file.tell()


def read_byte(self):
    byte = self.read(1)
    if byte == b'':
        raise EOFError
    else:
        return ord(byte)


def read_bytes(infile, size):
    if size > MAX_MESSAGE_LENGTH:
        raise IOError('Message length {} exceeds maximum length {}'.format(
            size, MAX_MESSAGE_LENGTH))
    return [read_byte(infile) for _ in range(size)]


def _dbg(text=''):
    print(text)


# We can't use the chunk module for two reasons:
#
# 1. we may have mixed big and little endian chunk sizes. (RIFF is
# little endian while MTrk is big endian.)
#
# 2. the chunk module assumes that chunks are padded to the nearest
# multiple of 2. This is not true of MIDI files.

def read_chunk_header(infile):
    header = infile.read(8)
    if len(header) < 8:
        raise EOFError

    # TODO: check for b'RIFF' and switch endian?

    return struct.unpack('>4sL', header)


def read_file_header(infile):
    name, size = read_chunk_header(infile)

    if name != b'MThd':
        raise IOError('MThd not found. Probably not a MIDI file')
    else:
        data = infile.read(size)

        if len(data) < 6:
            raise EOFError

        return struct.unpack('>hhh', data[:6])


def read_message(infile, status_byte, peek_data, delta, clip=False):
    try:
        spec = SPEC_BY_STATUS[status_byte]
    except LookupError:
        raise IOError('undefined status byte 0x{:02x}'.format(status_byte))

    # Subtract 1 for status byte.
    size = spec['length'] - 1 - len(peek_data)
    data_bytes = peek_data + read_bytes(infile, size)

    if clip:
        data_bytes = [byte if byte < 127 else 127 for byte in data_bytes]
    else:
        for byte in data_bytes:
            if byte > 127:
                raise IOError('data byte must be in range 0..127')

    return Message.from_bytes([status_byte] + data_bytes, time=delta)


def read_sysex(infile, delta):
    length = read_variable_int(infile)
    data = read_bytes(infile, length)

    # Strip start and end bytes.
    # TODO: is this necessary?
    if data and data[0] == 0xf0:
        data = data[1:]
    if data and data[-1] == 0xf7:
        data = data[:-1]

    return Message('sysex', data=data, time=delta)


def read_variable_int(infile):
    delta = 0

    while True:
        byte = read_byte(infile)
        delta = (delta << 7) | (byte & 0x7f)
        if byte < 0x80:
            return delta


def read_meta_message(infile, delta):
    meta_type = read_byte(infile)
    length = read_variable_int(infile)
    data = read_bytes(infile, length)
    return build_meta_message(meta_type, data, delta)


def read_track(infile, debug=False, clip=False):
    track = MidiTrack()

    name, size = read_chunk_header(infile)

    if name != b'MTrk':
        raise IOError('no MTrk header at start of track')

    if debug:
        _dbg('-> size={}'.format(size))
        _dbg()

    start = infile.tell()
    last_status = None

#    count = 0
    while True:
#        count += 1
#        if count > 20: break
        # End of track reached.
        if infile.tell() - start == size:
            break

        if debug:
            _dbg('Message:')

        delta = read_variable_int(infile)

        if debug:
            _dbg('-> delta={}'.format(delta))

        status_byte = read_byte(infile)

        if status_byte < 0x80:
            if last_status is None:
                raise IOError('running status without last_status')
            peek_data = [status_byte]
            status_byte = last_status
        else:
            if status_byte != 0xff:
                # Meta messages don't set running status.
                last_status = status_byte
            peek_data = []

        if status_byte == 0xff:
            msg = read_meta_message(infile, delta)
        elif status_byte in [0xf0, 0xf7]:
            # TODO: I'm not quite clear on the difference between
            # f0 and f7 events.
            msg = read_sysex(infile, delta)
        else:
            msg = read_message(infile, status_byte, peek_data, delta, clip)

#        print('gc.mem_free()', gc.mem_free(), msg, msg.type)
#        if msg.type in ('note_on','note_off'):
        gc.collect()
        track.append(msg)

        if debug:
            _dbg('-> {!r}'.format(msg))
            _dbg()

    return track




def get_seconds_per_tick(tempo, ticks_per_beat):
    # Tempo is given in microseconds per beat (default 500000).
    # At this tempo there are (500000 / 1000000) == 0.5 seconds
    # per beat. At the default resolution of 480 ticks per beat
    # this is:
    #
    #    (500000 / 1000000) / 480 == 0.5 / 480 == 0.0010417
    #
    return (tempo / 1000000.0) / ticks_per_beat


class MidiFile(object):
    def __init__(self, filename=None, file=None,
                 type=1, ticks_per_beat=DEFAULT_TICKS_PER_BEAT,
                 charset='latin1',
                 debug=False,
                 clip=False
                 ):

        self.filename = filename
        self.type = type
        self.ticks_per_beat = ticks_per_beat
        self.charset = charset
        self.debug = debug
        self.clip = clip

        self.tracks = []

        if type not in range(3):
            raise ValueError(
                'invalid format {} (must be 0, 1 or 2)'.format(format))

        if file is not None:
            self._load(file)
        elif self.filename is not None:
            with io.open(filename, 'rb') as file:
                self._load(file)

    def add_track(self, name=None):
        raise Exception('not implemented')

    def _load(self, infile):
        if self.debug:
            infile = DebugFileWrapper(infile)

        with meta_charset(self.charset):
            if self.debug:
                _dbg('Header:')

            (self.type,
             num_tracks,
             self.ticks_per_beat) = read_file_header(infile)

            if self.debug:
                _dbg('-> type={}, tracks={}, ticks_per_beat={}'.format(
                    self.type, num_tracks, self.ticks_per_beat))
                _dbg()

            for i in range(num_tracks):
                if self.debug:
                    _dbg('Track {}:'.format(i))

                self.tracks.append(read_track(infile,
                                              debug=self.debug,
                                              clip=self.clip))
                # TODO: used to ignore EOFError. I hope things still work.

    @property
    def length(self):
        if self.type == 2:
            raise ValueError('impossible to compute length'
                             ' for type 2 (asynchronous) file')

        return sum(msg.time for msg in self)

    def __iter__(self):
        # The tracks of type 2 files are not in sync, so they can
        # not be played back like this.
        if self.type == 2:
            raise TypeError("can't merge tracks in type 2 (asynchronous) file")

        tempo = DEFAULT_TEMPO
        # causes OOM
        # for msg in merge_tracks(self.tracks):
        for track in self.tracks:
          for msg in track:
            # Convert message time from absolute time
            # in ticks to relative time in seconds.
            if msg.time > 0:
                delta = tick2second(msg.time, self.ticks_per_beat, tempo)
            else:
                delta = 0

            yield msg.copy(time=delta)

            if msg.type == 'set_tempo':
                tempo = msg.tempo

    def play(self, meta_messages=False):
        sleep = time.sleep

        for msg in self:
            sleep(msg.time)

            if isinstance(msg, MetaMessage) and not meta_messages:
                continue
            else:
                yield msg

    def save(self, filename=None, file=None):
        pass

    def _save(self, outfile):
        pass

    def print_tracks(self, meta_only=False):
        for i, track in enumerate(self.tracks):
            print('=== Track {}'.format(i))
            for msg in track:
                if not isinstance(msg, MetaMessage) and meta_only:
                    pass
                else:
                    print('{!r}'.format(msg))

    def __repr__(self):
        return '<midi file {!r} type {}, {} tracks, {} messages>'.format(
            self.filename, self.type, len(self.tracks),
            sum([len(track) for track in self.tracks]))

    # The context manager has no purpose but is kept around since it was
    # used in examples in the past.
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        return False
