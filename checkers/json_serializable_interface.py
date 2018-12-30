from abc import ABCMeta, abstractmethod
import json

class JsonSerializableInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_json(self):raise NotImplementedError

    @abstractmethod
    def from_json(self)->list:raise NotImplementedError
