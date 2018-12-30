import pytest
from checkers.pawn import *
from copy import deepcopy

def test_opposite():
    color = PawnColor('white')
    assert 'BLACK' == color.opposite().name

    color = PawnColor('black')
    assert 'WHITE' == color.opposite().name

    with pytest.raises(ValueError):
        PawnColor('bad_color')

def test_pawns_eq():
    pawn1 = Pawn((1,1), PawnColor('white'), PawnType('queen'))
    pawn2 = Pawn((1,2), PawnColor('black'), PawnType('queen'))
    pawn3 = deepcopy(pawn1)

    assert False == (pawn1 == pawn2)
    assert True == (pawn1 == pawn3)
