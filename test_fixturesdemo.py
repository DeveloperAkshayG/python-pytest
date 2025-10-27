#fixtures in pytest

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