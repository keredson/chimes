# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
from .backends.backend import Backend
#from . import ports, sockets
from .messages import (Message, parse_string, parse_string_stream,
                       format_as_string, MIN_PITCHWHEEL, MAX_PITCHWHEEL,
                       MIN_SONGPOS, MAX_SONGPOS)
from .parser import Parser, parse, parse_all
from .midifiles import (MidiFile, MidiTrack, merge_tracks,
                        MetaMessage, UnknownMetaMessage,
                        bpm2tempo, tempo2bpm, tick2second, second2tick,
                        KeySignatureError)
#from .syx import read_syx_file, write_syx_file
#from .version import version_info
#from .__about__ import (__version__, __author__, __author_email__,
#                        __url__, __license__)

# Prevent splat import.
__all__ = []


def set_backend(name=None, load=False):
    glob = globals()

    if isinstance(name, Backend):
        backend = name
    else:
        backend = Backend(name, load=load, use_environ=True)
    glob['backend'] = backend

    for name in dir(backend):
        if name.split('_')[0] in ['open', 'get']:
            glob[name] = getattr(backend, name)


set_backend()

del os, absolute_import
