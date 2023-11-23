from selenium.webdriver.common.by import By
from ..pages.LoginPage import LoginPage
from ..pages.HomePage import HomePage
from ..conftest import browser, navigate_to_login

#This test checks valid login
def test_validLogin(browser):
    login_page = LoginPage(browser)
    home_page = HomePage(browser)
    # Enter username and password
    login_page.enter_username('Admin')
    login_page.enter_password('admin123')
    # Click on the login button
    login_page.login_button().click()
    # Assert that the dashboard page is loaded
    assert 'PaulJohn CollingsJohn' in home_page.loggedUser().text


#This test checks invalid login and asserts the error message
def test_invalidLogin(browser):
    login_page = LoginPage(browser)
    # Enter username and password
    login_page.enter_username('Admin1')
    login_page.enter_password('admin1234')
    # Click on the login button
    login_page.login_button().click()
    # Assert the error message
    login_page.assertErrorMessage('Invalid credentials')
