import os
from selenium import webdriver
import pytest
from configparser import ConfigParser
import time
from selenium.webdriver.chrome.service import Service


project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
config = ConfigParser()
config.read(os.path.join(project_root, "selenium_Python", "utils", "config.ini"))

@pytest.fixture(scope="session")
def browser():
    options = webdriver.ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    options.add_argument("--disable-setuid-sandbox")
    # Construct the chromedriver path relative to the project root
    service = Service(os.path.join(project_root, "selenium_Python", "drivers", "chromedriver.exe"))
    driver = webdriver.Chrome(service=service, options=options) 
    driver.implicitly_wait(10)

    yield driver
    

    time.sleep(5)
    driver.quit()
#Navigates and allows to reach homepage each test run.
@pytest.fixture(scope="function", autouse=True)
def navigate_to_login(browser):
    browser.delete_all_cookies()
    browser.refresh()
    browser.get(config.get("web", "login_url"))
    
