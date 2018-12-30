from checkers.pawn import *
from checkers.move import *
from checkers.state import *
from checkers.checkers_interface import CheckersInterface

class Board(CheckersInterface):
    """BOARD SIZE MUST BE EVEN"""
    board_size = 8
    pawns_for_site = 12

    white_pawns = []
    black_pawns = []

    def __init__(self, state: State = None):
        if state is None:
            self.initial_state()
        else:
            self.white_pawns = state.white_pawns
            self.black_pawns = state.black_pawns

    def initial_state(self):
        gen_black_places = self.make_places_gen(PawnColor('BLACK'))
        gen_white_places = self.make_places_gen(PawnColor('WHITE'))

        for pawn_id in range(self.pawns_for_site):
            self.white_pawns.append(
                Pawn(pawn_id, next(gen_white_places), PawnColor('WHITE'), PawnType('NORMAL'))
            )
            self.black_pawns.append(
                Pawn(pawn_id, next(gen_black_places), PawnColor('BLACK'), PawnType('NORMAL'))
            )

    def make_places_gen(self, color:PawnColor)->iter:
        board_side = range(self.board_size//2 - 1) if color.name == 'BLACK' else range(self.board_size-1, self.board_size // 2, -1)
        return ((y,x) for x in range(self.board_size) for y in board_side if (y%2==0 and x%2==0) or (y%2==1 and x%2==1))

    def get_state(self):
        return State(self.white_pawns, self.black_pawns)

    def resolve_moves(self, side: PawnColor)->list:
        # directions = ((1,1),(1,-1),(-1,-1),(-1,1))
        pawns = self.get_pawns(side)


    def get_pawns(self, side: PawnColor):
        return self.white_pawns if side.name == 'WHITE' else self.black_pawns
