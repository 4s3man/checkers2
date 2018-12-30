from abc import ABCMeta, abstractmethod


class CheckersServiceInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def init_game(self):raise NotImplementedError

    @abstractmethod
    def handle_move(self):raise NotImplementedError

