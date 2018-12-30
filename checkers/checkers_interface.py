from abc import ABCMeta, abstractmethod
from checkers.state import State
from checkers.move import Move


class CheckersInterface():
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_state(self):raise NotImplementedError

    @abstractmethod
    def resolve_moves(self)->list:raise NotImplementedError

    @abstractmethod
    def make_move(self, move:Move)->State:raise NotImplementedError
