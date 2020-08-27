from time import sleep

from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

driver = webdriver.Firefox(executable_path=os.getenv('GECKO'))
driver.get("https://rahulshettyacademy.com/angularpractice")
driver.find_element_by_name("name").send_keys("Marky")
"""
Xpath and CSS Selector validation can be done through the dev tool's console using $('selector') for CSS and 
$x('selector') for Xpath
"""
driver.find_element_by_css_selector('input[name="email"]').send_keys("ivan.berbenzana@zenrooms.com")
driver.find_element_by_id("exampleCheck1").click()
sleep(5)
driver.close()
