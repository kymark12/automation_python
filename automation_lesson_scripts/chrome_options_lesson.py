from selenium import webdriver
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximizeed')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-cerficate-errors')

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'), options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
