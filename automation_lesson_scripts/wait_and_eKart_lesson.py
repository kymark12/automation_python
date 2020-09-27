import time
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
1. Access eKart site
2. Type "ber" in the search field
3. Verify the number of items that will appear
4. Click "Add to Cart" button on each items in the search result
5. Verify if the added items into the cart are the same items in the search page
6. Input promo code
7. Verify if the discounted amount is less than the original amount
8. Verify if the sum of the total prices per product in the table, matches the total amount in the breakdown section 
'''

# Assemble section
lst = []
lst2 = []
driver = webdriver.Chrome(executable_path=os.getenv('CHROME'))
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
driver.get("https://rahulshettyacademy.com/seleniumPractise/")

# Input the search keyword "ber" and verify items displayed after search
driver.find_element_by_css_selector("input.search-keyword").send_keys("ber")
time.sleep(2)
driver.find_elements_by_xpath("//div[@class='products']/div")
count = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
assert count == 3

# Gather item names and add them into the cart by clicking "Add to Cart" button per item
buttons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in buttons:
    # Pulls the text of the item name
    lst.append(button.find_element_by_xpath("parent::div/parent::div/h4").text)
    # Clicks the "Add to Cart" button per item
    button.click()

# Go to the Cart page and verify if the added items on the search page are added properly on the cart page
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()
time.sleep(2)
veggies = driver.find_elements_by_css_selector("p.product-name")
for veg in veggies:
    lst2.append(veg.text)
print(f"Products selected in search page: {lst}")
print(f"Products added in cart page: {lst2}")
assert lst == lst2

# Verify original amount vs. discounted amount after applying promo code
original_amount = driver.find_element_by_css_selector(".discountAmt").text
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))
print("Discount "+driver.find_element_by_css_selector("span.promoInfo").text)
discount_amount = driver.find_element_by_css_selector(".discountAmt").text
assert float(discount_amount) < float(original_amount)

# Verify total amount value by summing the total amount per item in the data table
values = driver.find_elements_by_xpath("//tr/td[5]/p")
val_sum = 0
for amount in values:
    val_sum = val_sum + int(amount.text)
print("Sum of the total amount per product in the table is = "+val_sum)
total_amount = int(driver.find_element_by_class_name("totAmt").text)
assert val_sum == total_amount
