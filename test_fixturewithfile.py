import pytest
import os

filename ='file1.txt'

@pytest.fixture()
def setup01():
    f=open(filename,'w')
    f.write('Learning pytest....')
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)

def test_checkfile(setup01):
    assert (setup01.readline()) == 'Learning pytest....'
    