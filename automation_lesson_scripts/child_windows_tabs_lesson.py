import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

'''
Test Case
------------------------------------------------
1. Access windows practice page
2. Click "Click Here" link
3. Print h3 label on new window/tab
4. Close tab
5. Assert parent window h3
'''

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()
child_window = driver.window_handles[1]
driver.switch_to.window(child_window)
print(driver.find_element_by_tag_name("h3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
assert "Opening a new window" == driver.find_element_by_tag_name("h3").text
