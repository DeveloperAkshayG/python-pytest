"""
fixture setup and teardown using yield
"""

import pytest

weekdays1=['mon','tue','wed']
weekdays2=['fri','sat','sun']

@pytest.fixture
def setup01():
    # part of setup
    wk1=weekdays1.copy()
    wk1.append('thru')
    """
    yeild similar to return , except in return statement after return are not executed , while in yield statement after return 
    are executed 
    """
    yield wk1
    # part of teardown
    print('\n After yield in setup01 fixture....')
    wk1.pop()

@pytest.fixture()
def setup02():
    wk2=weekdays2.copy()
    wk2.insert(0,'thru')
    yield wk2

def test_extendList(setup01):
    setup01.extend(weekdays2)
    assert setup01 == ['mon','tue','wed','thru','fri','sat','sun']

def test_len(setup01,setup02):
    assert len(weekdays1 + setup02) == len(setup01 + weekdays2)