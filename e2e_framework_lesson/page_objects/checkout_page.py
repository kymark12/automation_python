from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//div[@class='card h-100']")
    product_name = "div/h4/a"
    product_co_btn = "div/button"

    def get_products(self):
        return self.driver.find_elements(*CheckoutPage.products)

    @staticmethod
    def get_product_name():
        return CheckoutPage.product_name

    @staticmethod
    def get_product_checkout():
        return CheckoutPage.product_co_btn
