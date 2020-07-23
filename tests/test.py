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
from util.log import *

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
    if row[4].value.upper() == 'Y':
        username = row[1].value
        password = row[2].value
        try:
            login(driver, username, password)
            pe.set_sheet_by_name('account')
            acc_rows = pe.get_all_rows()[1:]
            test_data_pass_flag = True  # 结果表示，用于最后写入excel结果
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
                            test_data_pass_flag = False
                            info(u'保存失败：' + message)  # 输出日志
                            pe.write_cell_content(acc_id + 2, 9, message)  # 实际结果
                    except Exception as e:
                        pe.write_cell_content(acc_id + 2, 8, 'Fail', font='red')  # 测试结果
                        test_data_pass_flag = False
                        info(u'异常信息01：' + str(e))  # 输出日志
                        pe.write_cell_content(acc_id + 2, 9, str(e))
            if test_data_pass_flag:
                pe.set_sheet_by_name('login')
                pe.write_cell_content(id + 2, 6, 'Pass', font='green')  # 测试结果成功
            else:
                pe.set_sheet_by_name('login')
                pe.write_cell_content(id + 2, 6, 'Fail', font='red')  # 测试结果失败
        except Exception as e:
            pe.set_sheet_by_name('login')
            pe.write_cell_content(id + 2, 6, 'Fail', font='red')  # 测试结果失败
            info(u'异常信息02：', str(e))  # 输出日志
            pe.write_cell_content(id + 2, 7, str(e))  # 实际结果

# login_rows = pe.get_valid_data()
# for login_row in login_rows:
#     if login_row[u'是否执行'].upper() == 'Y':
#         username = login_row['Username']
#         password = login_row['Password']
#         try:
#             login(driver, username, password)
#             pe.set_sheet_by_name('account')
#             account_rows = pe.get_valid_data()
#             for account_row in account_rows:
#                 if account_row[u'是否执行'].upper() == 'Y':
#                     account_name = account_row[u'客户名称']
#                     account_number = account_row[u'客户编号']
#                     account_rating_option = account_row[u'客户等级']
#                     try:
#                         message = new_account(driver, account_name, account_number, account_rating_option)
#                         account_row[u'执行时间'] = str(time.strftime('%Y-%m-%d %H:%M:%S'))  # 执行时间
#                         if message == account_row[u'期望结果']:
#                             account_row[u'测试结果'] = 'Pass'
#                         else:
#                             account_row[u'测试结果'] = 'Fail'
#                             account_row[u'实际结果'] = message
#                     except Exception as e:
#                         account_row[u'测试结果'] = 'Fail'
#                         account_row[u'实际结果'] = str(e)
#             # 将字典列表account_rows写入'login' sheet
#         except Exception as e:
#             pe.set_sheet_by_name('login')
#             login_row[u'测试结果'] = 'Fail'
#             login_row[u'实际结果'] = str(e)
# # 将字典列表login_rows写入'login' sheet