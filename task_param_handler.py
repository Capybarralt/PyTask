import json
import pickle
import os
from abc import ABCMeta, abstractmethod

class ParamHandler(metaclass=ABCMeta):
    def __init__(self, source):
        self.source = source
        self.params = {}

    def add_param(self, key, value):
        self.params[key] = value

    def get_param(self, key):
        return self.params.get(key)

    def get_all_params(self):
        return self.params

    def remove_param(self, key):
        del self.params[key]

    def remove_all_params(self):
        self.params = {}

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass

class ParamHandlerException(Exception):
    pass

class ParamHandlerFactory(object):
    types = {}

    @classmethod
    def add_type(cls, name, klass):
        if not name:
            raise ParamHandlerException('Type must have a name.')

        if not issubclass(klass, ParamHandler):
            raise ParamHandlerException(
                'Class "{}" is not ParamHandler.'.format(klass)
            )
        cls.types[name] = klass

    @classmethod
    def create(cls, source):
        _, ext = os.path.splitext(str(source).lower())
        ext = ext.lstrip('.')
        klass = cls.types.get(ext)
        if klass is None:
            raise ParamHandlerException(
                'Type "{}" not found.'.format(ext)
            )
        return klass(source)


class JsonParamHandler(ParamHandler):
    def read(self):
        """Чтение из json файла и присвоение значений в self.params"""
        with open(self.source, "r") as read_file:
            read_params = json.load(read_file)
            self.params.update(read_params)

    def write(self):
        """Запись в json файл параметров self.params"""
        with open(self.source, "w") as write_file:
            json.dump(self.params, write_file)


class PickleParamHandler(ParamHandler):
    def read(self):
        """Чтение в формате pickle и присвоение значений в self.params"""
        with open(self.source, "rb") as read_file:
            read_params = pickle.load(read_file)
            self.params.update(read_params)

    def write(self):
        """Запись в формате pickle параметров self.params"""
        with open(self.source, "wb") as write_file:
            pickle.dump(self.params, write_file)


ParamHandlerFactory.add_type('json', JsonParamHandler)
ParamHandlerFactory.add_type('pickle', PickleParamHandler)
