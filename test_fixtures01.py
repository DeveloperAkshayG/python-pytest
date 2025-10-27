# to run this test use command "pytest -v -k fixtures01 -s" command
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