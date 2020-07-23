# encoding = 'utf-8'
# author = jessica
import logging
import logging.config
from project_var.var import *

# 读取日志的配置文件
logging.config.fileConfig(project_path + '\\config\\logger.conf')

# 选择一个日志格式
logger = logging.getLogger('example02')


def error(message):
    # 打印debug级别的信息
    logger.error(message)


def info(message):
    # 打印info级别的信息
    logger.info(message)


def warning(message):
    # 打印warning级别的信息
    logger.warning(message)


if __name__ == '__main__':
    # 测试代码
    info('hi')
    print('config file path: ', project_path + '\\config\\logger.conf')
    error('world!')
    warning('test!')