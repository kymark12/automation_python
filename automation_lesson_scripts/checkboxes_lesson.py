from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

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
