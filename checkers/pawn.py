from itertools import count
from checkers.pawn_color import PawnColor
from checkers.pawn_type import PawnType
from checkers.abstract_game_object import GameObj


class Pawn(GameObj):
    id = 0
    type = ''
    """position y,x"""
    position = ()

    #todo nie używać i usunąć w przyszłości
    color = ''

    def __init__(self, id:int, position:tuple, color:PawnColor, type:PawnType):
        self.id = id
        self.position = position
        self.color = color.name
        self.type = type.name

