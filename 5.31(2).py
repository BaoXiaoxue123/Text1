'''import time

a = time.time()
# 计算当前时间点的时间与a会见的时间间隔，以秒为单位
for x in range(100000):
    pass
b = time.time() -a
print(b)
# 第一次调用时，返回程序实际的运行时间
print(time.perf_counter())
# 第二次调用返回的是距离上一次调用的时间间隔
print(time.perf_counter())
# 前次调用返回的是距离上一次调用的时间间隔
print(time.perf_counter())
print(time.gmtime())
print(time.localtime())
a = time.time()
time.localtime(a)'''
from datetime import time

'''# 3秒暂停
import time

print("start:%s" % time.ctime())
time.sleep(3)
print("End:%s" % time.ctime())
# 生成固定的时间表示格式
print(time.time())
print(time.ctime(time.time()))'''


'''import time


a = time.strftime("%Y-%m-%d", time.gmtime())
print(a) 
b = time.strftime("%Y-%m-%d %X")
print(b)
c = time.strftime("%x %X")
print(c)'''

import calendar


calendar.prmonth(2021, 11, 0)
calendar.prmonth(2021, 11, 1)
calendar.prmonth(2021, 11,2)#w=0,1, 2 have the same effect.
calendar.prmonth(2021, 11, 3) # w = 3 has the difference effect than w <= 2
calendar.setfirstweekday(1)
calendar.prmonth(2021, 11)
# 2018年是平年，所以为False
print(calendar.isleap(2018))
# False#2008年是如年，所以为True
print(calendar.isleap(2008))
# True