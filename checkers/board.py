from checkers.state import *
from checkers.global_constants import DIRECTIONS
from checkers.exceptions import *
from checkers.move import Move
from checkers.jump import Jump
from checkers.checkers_interface import CheckersInterface
from copy import deepcopy

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
        self.enemies = side.opposite()
        for pawn in self.get_pawns(side):
            if pawn.type == 'NORMAL':
                moves += self.resolve_for_pawn(pawn)
            else:
                moves += self.resolve_for_queen(pawn)

    def resolve_for_pawn(self, pawn: Pawn, enemies: list):
        return self.get_jump_moves(pawn) or self.get_normal_pawn_moves(pawn)

    #todo zmienić nazwę zrobić testy czy zwraca zawsze maxymalne ruchy?
    def generate_move_data(self, pawn, moves, beated=[], last_position=(), id=1):

        has_nex_move = False
        jumps = self.get_beating_jumps(pawn, beated)
        for jump in jumps:
            has_nex_move = True
            beated.append(jump[1])


            v1 = deepcopy(pawn)
            v1.position = jump[0]

            self.generate_move_data(v1, moves, beated, pawn.position)

        if not has_nex_move:
                moves.append(Move(pawn.id, pawn.position, beated))
        return moves

    #todo zmienić nazwę zrobić testy
    def get_beating_jumps(self, pawn: Pawn, beated_pawn_ids: list=[])->iter:
        """Returns tuple of position after jump and beated pawn id if can jump in direction"""
        jumps = []
        for d in DIRECTIONS:
            for enemy in self.get_pawns(self.enemy_side):
                next_field = self.next_field_in_direction(pawn.position, d)
                if next_field == enemy.position:
                    field_after_jump = self.next_field_in_direction(next_field, d)
                    if self.can_jump_over_enemy(pawn, enemy, field_after_jump, beated_pawn_ids):
                        jumps.append((
                                self.next_field_in_direction(next_field, d),
                                enemy.id
                        ))
        return jumps

    def next_field_in_direction(self, position: tuple, direction: tuple)->tuple:
        """Returns field nexto to position in direction"""
        return tuple( x+y for y,x in zip(position, direction))


    def can_jump_over_enemy(self,pawn:Pawn, enemy: Pawn, destination: tuple, beated_pawn_ids: list)->bool:
        """Return false if distination out of board """
        if not self.has_position(destination): return False

        """Return false if place is busy"""
        if destination in (pawn.position for pawn in self.get_all_pawns_but_one(pawn)): return False

        """Return false if enemy was already beated"""
        if enemy.id in beated_pawn_ids: return False

        return True

    #todo tu tez powinien być generator
    def get_all_pawns_but_one(self, pawn: Pawn):
        """zwraca listę wszystkich pionków oprócz podanego"""
        return list(filter(lambda p: pawn.id != p.id, self.white_pawns + self.black_pawns))


    def has_position(self, position: tuple)->bool:
        """sprawdza czy board posiada daną pozycję"""
        for d in position:
            if d < 0 or d > self.board_size-1: return False
        return True

    # todo do zrobienia
    def get_normal_pawn_moves(self, pawn: Pawn)->list:
        return []

    #todo do zrobienia
    def resolve_for_queen(self, pawn: Pawn):
        return []

    def get_pawns(self, side: PawnColor):
        return self.white_pawns if side.name == 'WHITE' else self.black_pawns