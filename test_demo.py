# demo script demonstrating use of pytest
# run the script by using command "pytest pytest_topics" or "pytest -v pytest_topics"

# test no 1
def test_a1():
    assert  5+5 == 10
    assert  5-5 == 0
    assert  5*5 == 25
    assert  5/5 == 1

# test no 2
def test_a2():
    assert 5/5 == 1.5, "failed intentionally"

# test no 3
def test_a3():
    assert 5//5 == 1  #integer truncating division