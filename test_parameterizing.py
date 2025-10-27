# parameterizing in pytest

import pytest

@pytest.mark.parametrize(("a"),[5,6,7,8,2.5])
def test_case01(a):
    assert type(a) == int

@pytest.mark.parametrize(("a"),[55,56,756,75,40])
def test_case02(a):
    assert a > 50

@pytest.mark.parametrize(("a","b"),[(1,3),(2,4),(3,5),(4,6),(5,8)])
def test_case03(a,b):
    assert a+2 == b