# encoding = 'utf-8'
# author = jessica

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10, 0.2)  # 显示等待

    def get_username(self, locate_type, locate_expression):
        username = self.wait.until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return username

    def get_password(self, locate_type, locate_expression):
        password = self.wait.until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return password

    def get_login_button(self, locate_type, locate_expression):
        submit = self.wait.until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return submit


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://ap8.salesforce.com/')
    driver.maximize_window()
    lp = LoginPage(driver)
    lp.get_username('xpath', '//*[@id="username"]').send_keys('jessica.test@dev.com')
    lp.get_password('xpath', '//*[@id="password"]').send_keys('passwordtest')
    lp.get_login_button('xpath', '//*[@id="Login"]').click()
    driver.switch_to.default_content()
    time.sleep(20)
    assert 'Home' in driver.page_source, '"Home" not exist in page_source.'
