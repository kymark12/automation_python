from selenium import webdriver
import os
from os.path import join, dirname
from dotenv import load_dotenv
dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--start-maximizeed')
chrome_options.add_argument('--headless')
chrome_options.add_argument('--ignore-cerficate-errors')

driver = webdriver.Chrome(executable_path=os.getenv('CHROME'), options=chrome_options)
driver.get("https://rahulshettyacademy.com/angularpractice/")

print(driver.title)
