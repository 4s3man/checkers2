from abc import ABCMeta, abstractmethod


class ResponseInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def to_json(self):raise NotImplementedError

