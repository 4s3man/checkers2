import pytest
from checkers.move import Move

def test_json_convert():
    move = Move(1, (1,2), [1])
    move.set_id(1)
    json_move = move.to_json()

    converted_move = Move.from_json(json_move)

    assert isinstance(converted_move, Move)
    assert converted_move.id == 1
    assert converted_move.position_after_move == (1,2)
    assert converted_move.pawn_id == 1
    assert converted_move.beated_pawns == [1]
