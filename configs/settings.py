import configparser
import json
import os
from pathlib import Path


class DefaultOption(dict):
    def __init__(self, config, section, **kv):
        self._config = config
        self._section = section
        dict.__init__(self, **kv)

    def items(self):
        _items = []
        for option in self:
            if not self._config.has_option(self._section, option):
                _items.append((option, self[option]))
            else:
                value_in_config = self._config.get(self._section, option)
                _items.append((option, value_in_config))
        return _items


config = configparser.ConfigParser()


root = Path(__file__).parent.parent
config.read_file(open(str(root / 'config.ini')))

print(config.get('DATABASE', 'host'))
