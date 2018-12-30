from flask import session
from checkers.board import *
from service.session_key import SessionKey
from service.game_mode import GameMode
import json


class ChecersService():
    pass
    # @classmethod
    # def init_game(self, session: session, mode: GameMode):
    #     if mode.name == 'HOT_SEATS':
    #         board = Board()
    #         state = board.get_state()
    #         settings = {
    #             'turn': 'white',
    #             'board_state': json.dumps(state, la)
    #
    #         }
