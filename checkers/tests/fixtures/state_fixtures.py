import pytest
from checkers.state import *

def makeState(dict_state: dict)->State:
    return State.from_json(json.dumps(dict_state))

@pytest.fixture
def one_pawn_at_1_1_state():
    return makeState({
    "white_pawns":
        [
        {"id":1, "position":(1,1), "color": "WHITE", "type": "NORMAL"}
        ],
    "black_pawns":
        []
    })

@pytest.fixture
def different_pawns_around_white_state():
    return makeState({
        "white_pawns":
            [
            {"id":1, "position": (3,3) , "color": "WHITE", "type": "NORMAL"},
            {"id":2, "position": (2,4), "color": "WHITE", "type": "NORMAL"},
            ],
        "black_pawns":
            [
            {"id":3, "position": (2,2), "color": "BLACK", "type": "NORMAL"},
            {"id":4, "position": (4,2), "color": "BLACK", "type": "NORMAL"},
            {"id":5, "position": (5,1), "color": "BLACK", "type": "NORMAL"},
            {"id":6, "position": (5,7), "color": "BLACK", "type": "NORMAL"},
            ]
    })

@pytest.fixture
def extended_circle_state():
    return makeState({
        "white_pawns":
            [
            {"id":1, "position": (5,3), "color": "WHITE", "type": "NORMAL"},
            {"id":2, "position": (1,5), "color": "WHITE", "type": "NORMAL"},
            {"id":3, "position": (6,0), "color": "WHITE", "type": "NORMAL"},
            {"id":4, "position": (0,2), "color": "WHITE", "type": "NORMAL"},
            ],
        "black_pawns":
            [
            {"id":5, "position":( 2, 2), "color": "BLACK", "type": "NORMAL"},
            {"id":6, "position":( 4, 2), "color": "BLACK", "type": "NORMAL"},
            {"id":7, "position":( 4, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":8, "position":( 2, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":9, "position":( 6, 6), "color": "BLACK", "type": "NORMAL"},
            {"id":10, "position":( 1, 1), "color": "BLACK", "type": "NORMAL"},
            {"id":11, "position":( 6, 4), "color": "BLACK", "type": "NORMAL"},
            ]
    })

@pytest.fixture
def extended_circle_state_no_eleven():
    return makeState({
        "white_pawns":
            [
            {"id":1, "position": (5,3), "color": "WHITE", "type": "NORMAL"},
            {"id":2, "position": (1,5), "color": "WHITE", "type": "NORMAL"},
            {"id":3, "position": (6,0), "color": "WHITE", "type": "NORMAL"},
            {"id":4, "position": (0,2), "color": "WHITE", "type": "NORMAL"},
            ],
        "black_pawns":
            [
            {"id":5, "position":( 2, 2), "color": "BLACK", "type": "NORMAL"},
            {"id":6, "position":( 4, 2), "color": "BLACK", "type": "NORMAL"},
            {"id":7, "position":( 4, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":8, "position":( 2, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":9, "position":( 6, 6), "color": "BLACK", "type": "NORMAL"},
            {"id":10, "position":( 1, 1), "color": "BLACK", "type": "NORMAL"},
            ]
    })

@pytest.fixture
def for_queen_state():
    return makeState({
        "white_pawns":
            [
            {"id":1, "position":( 4, 2), "color": "WHITE", "type": "QUEEN"},
            ],
        "black_pawns":
            [
            {"id":2, "position":( 2, 0), "color": "BLACK", "type": "NORMAL"},
            {"id":3, "position":( 2, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":4, "position":( 6, 4), "color": "BLACK", "type": "NORMAL"},
            {"id":5, "position":( 6, 6), "color": "BLACK", "type": "NORMAL"},
            ]
    })

@pytest.fixture
def for_queen_blocking_pawns_state():
    return makeState({
        "white_pawns":
            [

            {"position":( 4, 2), "color": "WHITE", "type": "QUEEN",  "id": 1},

            ],
        "black_pawns":
            [
            {"position":( 3, 1), "color": "BLACK", "type": "NORMAL",  "id": 2},
            {"position":( 2, 4), "color": "BLACK", "type": "NORMAL",  "id": 3},
            {"position":( 6, 4), "color": "BLACK", "type": "NORMAL",  "id": 4},
            {"position":( 6, 6), "color": "BLACK", "type": "NORMAL",  "id": 5},
            {"position":( 1, 1), "color": "BLACK", "type": "NORMAL",  "id": 6},
            {"position":( 1, 5), "color": "BLACK", "type": "NORMAL",  "id": 7},

            ]
    })

@pytest.fixture
def for_queen_normal_moves_state():
    return makeState({
        "white_pawns":
            [

            {"position":( 4, 2), "color": "WHITE", "type": "QUEEN",  "id": 1},

            ],
        "black_pawns":
            [

            ]
    })

@pytest.fixture
def queen_extended_circle_state():
    return makeState({
        "white_pawns":
            [

            {"position":( 7, 1), "color": "WHITE", "type": "QUEEN",  "id": 1},
            {"position":( 0, 2), "color": "WHITE", "type": "QUEEN",  "id": 2},
            {"position":( 0, 4), "color": "WHITE", "type": "QUEEN",  "id": 3},
            {"position":( 1, 7), "color": "WHITE", "type": "QUEEN",  "id": 4},

            ],
        "black_pawns":
            [
            {"position":( 2, 2), "color": "BLACK", "type": "NORMAL",  "id": 5},
            {"position":( 4, 2), "color": "BLACK", "type": "NORMAL",  "id": 6},
            {"position":( 4, 4), "color": "BLACK", "type": "NORMAL",  "id": 7},
            {"position":( 2, 4), "color": "BLACK", "type": "NORMAL",  "id": 8},

            ]
    })

@pytest.fixture
def no_blocked_beating_move_bug():
    return makeState({
        "white_pawns":
            [

            {"position":( 2, 4), "color": "WHITE", "type": "QUEEN",  "id": 1},

            ],
        "black_pawns":
            [
            {"position":( 3, 1), "color": "BLACK", "type": "NORMAL",  "id": 0},
            {"position":( 3, 3), "color": "BLACK", "type": "NORMAL",  "id": 1},

            {"position":( 1, 1), "color": "BLACK", "type": "NORMAL",  "id": 4},
            {"position":( 1, 5), "color": "BLACK", "type": "NORMAL",  "id": 5},

            ]
    })

@pytest.fixture
def only_queens_state():
    return makeState({
        "white_pawns":
            [

            {"position":( 4, 2), "color": "WHITE", "type": "QUEEN",  "id": 0},

            {"position":( 5, 1), "color": "WHITE", "type": "QUEEN",  "id": 1},

            ],
        "black_pawns":
            [
            {"position":( 3, 1), "color": "BLACK", "type": "QUEEN",  "id": 2},
            {"position":( 2, 4), "color": "BLACK", "type": "QUEEN",  "id": 3},

            ]
    })
@pytest.fixture
def black_win_state():
    return makeState({
        "white_pawns":
            [

            ],
        "black_pawns":
            [
            {"position":( 3, 1), "color": "BLACK", "type": "QUEEN",  "id": 0},
            {"position":( 2, 4), "color": "BLACK", "type": "QUEEN",  "id": 1},

            ]
    })
@pytest.fixture
def WHITE_win_state():
    return makeState({
        "white_pawns":
            [
            {"position":( 3, 1), "color": "WHITE", "type": "QUEEN",  "id": 0},
            {"position":( 2, 4), "color": "WHITE", "type": "QUEEN",  "id": 1},

            ],
            "black_pawns":
            [

            ]
    })
@pytest.fixture
def two_queens_state():
    return makeState({
        "white_pawns":
            [
            {"position":( 3, 1), "color": "WHITE", "type": "QUEEN",  "id": 0},

            ],
            "black_pawns":
            [
            {"position":( 4, 6), "color": "BLACK", "type": "QUEEN",  "id": 1},

            ]
    })
@pytest.fixture
def flower_state():
    return makeState({
        "white_pawns":
            [
            {"position":( 3, 3), "color": "WHITE", "type": "NORMAL",  "id": 0},

            ],
            "black_pawns":
            [
            {"position":( 4, 4), "color": "BLACK", "type": "NORMAL",  "id": 1},
            {"position": (2, 2), "color": "BLACK", "type": "NORMAL", "id": 2},
            {"position": (4, 2), "color": "BLACK", "type": "NORMAL", "id": 3},
            {"position": (2, 4), "color": "BLACK", "type": "NORMAL", "id": 3},

            ]
    })


@pytest.fixture
def no_moves_for_black():
    return State('{"white_pawns": [{"color": "WHITE", "id": 0, "type": "QUEEN", 1, "position":( 1,  "moves": []}, null, null, {"color": "WHITE", "id": 3, "type": "NORMAL", 7, "position":( 3,  "moves": []}, null, null, {"color": "WHITE", "id": 6, "type": "NORMAL", 3, "position":( 5,  "moves": []}, {"color": "WHITE", "id": 7, "type": "NORMAL", 7, "position":( 5,  "moves": []}, {"color": "WHITE", "id": 8, "type": "NORMAL", 1, "position":( 7,  "moves": []}, {"color": "WHITE", "id": 9, "type": "NORMAL", 5, "position":( 3,  "moves": []}, {"color": "WHITE", "id": 10, "type": "NORMAL", 6, "position":( 6,  "moves": []}, {"color": "WHITE", "id": 11, "type": "NORMAL", 7, "position":( 7,  "moves": []}], "black_pawns": [null, null, null, null, null, null, null, null, {"color": "BLACK", "id": 8, "type": "NORMAL", 0, "position":( 6,  "moves": []}, null, null, null], "winner": ""}')
