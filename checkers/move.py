from checkers.abstract_game_object import GameObj
from itertools import count


class Move(GameObj):
    id = 0
    pawn_id = 0;
    after_move = ()
    beated_pawns = []

    def __init__(self, pawn_id: int, after_move: tuple, beated_pawns: list):
        self.pawn_id = pawn_id
        self.after_move = after_move
        self.beated_pawns = beated_pawns


