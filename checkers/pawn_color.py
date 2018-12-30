from enum import Enum


class PawnColor(Enum):
    WHITE = 'white'
    BLACK = 'black'

    def opposite(self):
        return PawnColor('black') if self.value == 'white' else PawnColor('black')
