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

    def login(self):
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)  # 显示等待
            username = wait.until(lambda x: x.find_element_by_xpath('//*[@id="username"]'))
            username.send_keys('jessica.test@dev.com')
            password = wait.until(lambda x: x.find_element_by_xpath('//*[@id="password"]'))
            password.send_keys('passwordtest')
            submit = wait.until(lambda x: x.find_element_by_xpath('//*[@id="Login"]'))
            submit.click()
            self.driver.switch_to.default_content()
            time.sleep(20)
            assert 'Home' in self.driver.page_source, '"Home" not exist in page_source.'

        except TimeoutException as e:
            print(traceback.print_exc())
        except NoSuchElementException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://ap8.salesforce.com/')
    driver.maximize_window()
    login = LoginPage(driver)
    login.login()