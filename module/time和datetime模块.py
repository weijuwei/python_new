import time

# 返回当前时间字符串 从1970.01.01 00：00：00到当前时间的秒数
print(time.time())

# 将时间戳转换为当前时区的struct_time,如果无参数，默认为当前时间
print(time.localtime(23432532))
print(time.ctime(3284353554))

# time.strftime(format[, t]) 根据指定的格式化字符串输出
print(time.strftime('%Y-%m-%d %H:%M:%S'))


print('---------------')

import datetime

# 返回当前日期
print(datetime.date.today())

# 返回当前日期时间
print(datetime.datetime.now())


t = datetime.datetime.now()
# 指定的格式输出时间日期
print(t.strftime('%Y-%m-%d %H:%M:%S') )


# 取得前一天
y = t - datetime.timedelta(days=1)
print(y)