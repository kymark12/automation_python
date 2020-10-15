from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '../.env')
load_dotenv(dotenv_path)

""" 
The browser exposes an executable file, through selenium test we need to invoke the executable file which will then 
invoke the actual browser
"""
# driver = webdriver.Chrome(executable_path="D:\\ChromedriverRepo\\chromedriver.exe")  # Chrome
driver = webdriver.Firefox(executable_path=os.getenv('GECKO'))  # Firefox
# driver = webdriver.Firefox(executable_path=os.getenv('IE'))  # IE
driver.maximize_window()
driver.get("https://rahulshettyacademy.com")  # get method to hit url on browser
print(driver.title)
print(driver.current_url)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.quit()  # close the session, driver.close() only closes a specific window
