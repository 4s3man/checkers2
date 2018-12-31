from checkers.vec import Vec

def test_add():
    assert (6, -4) == (Vec((1,1)) + Vec((5,-5))).vec
    assert (6, 5) != (Vec((1, 1)) + Vec((5, -5))).vec

def test_mul():
    assert (2,-2) == (Vec((1,-1)) * 2).vec

def test_eq():
    t1 = (1,1)
    t2 = (2,2)
    t3 = (1,1)

    assert Vec(t1) != Vec(t2)
    assert Vec(t3) == t1

    assert Vec(t1) == Vec(t3)
    assert Vec(t1) != Vec(t2)