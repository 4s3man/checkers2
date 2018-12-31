class Vec():
    vec = (0, 0)

    def __init__(self, yx: tuple):
        self.vec = yx

    def __eq__(self, other)->bool:
        if not isinstance(other, Vec): return False
        return self.vec[0] == other.vec[0] and self.vec[1] == other.vec[1]

    def __ne__(self, other: iter)->bool:
        if not isinstance(other, Vec): return False
        return not self.__eq__(other)

    def __add__(self, other):
        assert isinstance(other, Vec)
        return Vec(self.vec[0] + other.vec[0], self.vec[1] + other.vec[1])

    def __sub__(self, other):
        assert isinstance(other, Vec)
        return Vec(self.vec[0] - other.vec[0], self.vec[1] - other.vec[1])

    def __iadd__(self, other):
        assert isinstance(other, Vec)
        self.vec[0] + other.vec[0]
        self.vec[1] + other.vec[1]

    def __isub__(self, other):
        self.vec[0] - other.vec[0]
        self.vec[1] - other.vec[1]
