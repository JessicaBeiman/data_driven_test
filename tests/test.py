# encoding = 'utf-8'
# author = jessica
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback

from page_object.login_page import LoginPage
from page_object.account import Account

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                          executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
driver.get('https://ap8.salesforce.com/')
driver.maximize_window()
lp = LoginPage(driver)
acc = Account(driver)
try:
    lp.login()
    acc.new_account()
except TimeoutException as e:
    print(traceback.print_exc())
except NoSuchElementException as e:
    print(traceback.print_exc())
except Exception as e:
    print(traceback.print_exc())