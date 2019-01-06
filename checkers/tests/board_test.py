from checkers.board import *
from checkers.tests.fixtures.state_fixtures import *

def test_initial_state():
    board = Board()
    board.size = 8
    board.pawns_for_site = 12
    black_positions = set([(0,0), (0,2), (0,4), (0,6), (1, 1), (1, 3), (1, 5), (1,7), (2,0), (2,2), (2,4), (2,6)])
    board_black_pawns_position = set(map(lambda x: x.position, board.black_pawns))
    assert board_black_pawns_position == black_positions
    assert board_black_pawns_position != black_positions.add((0,1))

    white_positions = set([(6, 0), (6, 2), (6, 4), (6, 6), (5, 1), (5, 3), (5, 5), (5, 7), (7, 1), (7, 3), (7, 5), (7, 7)])
    board_white_pawns_position= set(map(lambda x: x.position, board.white_pawns))
    assert board_white_pawns_position == white_positions
    assert board_white_pawns_position != white_positions.add((0,1))

def test_get_pawns():
    b = Board()
    white_pawns = b.get_pawns(PawnColor('WHITE'))
    assert white_pawns == b.white_pawns

    black_pawns = b.get_pawns(PawnColor('BLACK'))
    assert black_pawns == b.black_pawns

    assert black_pawns != white_pawns

def test_get_all_pawns_position_but_one(different_pawns_around_white_state):
    b = Board()
    pawn0 = b.white_pawns[0]
    pawn1 = b.white_pawns[1]
    for position in b.get_all_pawn_positions_but_one(pawn0):
        assert pawn0.position != position

    for position in b.get_all_pawn_positions_but_one(pawn1):
        assert pawn1.position != position

def test_has_position():
    b = Board()
    false_pos = [ (x, y) for x in [-1, b.board_size] for y in [b.board_size, (-1)]]
    true_pos = (3,3)
    for pos in false_pos:
        assert False == b.has_position(pos)
    assert True == b.has_position(true_pos)

def test_can_jump_over_enemy(different_pawns_around_white_state):
    b = Board(different_pawns_around_white_state)
    pawn0 = b.white_pawns[0]
    pawn1 = b.white_pawns[1]
    assert True == b.can_jump_over_enemy(pawn0, b.black_pawns[0], (1,1), [])
    assert False == b.can_jump_over_enemy(pawn0, b.black_pawns[0], (1, 1), [3])

    assert False == b.can_jump_over_enemy(pawn0, b.black_pawns[0], (2, 2), [])
    assert True == b.can_jump_over_enemy(pawn0, b.black_pawns[0], (4, 4), [])

def test_next_field_in_direction():
    b = Board()
    assert (6,4) == b.next_field_in_direction((5,3), (1,1))


def test_generate_jumps(different_pawns_around_white_state, extended_circle_state):
    b = Board(different_pawns_around_white_state)
    b.enemy_side = PawnColor('BLACK')
    gen1 = b.generate_jumps(b.white_pawns[0], [])
    for t in gen1:
        assert t == ((1,1), 3)

    b.enemy_side = PawnColor('WHITE')
    gen2 = b.generate_jumps(b.black_pawns[1], [])
    for t in gen2:
        assert t == ()

    b1 = Board(extended_circle_state)
    b1.enemy_side = PawnColor('BLACK')
    gen3 = b1.generate_jumps(b1.white_pawns[0], [])
    for t in gen3:
        assert t in [((7, 5), 11), ((3,5), 7), ((3,1),6) ]

    gen4 = b1.generate_jumps(b1.white_pawns[0], [7])
    for t in gen4:
        assert t in [((7, 5), 11), ((3,1),6) ]

    gen5 = b1.generate_jumps(b1.white_pawns[3], [])
    for t in gen5:
        assert t == ((2,0), 10)

    b1 = Board(extended_circle_state)
    b1.enemy_side = PawnColor('BLACK')
    gen6 = b1.generate_jumps(b1.white_pawns[1], [])
    for t in gen6:
        assert t in [((3,3),8)]

