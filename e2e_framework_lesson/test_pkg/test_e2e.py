from e2e_framework_lesson.page_objects.checkout_page import CheckoutPage
from e2e_framework_lesson.page_objects.home_page import HomePage
from e2e_framework_lesson.utilities.BaseClass import BaseClass


class TestClass(BaseClass):

    def test_e2e(self):
        home_page = HomePage(self.driver)
        # test case actions
        home_page.shop_items().click()
        checkout_page = CheckoutPage(self.driver)
        desired_product = "Blackberry"
        products = checkout_page.get_products()
        for product in products:
            product_name = product.find_element_by_xpath(checkout_page.get_product_name()).text
            if product_name == desired_product:
                product.find_element_by_xpath(checkout_page.get_product_checkout()).click()
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()
        self.driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
        self.driver.find_element_by_id("country").send_keys("ind")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()
        success_text = self.driver.find_element_by_css_selector(".alert-success").text

        # Assert success message
        try:
            assert "Success! Thank you!" in success_text
        except Exception as e:
            print(e)
            self.driver.get_screenshot_as_file("screen.png")
