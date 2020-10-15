from selenium.webdriver import ActionChains
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
from selenium.webdriver.support.wait import WebDriverWait
load_dotenv(find_dotenv())
'''
Test Case
------------------------------------------------
1. Access https://chercher.tech/practice/practice-pop-ups-selenium-webdriver
2. Double click button
3. Assert alert message text
4. Close alert message
5. Context click the double click button
'''

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
actions = ActionChains(driver)
actions.context_click(driver.find_element_by_id("double-click")).perform()

actions.double_click(driver.find_element_by_id("double-click")).perform()

alert = driver.switch_to.alert
assert "You double clicked me!!!, You got to be kidding me" == alert.text
alert.accept()
