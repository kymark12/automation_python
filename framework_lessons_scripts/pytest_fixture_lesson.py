import pytest


# @pytest.mark.usefixtures("setup")
# class TestExample:
#
#     def test_fixturemethod(self):
#         print("I will execute steps in fixturemethod method")


@pytest.mark.usefixtures("data_load")
class TestExample2:

    def test_edit_profile(self, data_load):
        print(data_load)
