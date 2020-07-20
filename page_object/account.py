# encoding = 'utf-8'
# author = jessica
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import traceback
from page_object.login_page import LoginPage


class Account(object):
    def __init__(self, driver):
        self.driver = driver

    def new_account(self):
        try:
            wait = WebDriverWait(self.driver, 10, 0.2)  # 显示等待
            self.driver.get('https://ap8.lightning.force.com/001/o')
            time.sleep(10)
            new_btn = wait.until(lambda x: x.find_element_by_xpath('//*[@id="brandBand_1"]//a[@title="New"]'))
            new_btn.click()
            time.sleep(10)
            timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
            acc_name_text = 'jessicatest' + timestamp
            acc_name = wait.until((lambda x: x.find_element_by_xpath(
                '//h2[contains(text(),"New Account")]/..//span[text()="Account Name"]/../following-sibling::input[1]')))
            acc_name.send_keys(acc_name_text)
            acc_num = wait.until(lambda x: x.find_element_by_xpath(
                '//h2[contains(text(),"New Account")]/..//span[text()="Account Number"]/../following-sibling::input[1]'))
            acc_num.send_keys(timestamp)
            rating_ddl = wait.until(lambda x: x.find_element_by_xpath(
                '//h2[contains(text(),"New Account")]/..//span[text()="Rating"]/../following-sibling::div[1]//a'))
            rating_ddl.click()  # 先选中drop down list, 点击，使得下拉列表中的选项visible, 然后点击选项将其选择。
            rating_item = wait.until(lambda x: x.find_element_by_xpath('//a[text()="Hot"]'))
            rating_item.click()
            save_btn = wait.until(lambda x: x.find_element_by_xpath('//*[@class="inlineFooter"]//button[3]'))
            save_btn.click()
            message = wait.until(lambda x: x.find_element_by_xpath(
                '//div[contains(@class,"slds-theme--success")]/div/div/span[contains(@class,"toastMessage")]'))
            # print(message.text)
            assert message.text == f'Account "{acc_name_text}" was created.', 'Actual message is: ' + message.text
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
    lp = LoginPage(driver)
    lp.login()
    acc = Account(driver)
    acc.new_account()