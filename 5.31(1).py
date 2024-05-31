'''datetime import datetime


a = datetime.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
print(a.date())'''


'''import datetime


a = datetime.date.today()
print(a)
print(a.year)
print(a.month)
print(a.day)
a = datetime.date(2024, 4, 28)
b = datetime.date(2017, 3, 15)
print(a.__eq__(b))
print(a.__ge__(b))
print(a.__gt__(b))
print(a.__le__(b))
print(a.__lt__(b))
print(a.__ne__(b))
print(a.__sub__(b))
print(a.__rsub__(b))
'''
'''
eq  等于x==y
ge  大于等于x>=y
gt  大于x>y
le  小于等于x<=y
lt  小于x<y
ne  不等于x!=y


'''


'''import datetime
a = datetime.date.today()


print(a.__format__('%Y-%m-%d'))
print(a.__format__('%Y/%m/%d'))
print(a.__format__('%y-%m-%d'))
print(a.__format__('%y/%m/%d'))
print(a.__format__('%D'))
print(a.__format__('%d'))


from datetime import time
a = datetime.time(8, 50, 30, 899)
print(a)'''


from datetime import *


d = date(2012, 12, 12)
print(d)


#昨天
d1 = d + timedelta(days=-1)
print(d1)
#明天
d2 = d + timedelta(days=1)
print(d2)


from datetime import *

dt = datetime(2012, 12, 12, 23, 59, 59)
print(dt)
# 昨天
dt1 = dt + timedelta(days=-1)
print(dt1)
# 明天
dt2 = dt + timedelta(days=1)
print(dt2)
# 上一个小时
dt3 = dt + timedelta(hours=-1)
print(dt3)
# 下一个小时
dt4 = dt + timedelta(hours=1)
print(dt4)
# 上一秒
dt5 = dt + timedelta(seconds=-1)
print(dt5)
# 下一秒
dt6 = dt + timedelta(seconds=1)
print(dt6)