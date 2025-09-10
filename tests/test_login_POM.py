from selenium import webdriver
from pages.login_page import LoginPage
import utils.constants as const
import time

def test_login_HardCoded():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(const.URL) #Get URL from constants.py
    driver.implicitly_wait(const.Wait)

    login_page = LoginPage(driver)
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    time.sleep(5)  # wait for navigation or assertion
    driver.quit()
