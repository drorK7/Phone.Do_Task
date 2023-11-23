from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:
    def __init__(self, driver):
        self.driver = driver

    def loggedUser(self):
        return self.driver.find_element(By.CLASS_NAME, "oxd-userdropdown-name")
        
















