"""
JS DOM can access any elements on web page just like how selenium does
Selenium has a method to execute javascript code in it
"""
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element_by_name("name").send_keys("hello")

# does not ouput anything because it's not yet ouputted in DOM
print(driver.find_element_by_name("name").text)

# gets value in the textbox instead of DOM output
print(driver.find_element_by_name("name").get_attribute("value"))

# gets the value in the textbox via JS in DOM
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# clicks an element via JS
shop_button = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shop_button)

# scrolls the page via JS
driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
