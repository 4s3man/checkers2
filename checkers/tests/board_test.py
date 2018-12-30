from checkers.board import *

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