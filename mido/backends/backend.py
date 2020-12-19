import os
import importlib
from .. import ports

DEFAULT_BACKEND = 'mido.backends.rtmidi'


class Backend(object):
    def __init__(self, name=None, api=None, load=False, use_environ=True):
        self.name = name or (os.environ.get('MIDO_BACKEND', DEFAULT_BACKEND) if hasattr(os,'environ') else DEFAULT_BACKEND)
        self.api = api
        self.use_environ = hasattr(os,'environ') and use_environ
        self._module = None

        # Split out api (if present).
        if api:
            self.api = api
        elif self.name and '/' in self.name:
            self.name, self.api = self.name.split('/', 1)
        else:
            self.api = None

        if load:
            self.load()

    @property
    def module(self):
        self.load()
        return self._module

    @property
    def loaded(self):
        """Return True if the module is loaded."""
        return self._module is not None

    def load(self):
        if not self.loaded:
            self._module = importlib.import_module(self.name)

    def _env(self, name):
        if self.use_environ:
            return os.environ.get(name)
        else:
            return None

    def _add_api(self, kwargs):
        if self.api and 'api' not in kwargs:
            kwargs['api'] = self.api
        return kwargs

    def open_input(self, name=None, virtual=False, callback=None, **kwargs):
      pass

    def open_output(self, name=None, virtual=False, autoreset=False, **kwargs):
      pass
  
    def open_ioport(self, name=None, virtual=False,
                    callback=None, autoreset=False, **kwargs):
      pass

    def _get_devices(self, **kwargs):
        if hasattr(self.module, 'get_devices'):
            return self.module.get_devices(**self._add_api(kwargs))
        else:
            return []

    def get_input_names(self, **kwargs):
      pass

    def get_output_names(self, **kwargs):
      pass

    def get_ioport_names(self, **kwargs):
      pass

    def __repr__(self):
        if self.loaded:
            status = 'loaded'
        else:
            status = 'not loaded'

        if self.api:
            name = '{}/{}'.format(self.name, self.api)
        else:
            name = self.name

        return '<backend {} ({})>'.format(name, status)
