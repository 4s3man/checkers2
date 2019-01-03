from checkers.abstract_game_object import GameObj
from itertools import count


class Move(GameObj):
    id = 0
    pawn_id = 0;
    position_after_move = []
    beated_pawns_ids = []

    def __init__(self, id:int, pawn_id:int, visited_fields:list, beated_pawn_ids:list=[]):
        self.id = id
        self.pawn_id = pawn_id
        self.visited_fields = visited_fields
        self.beated_pawn_ids = beated_pawn_ids
