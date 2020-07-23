# encoding = 'utf-8'
# author = jessica
from selenium.webdriver.support.ui import WebDriverWait
import time


# 获取单个元素对象
def get_element(driver, locate_type, locate_expression):
    try:
        element = WebDriverWait(driver, 60).until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return element
    except Exception as e:
        raise e


# 获取多个相同页面元素对象，返回list
def get_elements(driver, locate_type, locate_expression):
    try:
        elements = WebDriverWait(driver, 60).until(lambda x: x.find_element(by=locate_type, value=locate_expression))
        return elements
    except Exception as e:
        raise e


if __name__ == '__main__':
    from selenium import webdriver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=chrome_options.to_capabilities(),
                              executable_path='C:\\PycharmProjects\\data_driven_test\\chromedriver.exe')
    driver.get('https://www.baidu.com/')
    driver.maximize_window()
    search_box = get_element(driver, 'xpath', '//input[@id="kw"]').send_keys('test')
    time.sleep(5)
    driver.quit()