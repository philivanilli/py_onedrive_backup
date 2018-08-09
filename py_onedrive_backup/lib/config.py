# -*- coding: UTF-8 -*-

import json
import os
from . import logger


_config_object = None


class JSONConfig:
    def __init__(self, config_filename=None):
        self.is_dirty = False
        self.is_new = False
        self.is_file_protected = False
        self.data = dict()
        self.filename = config_filename
        if self.filename is not None:
            self.load()

    def get(self, key, default=None):
        if isinstance(key, str):
            key = list(filter(None, key.split('/')))
        if not isinstance(key, list):
            raise TypeError("string or string list expected for param key")

        parent = self.data
        for item in key:
            if item in parent:
                parent = parent[item]
            else:
                return default

        return parent

    def set(self, key, value):
        if isinstance(key, str):
            key = list(filter(None, key.split('/')))
        if not isinstance(key, list):
            raise TypeError("string or string list expected for param key")

        self.is_dirty = True

        parent = self.data
        for item in key[:-1]:
            if item not in parent:
                parent[item] = {}
            parent = parent[item]

        parent[key[-1]] = value

    def load(self, config_filename=None):
        if config_filename is not None:
            self.filename = config_filename

        self.is_dirty = False
        self.is_new = False
        self.is_file_protected = False

        if os.path.isfile(self.filename):
            logger.info("Loading configuration file %s" % self.filename)

            try:
                with open(self.filename) as infile:
                    self.data = json.load(infile)
            except Exception as e:
                self.is_file_protected = True
                logger.error(" %s" % str(e))
                logger.warning(" Loading configuration file failed. Saving will be disabled to keep file untouched.")
        else:
            self.is_new = True
            logger.warning("Configuration file '%s' does not exists" % self.filename)

    def save(self, config_filename=None):
        if config_filename is not None:
            self.filename = config_filename

        if not self.is_file_protected and self.is_dirty:
            logger.info("Saving configuration file %s" % self.filename)
            with open(self.filename, 'w') as outfile:
                json.dump(self.data, outfile)

            self.is_dirty = False
            self.is_new = False


def set_global_config(obj):
    global _config_object
    _config_object = obj


def get_global():
    global _config_object
    return _config_object