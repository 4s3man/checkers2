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
    enemy_side = None

    def __init__(self, state: State = None):
        self.enemy_side = None
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

    #todo przetestować
    def resolve_moves(self, side: PawnColor)->list:
        moves = []
        self.enemy_side = side.opposite()
        for pawn in self.get_pawns(side):
            if pawn.type == 'NORMAL':
                moves += self.resolve_for_pawn(pawn)
            else:
                moves += self.resolve_for_queen(pawn)

        return self.leave_only_most_beating_moves(moves)

    def resolve_for_pawn(self, pawn: Pawn):
        return self.leave_only_most_beating_moves(
            self.get_jump_moves(pawn, []) or self.get_normal_pawn_moves(pawn))

    def resolve_for_queen(self, pawn: Pawn):
        return self.leave_only_most_beating_moves(
            self.get_jump_moves_for_queen(pawn)) or self.get_normal_queen_moves(pawn)

    def get_jump_moves_for_queen(self, pawn: Pawn)->list:
        output = []
        for d in DIRECTIONS:
            position = pawn.position
            while self.has_position(position):
                if position != pawn.position:
                    enemy = self.get_enemy_by_position(position)
                    if enemy:
                        field_after_jump = self.next_field_in_direction(position, d)
                        vq = self.make_virtual_pawn_on_position(pawn, field_after_jump)
                        if self.can_jump_over_enemy(vq, enemy, field_after_jump):
                            output += self.get_jump_moves(vq, [], {'v':[vq.position],'b':[enemy.id]})
                        break

                position = self.next_field_in_direction(position, d)

        return output

    def get_normal_queen_moves(self, pawn: Pawn)->list:
        output = []
        for d in DIRECTIONS:
            position = pawn.position
            while self.has_position(position):
                if position != pawn.position:
                    if self.get_enemy_by_position(position):
                        break
                    else:
                        output.append(Move(pawn.id, position, []))

                position = self.next_field_in_direction(position, d)

        return output

    def get_normal_pawn_moves(self, pawn: Pawn)->list:
        """Get no jumping pawn moves"""
        foreward = -1 if pawn in self.white_pawns else 1
        output = []
        for d in [(foreward, 1), (foreward, -1)]:
            next_field = self.next_field_in_direction(pawn.position, d)
            if self.has_position(next_field) and next_field not in self.get_all_pawn_positions_but_one(pawn):
                output.append(
                    Move(pawn.id, next_field)
                )

        return output

    def get_jump_moves(self, pawn: Pawn, moves: list, car={})->list:
        """Gets list of Move objects as argument"""
        car = {'v':[],'b':[]} if not car else deepcopy(car)
        has_next = False
        for jump in self.generate_jumps(pawn, car['b']):
            has_next = True

            """If recurent came back strip last appended to carrier"""
            if len(car['v']) and pawn.position != car['v'][-1]:
                car['v'] = car['v'][:-1]
                car['b'] = car['b'][:-1]

            car['v'].append(jump[0])
            car['b'].append(jump[1])

            v1 = self.make_virtual_pawn_on_position(pawn, jump[0])

            self.get_jump_moves(v1, moves, car)

        if not has_next:
            """I dont want moves beating same pawns here"""
            if set(car['b']) != set(y for move in moves for y in move.beated_pawns):
                moves.append(Move(pawn.id, pawn.position, car['b']))
        return moves

    def make_virtual_pawn_on_position(self, pawn: Pawn, position: tuple)->Pawn:
        """Make pawn which is not in state and sets its position"""
        v1 = deepcopy(pawn)
        v1.position = position

        return v1

    def generate_jumps(self, pawn: Pawn, beated_pawn_ids: list=[])->iter:
        """Returns tuple of position after jump and beated pawn id if can jump in direction"""
        for d in DIRECTIONS:
            for enemy in self.get_pawns(self.enemy_side):
                next_field = self.next_field_in_direction(pawn.position, d)
                if next_field == enemy.position:
                    field_after_jump = self.next_field_in_direction(next_field, d)
                    if self.can_jump_over_enemy(pawn, enemy, field_after_jump, beated_pawn_ids):
                        yield (
                                self.next_field_in_direction(next_field, d),
                                enemy.id
                        )

    def next_field_in_direction(self, position: tuple, direction: tuple)->tuple:
        """Returns field nexto to position in direction"""
        return tuple( x+y for y,x in zip(position, direction))


    def can_jump_over_enemy(self,pawn:Pawn, enemy: Pawn, destination: tuple, beated_pawn_ids: list = [])->bool:
        """Return false if distination out of board """
        if not self.has_position(destination): return False

        """Return false if place is busy"""
        if destination in self.get_all_pawn_positions_but_one(pawn): return False

        """Return false if enemy was already beated"""
        if enemy.id in beated_pawn_ids: return False

        return True

    def get_all_pawn_positions_but_one(self, pawn: Pawn):
        return (x.position for x in self.white_pawns + self.black_pawns if pawn.id != x.id)

    def has_position(self, position:tuple)->bool:
        for d in position:
            if d < 0 or d > self.board_size-1: return False
        return True

    def get_pawns(self, side: PawnColor):
        return self.white_pawns if side.name == 'WHITE' else self.black_pawns

    def get_enemy_by_position(self, position: tuple)->Pawn or None:
        enemy = (x for x in self.get_pawns(self.enemy_side) if x.position == position)
        return next(enemy, None)

    def leave_only_most_beating_moves(self, moves: list)->list:
        """Returns list of moves which has longest beated_pawn_ids"""
        if len(moves):
            max_beated_pawns = self.get_max_beated_number(moves)
            return [move for move in moves if len(move.beated_pawns) == max_beated_pawns]
        else:
            return moves

    def get_max_beated_number(self, moves: list)->int:
        if len(moves):
            return len(max(moves, key=lambda x: len(x.beated_pawns)).beated_pawns)
        else:
            return 0
