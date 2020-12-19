"""
MIDI over TCP/IP.
"""
import socket
import select
from .parser import Parser
from .ports import MultiPort, BaseIOPort
from .py2 import PY2


def _is_readable(socket):
  pass

class PortServer(MultiPort):
  pass


class SocketPort(BaseIOPort):
    pass


def connect(host, portno):
    pass


def parse_address(address):
    pass


def format_address(host, portno):
    pass
