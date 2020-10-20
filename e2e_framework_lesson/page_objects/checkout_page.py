from selenium.webdriver.common.by import By

from e2e_framework_lesson.page_objects.confirm_page import ConfirmPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    product_name = "div/h4/a"
    product_co_btn = "div/button"
    checkout_btn = (By.CSS_SELECTOR, "a[class*='btn-primary']")
    cont_checkout_btn = (By.XPATH, "//button[@class='btn btn-success']")

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.products)

    @staticmethod
    def get_product_name():
        return CheckoutPage.product_name

    @staticmethod
    def get_product_checkout():
        return CheckoutPage.product_co_btn

    def click_checkout(self):
        self.driver.find_element(*CheckoutPage.checkout_btn).click()
        self.driver.find_element(*CheckoutPage.cont_checkout_btn).click()
        confirm_page = ConfirmPage(self.driver)
        return confirm_page
