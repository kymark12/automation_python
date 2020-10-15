from time import sleep
from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Firefox(executable_path=os.getenv('GECKO'))
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element_by_id("autosuggest").send_keys("Ind")
sleep(2)
countries = driver.find_elements_by_css_selector('li[class="ui-menu-item"] a')
# print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
print(driver.find_element_by_id("autosuggest").text)
assert driver.find_element_by_id("autosuggest").get_attribute('value') == "India"
