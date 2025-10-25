# to run the xfail marker use command 'pytest -v filepath'

import pytest

def test_strjoin():
    s1= 'Python,Pytest and Automation'
    l1=['Python,Pytest', 'and', 'Automation']
    assert ' '.join(l1) == s1

"""
reason we only provide for documentation of code ,it is not compulsory to provide reason with xfail ,just 
for documentation we provide the reason
"""
@pytest.mark.xfail(raises=IndexError,reason="known issue")
def test_str04():
    letters = 'abcdefghijklmnopqrstuvwxyz'
    assert letters[100]
    # adding the condition that pass the test
    #assert letters[10]

@pytest.mark.xfail
def test_str05():
    letters = 'abcd'
    num = 1234
    assert letters + num == 'abcd1234'