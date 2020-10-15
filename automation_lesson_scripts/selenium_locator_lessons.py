from time import sleep

from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

driver = webdriver.Firefox(executable_path=os.getenv('GECKO'))
# driver.get("https://rahulshettyacademy.com/angularpractice")
# driver.find_element_by_name("name").send_keys("Marky")
# """
# Xpath and CSS Selector validation can be done through the dev tool's console using $('selector') for CSS and
# $x('selector') for Xpath
# """
# driver.find_element_by_css_selector('input[name="name"]').clear()
# driver.find_element_by_css_selector('input[name="name"]').send_keys("Mark Ivan")
# driver.find_element_by_name('email').send_keys("ivan.berbenzana@zenrooms.com")
#
# driver.find_element_by_id("exampleCheck1").click()
#
# driver.find_element_by_xpath('//input[@type="submit"]').click()
#
# # Class name example
# # print(driver.find_element_by_class_name("alert-success").text)
#
# # Using contains locator techniques Xpath
# # print(driver.find_elements_by_xpath('//*[contains(@class, "success")]').text)
#
# # Using contains locator techniques CSS
# print(driver.find_element_by_css_selector('[class*="success"]').text)

driver.get("https://login.salesforce.com/?locale=ap")

driver.find_element_by_css_selector("#username").send_keys("marky")
driver.find_element_by_css_selector(".password").send_keys("berbenzana")
driver.find_element_by_css_selector(".password").clear()
driver.find_element_by_partial_link_text("Forgot").click()
# Finding elements using text (Xpath only)
driver.find_element_by_xpath('//a[text()="Cancel"]').click()

sleep(5)
driver.close()
