from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

"""
Test Case:
-----------------------------------------
1. Access site
2. Go to Shop
3. Add "Blackberry" product into cart
4. Click Checkout
5. Click Proceed
6. Search "Ind"
7. Select "India" on the dynamic list
8. Click checkbox for T&C
9. Click Submit button
10. Assert success message
"""

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximizeed')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--window-size=1920,1080')
chrome_options.add_argument('--ignore-cerficate-errors')

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'), options=chrome_options)
driver.implicitly_wait(10)
driver.get("https://rahulshettyacademy.com/angularpractice/")

# test case actions
driver.find_element_by_css_selector("a[href*='shop']").click()
desired_product = "Blackberry"
products = driver.find_elements_by_xpath("//div[@class='card h-100']")
for product in products:
    product_name = product.find_element_by_xpath("div/h4/a").text
    if product_name == desired_product:
        product.find_element_by_xpath("div/button").click()
driver.find_element_by_css_selector("a[class*='btn-primary']").click()
driver.find_element_by_xpath("//button[@class='btn btn-success']").click()
driver.find_element_by_id("country").send_keys("ind")
driver.find_element_by_link_text("India").click()
driver.find_element_by_xpath("//div[@class='checkbox checkbox-primary']").click()
driver.find_element_by_css_selector("[type='submit']").click()
success_text = driver.find_element_by_css_selector(".alert-success").text

# Assert success message
try:
    assert "Success! Thank you!" in success_text
except Exception as e:
    print(e)
    driver.get_screenshot_as_file("screen.png")
