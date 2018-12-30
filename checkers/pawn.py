from itertools import count
from checkers.pawn_color import PawnColor
from checkers.pawn_type import PawnType
from checkers.abstract_game_object import GameObj


class Pawn(GameObj):
    _id = count(1)
    color = None
    type = None
    """position y,x"""
    position = ()

    def __init__(self, position:tuple, color:PawnColor, type:PawnType):
        self.id = next(self._id)
        self.position = position
        self.color = color.name
        self.type = type.name

