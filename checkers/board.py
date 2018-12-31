from checkers.state import *
from checkers.global_constants import DIRECTIONS
from checkers.exceptions import *
from checkers.move import Move
from checkers.vec import Vec
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

    #todo nie działa prawdopodobnie robi nowy generator i zwraca ten sam ruch zamiast następnego
    def get_jump_moves(self, pawn: Pawn, carrier: dict = {'beated_pawn_ids':[], 'visited_fields':[], 'id':0}, move_list: list = [])->list:
        pass
        # for jump in self.make_jumps_generator(pawn, carrier['beated_pawn_ids']):
        #     carrier['visited_fields'].append(jump[0])
        #     carrier['beated_pawn_ids'].append(jump[1])
        #
        #
        #     virtual_pawn = deepcopy(pawn)
        #     virtual_pawn.position = jump[0]
        #
        #     self.get_jump_moves(gen, virtual_pawn, carrier, move_list)
        # else:
        #     carrier['id'] += 1
        #     carrier['pawn_id'] = pawn.id
        #     move_list.append(Move(**carrier))
        #     carrier = {'beated_pawn_ids':[], 'visited_fields':[], 'id':carrier['id']}
        #     return move_list


    #todo zmienić na moves generator, i żeby robił uzupełniał ruch już tu?
    def make_jumps_generator(self, pawn: Pawn, beated_pawn_ids: list=[])->iter:
        """Returns tuple of position after jump and beated pawn id if can jump in direction"""
        for d in DIRECTIONS:
            for enemy in self.get_pawns(self.enemy_side):
                next_field = self.next_field_in_direction(pawn.position, d)
                if next_field == enemy.position:
                    field_after_jump = self.next_field_in_direction(next_field, d)
                    if self.can_jump_over_enemy(pawn, enemy, field_after_jump, beated_pawn_ids):
                        yield (self.next_field_in_direction(next_field, d), enemy.id)


    def next_field_in_direction(self, position: tuple, direction: tuple)->tuple:
        """Returns field nexto to position in direction"""
        return (Vec(direction) + Vec(position)).vec


    def can_jump_over_enemy(self,pawn:Pawn, enemy: Pawn, destination: tuple, beated_pawn_ids: list)->bool:
        """Return false if distination out of board """
        if not self.has_position(destination): return False

        """Return false if place is busy"""
        if destination in [pawn.position for pawn in self.get_all_pawns_but_one(pawn)]: return False

        """Return false if enemy was already beated"""
        if enemy.id in beated_pawn_ids: return False

        return True


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