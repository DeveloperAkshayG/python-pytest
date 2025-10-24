import pytest
import sys

# TO SKIP ENTIRE TEST
pytestmark=pytest.mark.skipif(sys.platform != 'win32', reason='will run only on windows os')

const = 9/5
def cent_to_fah(cent=0):
    fah = (cent * const) + 32
    return fah

# print(cent_to_fah())

# to skip the test unconditionally without any reason
#@pytest.mark.skip()

# to skip the test with reason
@pytest.mark.skip(reason="skipped for no reason specified")
def test_case01():
    assert type(const) == float

#to skip the test based on specific condition
#@pytest.mark.skipif(sys.version_info < (3,8),reason="does not work on python version above 3.6")
#@pytest.mark.skipif(cent_to_fah() == 32,reason="default value test, so skipping")
def test_case02():
    assert cent_to_fah() == 32


# to skip based on pytest version
@pytest.mark.skipif(pytest.__version__ <  '8.4.0', reason='pytest version is less')
def test_case03():
    assert cent_to_fah(38) == 100.4