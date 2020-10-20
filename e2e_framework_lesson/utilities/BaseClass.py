import inspect
import logging

import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures('setup')
class BaseClass:

    @staticmethod
    def get_logger():
        # test name fetcher
        logger_name = inspect.stack()[1][3]

        # Logger object
        logger = logging.getLogger(logger_name)

        # file handler function
        file_handler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s : %(levelname)s : %(name)s : %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)  # file handler object
        logger.setLevel(logging.DEBUG)  # log level
        return logger

    @staticmethod
    def product_selection(desired_product, co_page):
        product_list = co_page.get_products()
        for product in product_list:
            product_name = product.find_element_by_xpath(co_page.get_product_name()).text
            if product_name == desired_product:
                product.find_element_by_xpath(co_page.get_product_checkout()).click()

    def assert_success_message(self, success):
        try:
            assert "Success! Thank you!" in success
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file("screen.png")

    @staticmethod
    def select_option_by_text(locator, text):
        sel = Select(locator)
        sel.select_by_visible_text(text)
