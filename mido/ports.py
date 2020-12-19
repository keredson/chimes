"""
Useful tools for working with ports
"""
from __future__ import unicode_literals
import threading
import time
import random
from .parser import Parser
from .messages import Message

# How many seconds to sleep before polling again.
_DEFAULT_SLEEP_TIME = 0.001
_sleep_time = _DEFAULT_SLEEP_TIME


# TODO: document this more.
def sleep():
    pass


def set_sleep_time(seconds=_DEFAULT_SLEEP_TIME):
    pass


def get_sleep_time():
    pass


def reset_messages():
    pass


def panic_messages():
    pass


class DummyLock(object):
    pass


class BasePort(object):
    pass


class BaseInput(BasePort):
    pass

class BaseOutput(BasePort):
    pass


class BaseIOPort(BaseInput, BaseOutput):
    pass


class IOPort(BaseIOPort):
    pass


class EchoPort(BaseIOPort):
    pass


class MultiPort(BaseIOPort):
    pass


def multi_receive(ports, yield_ports=False, block=True):
    pass


def multi_iter_pending(ports, yield_ports=False):
    pass


def multi_send(ports, msg):
    pass

