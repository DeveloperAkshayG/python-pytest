"""
fixture sharing from conftest file
"""
import pytest

def test_delItems(setup01):
    del setup01[-1]
    print(setup01)
    assert setup01 == pytest.weekdays1

def test_removeItems(setup02):
    print(setup02)
    setup02.remove('thru')
    assert setup02 == pytest.weekdays2