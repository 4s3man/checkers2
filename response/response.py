from checkers.state import State
from checkers.move import Move
from response.response_interface import ResponseInterface


class Response(ResponseInterface):
    state = None
    moves = []

    def __init__(self, state: State, moves: list):
        self.state = state
        self.moves = moves

