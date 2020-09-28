import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

'''
Test Case
------------------------------------------------
1. Access automation practice page
2. Hover over "Mouse Over" button
3. Click either first or second option on the tooltip
'''

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
menu = driver.find_element_by_id("mousehover")
action.move_to_element(menu).perform()
top = driver.find_element_by_link_text("Reload")
action.move_to_element(top).click().perform()
