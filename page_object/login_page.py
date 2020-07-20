# encoding = 'utf-8'
# author = jessica

from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from util.parse_page_object_repository import *
from project_var.var import *


class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig(page_object_repository_path)
        self.login_page_items = self.parse_config_file.get_item_section('salesforce_login')
        self.wait = WebDriverWait(self.driver, 10, 0.2)  # 显示等待

    def get_username(self):
        locate_type, locate_expression = self.login_page_items['login_page.username'].split('>')
        username = self.wait.until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return username

    def get_password(self):
        locate_type, locate_expression = self.login_page_items['login_page.password'].split('>')
        password = self.wait.until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return password

    def get_login_button(self):
        locate_type, locate_expression = self.login_page_items['login_page.login_button'].split('>')
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
    lp.get_username().send_keys('jessica.test@dev.com')
    lp.get_password().send_keys('passwordtest')
    lp.get_login_button().click()
    driver.switch_to.default_content()
    time.sleep(20)
    assert 'Home' in driver.page_source, '"Home" not exist in page_source.'
