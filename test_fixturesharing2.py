"""
to see which fixture is being run use below command
pytest -v -k nameoffile --setup-show -s
-s == print
"""

import pytest

def test_checkcase(setupstring):
    print(setupstring.upper())
    print(pytest.str2)
    assert setupstring.upper() == pytest.str2

def test_checktype(setupstring):

    assert type(setupstring) == str