def test_get_jump_moves(extended_circle_state, different_pawns_around_white_state, flower_state):
    board = Board(extended_circle_state)
    board.enemy_side = PawnColor('BLACK')
    moves = board.get_jump_moves(board.white_pawns[1], [])

    assert moves[0].position_after_move == (7,7)
    assert moves[0].beated_pawns== [8, 7, 9]

    assert moves[1].position_after_move == (7, 3)
    assert moves[1].beated_pawns == [8, 7, 11]

    assert moves[2].position_after_move == (5,1)
    assert moves[2].beated_pawns == [8, 6]

    assert moves[2].position_after_move != (7, 1)
    assert moves[2].beated_pawns != [6]

    assert len(moves) == 3

    moves = board.get_jump_moves(board.white_pawns[0], [])
    assert moves[0].position_after_move == (5, 7)
    assert moves[0].beated_pawns == [11, 9]

    assert moves[1].position_after_move == (5, 7)
    assert moves[1].beated_pawns == [7, 8, 5, 6, 11, 9]

    assert len(moves) == 2

    board = Board(different_pawns_around_white_state)
    board.enemy_side = PawnColor('BLACK')
    moves = board.get_jump_moves(board.white_pawns[0], [])
    assert moves[0].position_after_move == (1, 1)
    assert moves[0].beated_pawns == [3]

    assert len(moves) == 1

    board = Board(different_pawns_around_white_state)
    board.enemy_side = PawnColor('WHITE')
    moves = board.get_jump_moves(board.black_pawns[0], [])
    assert moves[0].position_after_move == (4, 4)
    assert moves[0].beated_pawns == [1]

    board = Board(flower_state)
    board.enemy_side = PawnColor('BLACK')
    moves = board.get_jump_moves(board.white_pawns[0], [])

    assert moves[0].position_after_move == (5, 5)
    assert moves[0].beated_pawns == [1]
    assert moves[1].position_after_move == (5, 1)
    assert moves[1].beated_pawns == [3]
    assert moves[2].position_after_move == (1, 5)
    assert moves[2].beated_pawns == [4]
    assert moves[3].position_after_move == (1, 1)
    assert moves[3].beated_pawns == [2]

def test_get_normal_pawn_moves(different_pawns_around_white_state, extended_circle_state):
    b = Board(different_pawns_around_white_state)

    for move in b.get_normal_pawn_moves(b.white_pawns[0]):
        assert False
    else:
        assert True

    moves = b.get_normal_pawn_moves(b.black_pawns[0])
    for move in moves:
        assert move.position_after_move == (3,1)
    assert len(moves) == 1

    moves = b.get_normal_pawn_moves(b.white_pawns[1])
    assert moves[0].position_after_move == (1, 5)
    assert moves[1].position_after_move == (1, 3)
    assert len(moves) == 2


def test_get_normal_pawn_moves__extended_circle(extended_circle_state):
    b1 = Board(extended_circle_state)
    moves = b1.get_normal_pawn_moves(b1.white_pawns[2])
    assert len(moves) == 1
    assert moves[0].position_after_move == (5, 1)

def test_get_jump_moves_for_queen___for_queen_blocking_pawns_state(for_queen_blocking_pawns_state):
    board = Board(for_queen_blocking_pawns_state)
    board.enemy_side = PawnColor('BLACK')
    moves = board.get_jump_moves_for_queen(board.white_pawns[0])
    assert moves[0].position_after_move == (5,7)
    assert moves[0].beated_pawns == [4,5]

    assert moves[1].position_after_move == (0, 2)
    assert moves[1].beated_pawns == [2, 6]


def test_get_jump_moves_for_queen___queen_extended_circle_state(queen_extended_circle_state):
    board = Board(queen_extended_circle_state)
    board.enemy_side = PawnColor('BLACK')
    moves = board.get_jump_moves_for_queen(board.white_pawns[0])

    assert moves[0].position_after_move == (5, 3)
    assert moves[0].beated_pawns == [7, 8, 5, 6]

    moves = board.get_jump_moves_for_queen(board.white_pawns[1])
    assert moves[0].position_after_move == (1, 3)
    assert moves[0].beated_pawns == [8, 7, 6, 5]

    moves = board.get_jump_moves_for_queen(board.white_pawns[2])
    assert moves[0].position_after_move == (1, 3)
    assert moves[0].beated_pawns == [5, 6, 7, 8]

