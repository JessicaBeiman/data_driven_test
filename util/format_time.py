# encoding = 'utf-8'
# author = jessica
import time
from datetime import timedelta, date


def date_time_chinese():
    print(u'returns the current time string, format for YYYY年mm月dd日HH时MM分SS秒')
    return time.strftime('%Y年%m月%d日 %H时%M分%S秒'.encode('unicode_escape').decode('utf-8'), time.localtime()).encode('utf-8').decode('unicode_escape')


def date_chinese():
    print(u'returns the current time string, format for YYYY年mm月dd日')
    return time.strftime('%Y年%m月%d日'.encode('unicode_escape').decode('utf-8'), time.localtime()).encode('utf-8').decode('unicode_escape')


def time_chinese():
    print(u'returns the current time string, format for HH时MM分SS秒')
    return time.strftime('%H时%M分%S秒'.encode('unicode_escape').decode('utf-8'), time.localtime()).encode('utf-8').decode('unicode_escape')


def date_time():
    print(u'returns the current time string, format for YYYY-mm-dd HH:MM:SS')
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())


def date_time_slash():
    print(u'returns the current time string, format for YYYY/mm/dd HH:MM:SS')
    return time.strftime('%Y/%m/%d %H:%M:%S', time.localtime())


def dates():
    print(u'returns the current time string, format for YYYY-mm-dd')
    return time.strftime('%Y-%m-%d', time.localtime())


def date_slash():
    print(u'returns the current time string, format for YYYY/mm/dd')
    return time.strftime('%Y/%m/%d', time.localtime())


def times():
    print(u'returns the current time string, format for HH:MM:SS')
    return time.strftime('%H:%M:%S', time.localtime())


def year():
    print(u'returns the current time string, format for year')
    return time.strftime('%Y', time.localtime())


def month():
    print(u'returns the current time string, format for month')
    return time.strftime('%m', time.localtime())


def day():
    print(u'returns the current time string, format for day')
    return time.strftime('%d', time.localtime())


def hour():
    print(u'returns the current time string, format for hour')
    return time.strftime('%H', time.localtime())


def minute():
    print(u'returns the current time string, format for minute')
    return time.strftime('%M', time.localtime())


def seconds():
    print(u'returns the current time string, format for seconds')
    return time.strftime('%S', time.localtime())


def str_to_tuple(stime):
    print(u'returns the string variable into time tuples')
    return time.strptime(stime, '%Y-%m-%d %H:%M:%S')


def add_date(day_num):
    today = date.today()
    print('returns the current date-%s add one time interval-%s' %(today, day_num))
    times = today + timedelta(days=day_num)
    return times


def sub_date(day_num):
    today = date.today()
    print('returns the current date-%s minus one time interval-%s' %(today, day_num))
    times = today - timedelta(day_num)
    return times


if __name__ == '__main__':
    # 测试代码
    # print(date_time_chinese())
    print(date_chinese())
    print(time_chinese())
    print(date_time())
    print(date_time_slash())
    print(dates())
    print(date_slash())
    print(times())
    print(year())
    print(month())
    print(day())
    print(hour())
    print(minute())
    print(seconds())
    stime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(str_to_tuple(stime))
    print(add_date(10))
    print(sub_date(20))