from flask import session
from checkers.board import *
from response.response import Response
from service.game_mode import GameMode
import json


class ChecersService():
    session_keys = [
        'BOARD_STATE',
        'TURN',
        'MOVES',
        'DRAW_COUNT',
    ]

    @classmethod
    def init_game(cls, session: session, mode: GameMode):
        if not cls.session_vars_are_set(session, mode):
            suffix = cls.get_suffix(mode)

            board = Board()
            moves = board.resolve_moves(PawnColor('BLACK'))

            session['BOARD_STATE' + suffix] = board.get_state().to_json()
            session['TURN' + suffix] = 'white'
            session['DRAW_COUNT' + suffix] = 0
            session['MOVES' + suffix] = cls.moves_to_json(moves)

    @classmethod
    def clear_game(cls, session: session, mode: GameMode):
        suffix = cls.get_suffix(mode)
        for key in ChecersService.session_keys:
            if session.get(key + suffix, None): del session[key + suffix]

    @classmethod
    def get_suffix(cls, mode: GameMode)->str:
        return '_' + mode.name

    @classmethod
    def session_vars_are_set(cls, session: session, mode: GameMode ):
        for key in cls.session_keys:
            if key + cls.get_suffix(mode) in session: return True

        return False

    @classmethod
    def moves_to_json(cls, moves: list)->str:
        return json.dumps(moves, default=(lambda x: x.__dict__))

    @classmethod
    def handle_move(cls, session:session, mode: GameMode)->Response:
        suffix = ChecersService.get_suffix(mode)
        board = Board(
            State.from_json(session['BOARD_STATE' + suffix])
        )

        moves = board.resolve_moves(PawnColor('white'))
        return ''

    @classmethod
    def create_response_from_session(cls,session: session, mode: GameMode):
        suffix = cls.get_suffix(mode)
        return Response.concat_json_response_elements(
            session['BOARD_STATE' + suffix],
            session['MOVES' + suffix],
            '',
        )
