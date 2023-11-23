from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.NAME, "username").send_keys(username)
        
        
    def enter_password(self, password):
        self.driver.find_element(By.NAME, "password").send_keys(password)
  

    def login_button(self):
        return self.driver.find_element(By.CLASS_NAME, "orangehrm-login-button")

    def assertErrorMessage(self,text):
        element = self.driver.find_element(By.CLASS_NAME, "oxd-alert-content")
        assert element.text == f'{text}'