# pytest raises exception

import pytest

def test_case01():
    with pytest.raises(Exception):
        assert (1/0)

def test_case02():
    with pytest.raises(ZeroDivisionError):
        assert (1/0)

# TO PRINT WHAT TYPE OF EXCEPTION WE ARE GETTING THIS METHOD IS USED
def test_case03():
    with pytest.raises(Exception) as exinfo:
        assert 3 > 3
    print(str(exinfo))

def test_case04():
    with pytest.raises(AssertionError):
        assert 4<3

def func1():
    raise ValueError('valueError raised via func1')

def test_case05():
    with pytest.raises(Exception) as exinfo:
        func1()
    print(str(exinfo))
    # to print what type of exception we are getting because of error in function
    assert str(exinfo.value) == "valueError raised via func1"
