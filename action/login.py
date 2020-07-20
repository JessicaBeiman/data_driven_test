# encoding = 'utf-8'
# author = jessica

from page_object.login_page import *
from selenium import webdriver


def login(driver, username, password):
    lp = LoginPage(driver)
    lp.get_username().send_keys(username)
    lp.get_password().send_keys(password)
    lp.get_login_button().click()


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://ap8.salesforce.com/')
    driver.maximize_window()
    login(driver, 'jessica.test@dev.com', 'passwordtest')
