import pytest
import os

filename = 'file.txt'

@pytest.fixture()
def setupfile():
    f=open(filename,'w')
    f.write('chintamani')
    f.close()
    f = open(filename, 'r+')
    yield f
    f.close()
    os.remove(filename)

def test_checkfiledata(setupfile):
    assert (setupfile.readline()) == 'chintamani'

def test_checktypedata(setupfile):
    assert type(setupfile.readline()) == str