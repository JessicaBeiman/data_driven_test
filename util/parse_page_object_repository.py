# encoding = 'utf-8'
# author = jessica

from configparser import ConfigParser


class ParsePageObjectRepositoryConfig(object):

    def __init__(self, config_path):
        self.cf = ConfigParser()  # 生成解析器
        self.cf.read(config_path)

    def get_item_section(self, section_name):
        # print(self.cf.items(section_name))
        return dict(self.cf.items(section_name))

    def get_option_value(self, section_name, option_name):  # 返回一个字典
        # print(self.cf.get(section_name, option_name))
        return self.cf.get(section_name, option_name)


if __name__ == '__main__':
    pp = ParsePageObjectRepositoryConfig('C:\\PycharmProjects\\data_driven_test\\config\\page_object_repository.ini')
    print(pp.get_item_section('salesforce_login'))
    print(pp.get_option_value('salesforce_login', 'login_page.username'))