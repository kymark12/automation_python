# Any pytest file should start with test_, _test, _suite
# Pytest method names should start with test_
# Any code should be wrapped in method only
# Method name should have sense
# -k stands for method names execution, -s logs in output, -v stands for more info metadata
# you can run specific file with pytest <file name>
# you can mark (tag) tests with @pytest.mark.smoke using -m smoke
# you can skip tests with @pytest.mark.skip
# you can skip failed tests with @pytest.mark.xfail
# fixtures are used for setup and tear down methods for test cases
# conftest file is used to generalize fixtures and make it available to all tests
# data driven and parameterization can be done with return statements in tupple format
# when you set fixture scope="class" it will only run at the start and end of a class

import pytest


# @pytest.mark.smoke
@pytest.mark.skip
def test_first_program():
    msg = "Hello"
    assert msg == "Hi", 'Test failed because strings do not match'


@pytest.mark.xfail
def test_second_program():
    a = 4
    b = 6
    assert a + 2 == b, "Addition does not match"


def test_crossbrowser(crossbrowser):
    print(crossbrowser[1])
