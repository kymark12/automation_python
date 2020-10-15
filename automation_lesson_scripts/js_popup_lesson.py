from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element_by_css_selector("#name").send_keys("Option3")
driver.find_element_by_id("alertbtn").click()
alert = driver.switch_to.alert
print(alert.text)
alert.accept()
