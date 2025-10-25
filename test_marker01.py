import pytest

mylist = [2, 4, 5, 7, 8, 9, 10]
total= len(mylist)

# to add module level marker
pytestmark = [pytest.mark.smoke,pytest.mark.listtest]

@pytest.mark.sanity
def test_case01():
    assert (type(mylist)) == list

@pytest.mark.sanity
def test_case02():
    assert (type(mylist[0])) == int == (type(mylist[6]))

@pytest.mark.list
def test_case03():
    mylist.append(25)
    assert (len(mylist)) == total+1

@pytest.mark.sanity
@pytest.mark.list
def test_case04():
    mylist.pop(3)
    assert (len(mylist)) == total-1

def test_case05():
    assert mylist[0] == 2

def test_case06():
    assert (len([1,2,3,4,5,6,8])) == total