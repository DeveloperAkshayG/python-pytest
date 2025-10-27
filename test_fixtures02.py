"""
calling fixtures using markers:

@pytest.markers.usefixtures("setup_list")


"""
import pytest

@pytest.fixture
def setup_list():
    print('in fixtures...\n')
    city=['mumbai','pune','thane','chinchpokli','sion']
    return city

def test_getItem(setup_list):
    assert setup_list[0] == 'mumbai'
    assert setup_list[-1] == 'sion'
    assert setup_list[::2] == ['mumbai','thane','sion']

def myReverse(lst):
    lst.reverse()
    return lst

def test_reverseList(setup_list):
    assert setup_list[::-2] == ['sion','thane','mumbai']
    assert setup_list[::-1] == myReverse(setup_list)

@pytest.mark.xfail(reason="known issue:usefixtures cannot use the fixture return value")
@pytest.mark.usefixtures("setup_list")
def test_usefixturesdemo():
    assert 1 == 1
    assert (setup_list[0])