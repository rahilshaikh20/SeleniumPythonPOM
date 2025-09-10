import utils.driver_factory as util
from pages.login_page import LoginPage
import utils.constants as con
import time

def test_login_DriverFactory():
    user="Admin"

    driver = util.get_driver()
    driver.get(con.URL)
    login_page = LoginPage(driver)
    login_page.enter_username(user)
    login_page.enter_password("admin123")
    print("Username: "+user)
    login_page.click_login()

    print(driver.current_url)
    print(driver.title)

    driver.quit()
