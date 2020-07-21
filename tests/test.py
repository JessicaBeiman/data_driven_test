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
from action.login import *
from action.new_account import *
from project_var.var import *
from util.excel import *

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('useAutomationExtension', False)
driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                          executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
driver.get('https://ap8.salesforce.com/')
driver.maximize_window()

pe = ParseExcel(test_data_excel_path)
pe.set_sheet_by_name('login')
rows = pe.get_all_rows()[1:]
for id, row in enumerate(rows):
    print('row[4].value.upper(): ', row[4].value.upper())
    if row[4].value.upper() == 'Y':
        username = row[1].value
        password = row[2].value
        try:
            login(driver, username, password)
            pe.set_sheet_by_name('account')
            acc_rows = pe.get_all_rows()[1:]
            for acc_id, acc_row in enumerate(acc_rows):
                if acc_row[5].value.upper() == 'Y':
                    account_name = acc_row[1].value
                    account_number = acc_row[2].value
                    account_rating_option = acc_row[3].value
                    try:
                        message = new_account(driver, account_name, account_number, account_rating_option)
                        pe.write_cell_current_time(acc_id + 2, 7)  # 执行时间
                        if message == acc_row[4].value:
                            pe.write_cell_content(acc_id + 2, 8, 'Pass', font='green')  # 测试结果
                        else:
                            pe.write_cell_content(acc_id + 2, 8, 'Fail', font='red')  # 测试结果
                            pe.write_cell_content(acc_id + 2, 9, message)  # 实际结果
                    except Exception as e:
                        pe.write_cell_content(acc_id + 2, 8, 'Fail', font='red')  # 测试结果
                        pe.write_cell_content(acc_id + 2, 9, str(e))
        except Exception as e:
            pe.set_sheet_by_name('login')
            pe.write_cell_content(id + 2, 6, 'Fail', font='red')  # 测试结果
            pe.write_cell_content(id + 2, 7, str(e))  # 实际结果