def test_get_normal_queen_moves(for_queen_normal_moves_state):
    board = Board(for_queen_normal_moves_state)

    board.enemy_side = PawnColor('BLACK')
    moves = board.resolve_for_queen(board.white_pawns[0])

    assert moves[0].position_after_move == (5, 3)
    assert moves[0].beated_pawns == []

    assert moves[1].position_after_move == (6, 4)
    assert moves[1].beated_pawns == []

    assert moves[2].position_after_move == (7, 5)
    assert moves[2].beated_pawns == []

    assert moves[3].position_after_move == (5, 1)
    assert moves[3].beated_pawns == []

    assert moves[4].position_after_move == (6, 0)
    assert moves[4].beated_pawns == []

    assert moves[5].position_after_move == (3, 3)
    assert moves[5].beated_pawns == []

    assert moves[6].position_after_move == (2, 4)
    assert moves[6].beated_pawns == []

    assert moves[7].position_after_move == (1, 5)
    assert moves[7].beated_pawns == []

    assert moves[8].position_after_move == (0, 6)
    assert moves[8].beated_pawns == []

    assert moves[9].position_after_move == (3, 1)
    assert moves[9].beated_pawns == []

    assert moves[10].position_after_move == (2, 0)
    assert moves[10].beated_pawns == []

def test_get_max_beated_number(extended_circle_state):
    board = Board(extended_circle_state)

    board.enemy_side = PawnColor('BLACK')
    num = board.get_max_beated_number(board.get_jump_moves(board.white_pawns[1], []))
    assert num == 3

def test_leave_most_beating_moves_only(extended_circle_state):
    board = Board(extended_circle_state)

    board.enemy_side = PawnColor('BLACK')
    moves = board.leave_only_most_beating_moves(
        board.get_jump_moves(board.white_pawns[1], [])
    )

    assert moves[0].position_after_move == (7, 7)
    assert moves[0].beated_pawns == [8, 7, 9]
    assert moves[1].position_after_move == (7, 3)
    assert moves[1].beated_pawns == [8, 7, 11]

def test_resolve_for_pawn___extended_circle_state(extended_circle_state):
    board = Board(extended_circle_state)

    board.enemy_side = PawnColor('BLACK')
    moves = board.resolve_for_pawn(board.white_pawns[1])

    assert moves[0].position_after_move == (7, 7)
    assert moves[0].beated_pawns == [8, 7, 9]
    assert moves[1].position_after_move == (7, 3)
    assert moves[1].beated_pawns == [8, 7, 11]

    moves = board.resolve_for_pawn(board.white_pawns[0])
    assert moves[0].position_after_move == (5, 7)
    assert moves[0].beated_pawns == [7, 8, 5, 6, 11, 9]

def test_resolve_moves_for_pawn___different_pawns_around_white(different_pawns_around_white_state):
    board = Board(different_pawns_around_white_state)

    board.enemy_side = PawnColor('BLACK')
    moves = board.resolve_for_pawn(board.white_pawns[0])

    assert moves[0].position_after_move == (1, 1)
    assert moves[0].beated_pawns == [3]

    board.enemy_side = PawnColor('WHITE')
    moves = board.resolve_for_pawn(board.black_pawns[1])
    
    assert moves[0].position_after_move == (5, 3)
    assert moves[0].beated_pawns == []


