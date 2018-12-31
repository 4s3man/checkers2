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


def test_position_generator(different_pawns_around_white_state):
    board = Board(different_pawns_around_white_state)
    board.enemies = board.get_pawns(PawnColor('BLACK'))
    gen = board.enemy_position_generator()
    for x in gen:
        assert x in [[2,2], [4,2], [5,1], [5,7]]

    board.enemies = board.get_pawns(PawnColor('WHITE'))
    gen1 = board.enemy_position_generator()
    for x in gen1:
        assert x in [[3,3], [2,4]]

    board.enemies = None
    with pytest.raises(InvalidUsageException):
        gen1 = board.enemy_position_generator()

    del board.enemies
    with pytest.raises(InvalidUsageException):
        gen1 = board.enemy_position_generator()

def test_generate_jump_directions(different_pawns_around_white_state):
    board = Board(different_pawns_around_white_state)
    board.enemies = board.get_pawns(PawnColor('BLACK'))
    gen = board.generate_jump_directions(board.white_pawns[0])
    for x in gen:
        print(x)
