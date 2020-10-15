from dotenv import load_dotenv, find_dotenv
import os
import pytest

from selenium import webdriver
load_dotenv(find_dotenv())


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome", help="selects what browser to run"
    )


@pytest.fixture(scope='class')
def setup(request):
    driver = ''
    browser_name = request.config.getoption("browser_name")
    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        # chrome_options.add_argument('--headless')
        chrome_options.add_argument('--window-size=1920,1080')
        chrome_options.add_argument('--ignore-cerficate-errors')
        driver = webdriver.Chrome(executable_path=os.getenv('CHROME'), options=chrome_options)
    elif browser_name == "firefox":
        driver = webdriver.Firefox(executable_path=os.getenv('GECKO'))
    elif browser_name == "IE":
        driver = webdriver.Firefox(executable_path=os.getenv('IE'))
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    request.cls.driver = driver
    yield
    driver.close()
