from checkers.state import *
from checkers.vec import Vec
from checkers.global_constants import DIRECTIONS
from checkers.exceptions import *
from checkers.checkers_interface import CheckersInterface

class Board(CheckersInterface):
    """BOARD SIZE MUST BE EVEN"""
    board_size = 8
    pawns_for_site = 12

    white_pawns = []
    black_pawns = []
    enemies = None

    def __init__(self, state: State = None):
        self.enemies = None
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
        return ((y, x) for x in range(self.board_size) for y in board_side if (y%2==0 and x%2==0) or (y%2==1 and x%2==1))

    def get_state(self):
        return State(self.white_pawns, self.black_pawns)

    def resolve_moves(self, side: PawnColor)->list:
        moves = []
        self.enemies = self.get_pawns(side.opposite())
        for pawn in self.get_pawns(side):
            if pawn.type == 'NORMAL':
                moves += self.resolve_for_pawn(pawn)
            else:
                moves += self.resolve_for_queen(pawn)

    def resolve_for_pawn(self, pawn: Pawn, enemies: list):
        return self.get_jump_moves(pawn) or self.get_normal_pawn_moves(pawn)


    #todo do zrobienia
    def get_jump_moves(self, pawn: Pawn, enemies: list, carrier: dict = {}, move_list: list = [])->list:
        pass

    #todo nie działa
    def generate_jump_directions(self, pawn: Pawn)->iter:
        return (d for d in DIRECTIONS for x in self.enemy_position_generator() if [d[0] + pawn.position[0], d[1] + pawn.position[1]] == x )

    def enemy_position_generator(self):
        if getattr(self, 'enemies', None):
            return (e.position for e in self.enemies)
        else:
            raise InvalidUsageException('self.enemies should be specified to use this func')

    # todo do zrobienia
    def get_normal_pawn_moves(self, pawn: Pawn)->list:
        return []

    #todo do zrobienia
    def resolve_for_queen(self, pawn: Pawn):
        return []

    def get_pawns(self, side: PawnColor):
        return self.white_pawns if side.name == 'WHITE' else self.black_pawns
