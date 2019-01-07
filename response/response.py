from checkers.state import State
from checkers.move import Move
from response.response_interface import ResponseInterface
import json

class Response(ResponseInterface):
    state = None
    moves = []

    def __init__(self, state: State, moves: list):
        self.state = state
        self.moves = moves

    def to_json(self)->str:
        return json.dumps(self, default=(lambda x: x.__dict__))

    @staticmethod
    def concat_json_response_elements(state: str, moves:str):
        return json.dumps({'state': state, 'moves': moves})

