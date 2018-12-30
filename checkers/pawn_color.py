from enum import Enum


class PawnColor(Enum):
    WHITE = 'WHITE'
    BLACK = 'BLACK'

    def opposite(self):
        return PawnColor('BLACK') if self.name == 'WHITE' else PawnColor('BLACK')
