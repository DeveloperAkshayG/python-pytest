import pytest

@pytest.fixture()
def setup_tuples():
    print("in f=...\n")
    city=('mumbai','chennai','thane','jalgaon','dadar')
    return city

def test_getItem01(setup_tuples):
    assert setup_tuples[0] == 'mumbai'
    assert setup_tuples[-1] == 'dadar'

def test_mytype(setup_tuples):
    assert (type(setup_tuples[0])) == str

def test_reversetuple(setup_tuples):
    assert (setup_tuples[::-1]) == ('dadar','jalgaon','thane','chennai','mumbai')

"""
calling fixtures from markers
"""

@pytest.mark.xfail(reason="known issue:usefixtures cannot use the fixture return value")
@pytest.mark.usefixtures("setup_tuple")
def test_usefixturesdemo():
    assert (setup_tuples[0])
