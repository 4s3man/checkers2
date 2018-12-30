from checkers.pawn import *


class State(GameObj):
    white_pawns = []
    black_pawns = []

    def __init__(self, white_pawns:list, black_pawns:list):
        self.white_pawns = white_pawns
        self.black_pawns = black_pawns
