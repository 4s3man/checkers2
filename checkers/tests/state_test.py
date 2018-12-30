import pytest
from checkers.state import State
from checkers.tests.fixtures.state_fixtures import *
from copy import deepcopy

def test_equall(for_queen_blocking_pawns_state):
    s = for_queen_blocking_pawns_state
    s1 = State([], [])

    assert s != s1

    s2 = deepcopy(s1)
    assert s2 == s1

def test_json_convert(for_queen_blocking_pawns_state):
    s = for_queen_blocking_pawns_state
    s.to_json() == {"white_pawns": [{"id": 1, "position": [4, 2], "color": "WHITE", "type": "QUEEN"}],
     "black_pawns": [{"id": 0, "position": [3, 1], "color": "BLACK", "type": "NORMAL"},
                     {"id": 1, "position": [2, 4], "color": "BLACK", "type": "NORMAL"},
                     {"id": 2, "position": [6, 4], "color": "BLACK", "type": "NORMAL"},
                     {"id": 3, "position": [6, 6], "color": "BLACK", "type": "NORMAL"},
                     {"id": 4, "position": [1, 1], "color": "BLACK", "type": "NORMAL"},
                     {"id": 5, "position": [1, 5], "color": "BLACK", "type": "NORMAL"}]}

    s1 = State.from_json(s.to_json())
    assert s == s1
