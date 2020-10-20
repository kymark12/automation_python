from selenium.webdriver.common.by import By


class ConfirmPage:
    def __init__(self, driver):
        self.driver = driver

    success_text = (By.CSS_SELECTOR, ".alert-success")

    def confirm_page_actions(self):
        self.driver.find_element_by_id("country").send_keys("ind")
        self.driver.find_element_by_link_text("India").click()
        self.driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element_by_css_selector("[type='submit']").click()

    def get_success_text(self):
        return self.driver.find_element(*ConfirmPage.success_text)
