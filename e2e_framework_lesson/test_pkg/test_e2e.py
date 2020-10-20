import pytest

from e2e_framework_lesson.page_objects.checkout_page import CheckoutPage
from e2e_framework_lesson.page_objects.home_page import HomePage
from e2e_framework_lesson.utilities.BaseClass import BaseClass


class TestClass(BaseClass):

    @pytest.fixture(params=["Blackberry", "iphone X"])
    def get_desired_product(self, request):
        return request.param

    def test_e2e(self, get_desired_product):
        # log object
        log = self.get_logger()

        # page object method
        home_page = HomePage(self.driver)

        # test case actions
        checkout_page = home_page.shop_items()
        desired_product = get_desired_product
        log.info(f"The desired product is {desired_product}")
        self.product_selection(desired_product, co_page=checkout_page)
        log.info(f"{desired_product} is now added to the cart")
        confirm_page = checkout_page.click_checkout()
        log.info("Entering country name as ind")
        confirm_page.confirm_page_actions()
        log.info("India is selected as the country")
        success_text = confirm_page.get_success_text().text
        log.info(f"Success message: {success_text} is received")

        # Assert success message
        self.assert_success_message(success_text)
        self.driver.refresh()
