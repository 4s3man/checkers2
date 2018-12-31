class Vec():
    vec = ()

    def __init__(self, yx: tuple):
        assert len(yx) == 2
        self.vec = yx

    def __add__(self, other):
        assert isinstance(other, Vec)
        return Vec(tuple(self.vec[i] + other.vec[i] for i in range(2)))

    def __mul__(self, other):
        assert isinstance(other, int)
        return Vec(tuple(self.vec[i] * other for i in range(2)))

    def __eq__(self, other):
        if isinstance(other, Vec):
            return self.vec == other.vec
        elif isinstance(other, tuple) and 2 == len(other):
            return self.vec == other
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)
