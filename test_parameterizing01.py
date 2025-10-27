import pytest
import math

@pytest.mark.parametrize(("a"),[2,3,4,5,6])
def test_case01(a):
    assert type(a) != str

@pytest.mark.parametrize(("a"),[222,3333,444,555,666])
def test_case02(a):
    assert a > 40

@pytest.mark.parametrize(("a","b","c"),[(1,2,2),(2,2,4),(2,3,6),(3,3,9),(3,4,12)])
def test_case03(a,b,c):
    assert a*b == c

@pytest.mark.parametrize(("a","b"),[(5,4),(2,3),(6,3),(2,1),(8,5)])
def test_case04(a,b):
    assert a > b

data=[
    ([2,3,4],'sum',9),
    ([2,3,4],'prod',24)
]
@pytest.mark.parametrize(("a","b","c"),data)
def test_case05(a,b,c):
    if b == 'sum':
        assert sum(a) == c
    elif b == 'prod':
        assert math.prod(a) == c
