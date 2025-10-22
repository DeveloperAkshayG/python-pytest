# assertions example in pytest
def test_a1():
    assert 4 > 3

def test_a2():
    assert 4 <= 3

def test_a3():
    assert 4 != 3

def test_a4():
    assert "abc" == 'abc'

def test_a5():
    assert 3-1*8/4 == 1.0

def test_a6():
    assert 0 in divmod(10,2)

