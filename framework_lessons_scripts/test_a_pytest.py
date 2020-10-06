# Any pytest file should start with test_, _test, _suite
# Pytest method names should start with test_
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# you can run specific file with pytest <file name>

def test_first_program():
    msg = "Hello"
    assert msg == "Hi", 'Test failed because strings do not match'


def test_second_program():
    a = 4
    b = 6
    assert a + 2 == b, "Addition does not match"
