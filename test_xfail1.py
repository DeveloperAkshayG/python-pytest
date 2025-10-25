import pytest

def test_str07():
    str1 = "nun"
    assert str1 == str1[::-1]

@pytest.mark.xfail(raises= IndexError,reason="known issue")
def test_str08():
    mylist = [2,4,5,6,7]
    assert mylist[6]

@pytest.mark.xfail()
def test_str09():
    str1 = "akshay dob is "
    num = 14
    assert str1 + num == "akshay dob is14"