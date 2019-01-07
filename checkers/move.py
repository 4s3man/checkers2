from checkers.abstract_game_object import GameObj
from checkers.json_serializable_interface import JsonSerializableInterface
import json

class Move(GameObj, JsonSerializableInterface):
    id = 0
    pawn_id = 0;
    position_after_move = ()
    beated_pawns = []

    def __init__(self, pawn_id: int, position_after_move: tuple, beated_pawns: list = [], id: int = 0):
        self.pawn_id = pawn_id
        self.position_after_move = position_after_move
        self.beated_pawns = beated_pawns
        self.id = id

    def set_id(self, id: int):
        self.id = id

    def to_json(self):
        return json.dumps(self, default=(lambda x: x.__dict__))

    @classmethod
    def from_json(cls, json_string: str):
        move_dict = json.loads(json_string)
        return cls(move_dict['pawn_id'], tuple(move_dict['position_after_move']), move_dict['beated_pawns'], move_dict['id'])
