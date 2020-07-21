# encoding = 'utf-8'
# author = jessica

import os

# 获取工程所在目录的绝对路径
project_path = os.path.dirname(os.path.dirname(__file__))

# 获取页面对象库文件的绝对路径
page_object_repository_path = project_path + u'/config/page_object_repository.ini'

# 获取测试数据excel文件的绝对路径
test_data_excel_path = project_path + u'/test_data/test_data.xlsx'


if __name__ == '__main__':
    print('project_path: ', project_path)
    print('page_object_repository_path: ', page_object_repository_path)
    print(os.path.exists(project_path))
    print(os.path.exists(page_object_repository_path))