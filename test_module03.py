# pytest raises exception example 2

import pytest
def test_case01():
    with pytest.raises(ZeroDivisionError):
        assert (4/0)

def test_case02():
    with pytest.raises(AssertionError):
        assert 'a' in 'python'

def test_case03():
    with pytest.raises(Exception):
        assert 4 == 3

def test_case04():
    with pytest.raises(Exception):
        assert -3 + 2 == 1

def func1():
    raise ValueError('exception raised from func1')

def test_case05():
    with pytest.raises(Exception) as exinfo:
        func1()
    print(str(exinfo))
    assert str(exinfo.value) == "exception raised from func1"
