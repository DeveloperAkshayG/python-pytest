import pytest
import sys

pytestmark=pytest.mark.skipif(sys.platform == 'win32', reason='will run only on linux os')

const = 10

def add_to_const(cent=0):
    res = (cent * const) + 64
    return res


#@pytest.mark.skip(reason='skipped for no reason specified')
def test_case01():
    assert type(const) == int

#@pytest.mark.skipif(add_to_const() == 64,reason='default test so skipping')
def test_case02():
    assert add_to_const() == 64

#@pytest.mark.skipif(pytest.__version__ <  '8.4.0', reason='pytest version is less')
def test_case03():
    assert  add_to_const(0.6) == 70