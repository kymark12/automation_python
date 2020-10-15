from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
assert driver.find_element_by_id("displayed-text").is_displayed()
driver.find_element_by_id("hide-textbox").click()
assert not driver.find_element_by_id("displayed-text").is_displayed()
