# date time  ,  date  , time  , time delta , calender : 

import datetime as dt 

"""a= dt.datetime.now()
b= dt.datetime.today()
print(a)
print(b)
"""

"""a= dt.datetime(2025,10,10,13,22,56,456789)
print(a)
print(a.day)
print(a.month)
print(a.year)
print(a.hour)
print(a.minute)
print(a.second)
"""
# 10/ 10 /2025  13 :22 :56 

"""a= dt.datetime(2025,10,10,13,22,56,456789).strftime("%d/%m/%Y %H:%M:%S")  # 
print(a)

b=dt.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
print(b)
"""

import  time as t 

"""print(t.ctime())   # var mon day  hr:min:sec  year 

print(t.localtime())

print(t.time())#epoch==> 1760083265
"""
"""
for i in range(5):
    t.sleep(1)
    print(i)
"""    

from  datetime import timedelta as td 

"""
today =dt.datetime.now()
future_date = today + td(days =243)
print(future_date)  # 283 

"""

import calendar as cal

a= cal.calendar(2025)
print(a)