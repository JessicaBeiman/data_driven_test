# encoding = 'utf-8'
# author = jessica
from page_object.account import *
from selenium import webdriver
from action.login import login


def new_account(driver, account_name, account_number='0', rating_option='--None--'):
    acc = Account(driver)
    acc.get_account_link()
    acc.get_new_button().click()
    acc.get_account_name().send_keys(account_name)
    acc.get_account_number().send_keys(account_number)
    acc.get_rating_ddl().click()
    acc.get_rating_option(rating_option).click()
    acc.get_save_button().click()
    message = acc.get_message()
    assert message.text == f'Account "{account_name}" was created.', 'Actual message is: ' + message.text


if __name__ == '__main__':
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://ap8.salesforce.com/')
    driver.maximize_window()
    login(driver, 'jessica.test@dev.com', 'passwordtest')
    time.sleep(20)
    timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    acc_name_text = 'jessicatest' + timestamp
    new_account(driver, acc_name_text, timestamp, 'Cold')
