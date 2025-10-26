# code containing skip, marker and xfail
import pytest
import sys

@pytest.mark.sanity
def test_case01():
    assert 2+1 == 3

@pytest.mark.skip(reason="skipped without intention")
def test_case02():
    assert type(2) == int

@pytest.mark.sanity
def test_case03():
    assert type(2.4) == float

@pytest.mark.sanity
@pytest.mark.listtest
def test_case04():
    mylist=[1,2,3,4,5]
    assert len(mylist) == 5

@pytest.mark.xfail
def test_case05():
    mylist=[5,6,8,89,8,9]
    assert 10 in mylist

@pytest.mark.sanity
def test_case06():
    mylist=[1,25,6,7,8]
    assert type(mylist[0]) == int

@pytest.mark.xfail
def test_case07():
    str='abcd'
    num=1234
    assert str+num == 'abcd1234'

@pytest.mark.skipif(sys.platform == 'win32', reason='will run only on linux os')
def test_case08():
    mylist =[1,2,3,5,6]
    total = len(mylist)
    mylist.append(4)
    assert len(mylist) == total+1

