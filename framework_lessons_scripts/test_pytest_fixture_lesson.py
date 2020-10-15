import pytest
from framework_lessons_scripts.BaseClass import BaseClass

# @pytest.mark.usefixtures("setup")
# class TestExample:
#
#     def test_fixturemethod(self):
#         print("I will execute steps in fixturemethod method")


@pytest.mark.usefixtures("data_load")
class TestExample2(BaseClass):

    def test_edit_profile(self, data_load):
        log = self.get_logger()
        log.info(data_load[0])
        log.info(data_load[2])
