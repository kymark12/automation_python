import requests
from bs4 import BeautifulSoup


data = requests.get("https://rahulshettyacademy.com/AutomationPractice/")
soup = BeautifulSoup(data.content, "html.parser")
li = []
appium = soup.find('a', string='Appium')
print(appium['href'])
