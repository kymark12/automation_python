from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
print(len(checkboxes))
option = "option2"
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == option:
        checkbox.click()
        assert checkbox.is_selected()
radio_buttons = driver.find_elements_by_name("radioButton")
radio_buttons[2].click()
radio_buttons[2].is_selected()
