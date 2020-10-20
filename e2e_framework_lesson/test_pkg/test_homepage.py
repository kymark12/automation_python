from selenium.webdriver.support.select import Select
from selenium import webdriver
import pytest

from data_sets.homepage_datasets import HomePageData
from page_objects.home_page import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):

    def test_formSubmission(self, get_data):
        log = self.get_logger()
        homepage= HomePage(self.driver)
        log.info("first name is "+get_data["firstname"])
        homepage.get_name().send_keys(get_data["firstname"])
        homepage.get_email().send_keys(get_data["lastname"])
        homepage.get_checkBox().click()
        self.select_option_by_text(homepage.get_gender(), get_data["gender"])

        homepage.submit_form().click()

        alertText = homepage.get_success_message().text

        assert ("Success" in alertText)
        self.driver.refresh()

    @pytest.fixture(params=HomePageData.test_homepage_data)
    def get_data(self, request):
        return request.param
