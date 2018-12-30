from abc import ABCMeta, abstractmethod


class CheckersServiceInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def response(self):raise NotImplementedError

