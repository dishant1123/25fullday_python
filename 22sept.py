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

"""x = 2
for i in range(x):  # 0 1    == >stat  stop  step 
    x += 2   # x -=2   # x = 0 -2  
    print (x)  # 0 
"""

"""n=10 
for i in range(n):
    print(i)
"""

"""var = 10      # 10 
for i in range(5): # 0 ,5   == > 4      
    for j in range(2, 3, 1):  # 2 ,3 
        if var%2 == 0:    # 15 % 2 ==0
              break
        var += 1   # var =18   
    var+=1   # var =19    
else:
     var+=1    # var =20 
print(var)
# saumya   harshil 21 purva 22 vidhi 11  remo 20   het 10  shalin 11
"""

"""A=0
for i in range(4):  # 3  ,4 
    if i%2==0:   #  3 % 2==0 
        pass 
    else:
        continue
        break
    A+=1  # 2 
print(A)"""
# saumya 9  harshil 2  purva 2  vidhi 5   remo 2   het 2   shalin 2 

"""
count = 0
while(True):
   if count % 3 == 0:
       print(count, end = " ")
   if(count > 15):
       break
   count += 1
"""

"""for num in range(26, 30):# 26 27  28 29 
      for i in range(2, num):  # 2 ,  29   
            if num%i == 1:      #   if 29 % 2 ==1 
                print(num, end=",") # 26 27 28  29   
                break
"""

"""
var = 10
for i in range(10):
    for j in range(2, 10, 1):
        if var % 2 == 0:
            var += 1
            continue
    var+=1
else:
    var+=1
print(var)
"""