import pytest


@pytest.mark.sanity
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", 'Test failed because strings do not match'


def test_second_program():
    a = 4
    b = 6
    assert a + 2 == b, "Addition does not match"
