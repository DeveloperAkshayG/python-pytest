"""
setup and teardown another example in pytest
"""

import pytest

str1="india"
str2="INDIA"

@pytest.fixture()
def setup02():
    s1=str1
    yield s1
    print('\n After yeild in setup02 fixture....')
    del s1

def test_mycase(setup02):
    assert setup02.upper() == str2



