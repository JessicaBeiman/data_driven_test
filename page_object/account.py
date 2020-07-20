# encoding = 'utf-8'
# author = jessica
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from page_object.login_page import LoginPage
from util.parse_page_object_repository import *
from project_var.var import *
from util.object_map import *
from action.login import *


class Account(object):
    def __init__(self, driver):
        self.driver = driver
        self.parse_config_file = ParsePageObjectRepositoryConfig(page_object_repository_path)
        self.account_page_items = self.parse_config_file.get_item_section('salesforce_account')

    def get_account_link(self):
        self.driver.get('https://ap8.lightning.force.com/001/o')
        time.sleep(10)

    def get_new_button(self):
        locate_type, locate_expression = self.account_page_items['account_listview_page.new_button'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_account_name(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.account_name'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_account_number(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.account_number'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_rating_ddl(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.rating_ddl'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_rating_option(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.rating_option'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_save_button(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.save_button'].split('>')
        return get_element(self.driver, locate_type, locate_expression)

    def get_message(self):
        locate_type, locate_expression = self.account_page_items['new_account_page.message'].split('>')
        return get_element(self.driver, locate_type, locate_expression)


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://ap8.salesforce.com/')
    driver.maximize_window()
    login(driver, 'jessica.test@dev.com', 'passwordtest')
    time.sleep(20)
    acc = Account(driver)
    acc.get_account_link()
    acc.get_new_button().click()
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    acc_name_text = 'jessicatest' + timestamp
    acc.get_account_name().send_keys(acc_name_text)
    acc.get_account_number().send_keys(timestamp)
    acc.get_rating_ddl().click()
    acc.get_rating_option().click()
    acc.get_save_button().click()
    message = acc.get_message()
    assert message.text == f'Account "{acc_name_text}" was created.', 'Actual message is: ' + message.text