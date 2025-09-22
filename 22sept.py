#date time  : 
import  datetime  as dt 

"""a= dt.datetime.now()
print(a)
"""
# b=dt.datetime.strftime(a,"%A %d -%m- %Y %H : %M : %S  %f .%p %w")
# print(b)

"""x= dt.datetime.today()
print(x)
"""

"""
y =dt.datetime(2025,9,22,14,28,30,12344)
print(y)
print(type(y))

print(y.date())
print(y.day)
print(y.month)
print(y.year)
print(y.hour)
print(y.minute)
print(y.second)
print(y.microsecond)
"""

import  time as  t 

"""# print(t.time())
print(t.ctime())
print(t.localtime())
# print(t.altzone())

print(t.asctime())
"""
"""
for i in range(10):
    t.sleep(1)
    print(i)
"""

from datetime import timedelta as td 

"""
current_date  = dt.datetime.now()
future_date = current_date +td(days =180)

print(current_date)
print(future_date)
"""

# diff : 

"""current_date =  dt.datetime.now()  # aaj ki date 
custom_date = dt.datetime(2026,6,22)

diff = custom_date -current_date
print(diff)
"""

"""
days = int(input("enter the days : "))
months = int(input("enter the months : "))
years = int(input("enter the years : "))

x = dt.datetime(years,months,days)
print(x)
"""

# birth date  ==>  age  calculate   