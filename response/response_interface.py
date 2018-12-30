from abc import ABCMeta, abstractmethod


class ResponseInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def toJson(self):raise NotImplementedError

