"""
using conftest.py we can share the fixtures among multiple test file
"""

import pytest

def pytest_configure():
    pytest.weekdays1=['mon','tue','wed']
    pytest.weekdays2=['fri','sat','sun']
    pytest.str1 = 'india'
    pytest.str2 = 'INDIA'

@pytest.fixture(scope="module")
def setup01():
    wk=pytest.weekdays1.copy()
    wk.append('thru')
    yield wk
    print('\n Fixture1 setup closing')
    # wk.pop()

@pytest.fixture()
def setup02():
    wk2=pytest.weekdays2.copy()
    wk2.insert(0,'thru')
    yield wk2

@pytest.fixture()
def setupstring():
    s1=pytest.str1
    yield s1
