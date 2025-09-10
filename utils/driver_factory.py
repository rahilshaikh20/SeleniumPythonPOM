from selenium import webdriver
import utils.constants as con

def get_driver():

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(con.Wait)  # Set implicit wait
    return driver