def test_resolve_moves___initial_state():
    board = Board()
    moves = board.resolve_moves(PawnColor('WHITE'))
    assert moves[0].pawn_id == 2
    assert moves[0].position_after_move == (4, 2)
    assert moves[0].beated_pawns == []

    assert moves[1].pawn_id == 2
    assert moves[1].position_after_move == (4, 0)
    assert moves[1].beated_pawns == []

    assert moves[2].pawn_id == 5
    assert moves[2].position_after_move == (4, 4)
    assert moves[2].beated_pawns == []

    assert moves[3].pawn_id == 5
    assert moves[3].position_after_move == (4, 2)
    assert moves[3].beated_pawns == []

    assert moves[4].pawn_id == 8
    assert moves[4].position_after_move == (4, 6)
    assert moves[4].beated_pawns == []

    assert moves[5].pawn_id == 8
    assert moves[5].position_after_move == (4, 4)
    assert moves[5].beated_pawns == []

    assert moves[6].pawn_id == 11
    assert moves[6].position_after_move == (4, 6)
    assert moves[6].beated_pawns == []

    moves = board.resolve_moves(PawnColor('BLACK'))

    assert moves[0].pawn_id == 1
    assert moves[0].position_after_move == (3, 1)
    assert moves[0].beated_pawns == []

    assert moves[1].pawn_id == 4
    assert moves[1].position_after_move == (3, 3)
    assert moves[1].beated_pawns == []

    assert moves[2].pawn_id == 4
    assert moves[2].position_after_move == (3, 1)
    assert moves[2].beated_pawns == []

    assert moves[3].pawn_id == 7
    assert moves[3].position_after_move == (3, 5)
    assert moves[3].beated_pawns == []

    assert moves[4].pawn_id == 7
    assert moves[4].position_after_move == (3, 3)
    assert moves[4].beated_pawns == []

    assert moves[5].pawn_id == 10
    assert moves[5].position_after_move == (3, 7)
    assert moves[5].beated_pawns == []

    assert moves[6].pawn_id == 10
    assert moves[6].position_after_move == (3, 5)
    assert moves[6].beated_pawns == []

def resolve_moves___no_blocked_beating_move_bug(no_blocked_beating_move_bug):
    board = Board(no_blocked_beating_move_bug())
    moves = board.resolve_moves(PawnColor('WHITE'))
    assert moves[0].pawn_id == 1
    assert moves[0].position_after_move == (0, 2)
    assert moves[0].beated_pawns == [1, 0, 4]

def resolve_moves__extended_circle_state(extended_circle_state):
    board = Board(extended_circle_state)
    moves = board.resolve_moves(PawnColor('BLACK'))
    assert moves[0].pawn_id == 7
    assert moves[0].position_after_move == (6, 2)
    assert moves[0].beated_pawns == [1]
    assert moves[1].pawn_id == 8
    assert moves[1].position_after_move == (0, 6)
    assert moves[1].beated_pawns == [2]

def resolve_moves__queen_pawns_blocking_state(for_queen_blocking_pawns_state):
    board = Board(for_queen_blocking_pawns_state())
    moves = board.resolve_moves(PawnColor('BLACK'))
    assert moves[0].pawn_id == 2
    assert moves[0].position_after_move == (5, 3)
    assert moves[0].beated_pawns == [1]

    moves = board.resolve_moves(PawnColor('WHITE'))
    assert moves[0].pawn_id == 1
    assert moves[0].position_after_move == (5, 7)
    assert moves[0].beated_pawns == [4, 5]

    assert moves[1].pawn_id == 1
    assert moves[1].position_after_move == (0, 2)
    assert moves[1].beated_pawns == [2, 6]

def resolve_moevs__queen_extended_circle():
    board = Board(for_queen_blocking_pawns_state())
    moves = board.resolve_moves(PawnColor('WHITE'))
    assert moves[0].pawn_id == 1
    assert moves[0].position_after_move == (5, 3)
    assert moves[0].beated_pawns == [7, 8, 5, 6]
    assert moves[1].pawn_id == 2
    assert moves[1].position_after_move == (1, 3)
    assert moves[1].beated_pawns == [8, 7, 6, 5]
    assert moves[2].pawn_id == 3
    assert moves[2].position_after_move == (1, 3)
    assert moves[2].beated_pawns == [5, 6, 7, 8]
    assert moves[3].pawn_id == 4
    assert moves[3].position_after_move == (3, 5)
    assert moves[3].beated_pawns == [7, 6, 5, 8]

    moves = board.resolve_moves(PawnColor('BLACK'))
