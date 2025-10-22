# Test class Example
class TestMyclass:
    
    def test_type(self):
        assert type(2) == int

    def test_upper(self):
        assert(str.upper('python')) == 'PYTHON'

    def test_lower(self):
        assert (str.lower('PYTHON')) == 'PYTHON'