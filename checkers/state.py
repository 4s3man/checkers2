from checkers.pawn import *
from checkers.json_serializable_interface import JsonSerializableInterface
import json

class State(GameObj, JsonSerializableInterface):
    white_pawns = []
    black_pawns = []

    def __init__(self, white_pawns:list, black_pawns:list):
        self.white_pawns = white_pawns
        self.black_pawns = black_pawns

    def to_json(self):
        return json.dumps(self, default=(lambda x: x.__dict__))

    @classmethod
    def from_json(self, json_string: str):
        state_dict = json.loads(json_string)
        self.white_pawns = self.convert_pawn(State, PawnColor('WHITE'), state_dict['white_pawns'])
        self.black_pawns = self.convert_pawn(State, PawnColor('BLACK'), state_dict['white_pawns'])

        return self

    def convert_pawn(self, color: PawnColor, pawn_data: dict):
        convert_pawn = (lambda p, c=color: Pawn(p['id'], p['position'], color, PawnType(p['type'])))
        return list(map(
            convert_pawn,
            pawn_data
        ))

