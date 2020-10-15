import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.support.wait import WebDriverWait
load_dotenv(find_dotenv())

'''
Test Case
------------------------------------------------
1. Access iframe practice page
2. Clear multi-line text field
3. Type "I am able to automate"
4. Go back to default html content
5. Print header text
'''

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am able to automate")

driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)
