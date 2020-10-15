from time import sleep
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.get("https://makemytrip.com/")
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
sleep(2)
cities = driver.find_elements_by_xpath("//div[@id='react-autowhatever-1']/div/ul/li/div/div/p[1]")
print(len(cities))
for city in cities:
    if city.text == "Detroit, United States":
        city.click()
        break
