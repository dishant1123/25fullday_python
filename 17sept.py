# module : random  , date time  , time delta , calendar,time , math , cmath  

import random as r 

# print(r.random())  # 0-1 float  value  
# print(r.randrange(0,10,2))  # last exclude 
# print(r.randint(1,10))  # both  value include 

# print(r.choice([1,2,3,4,5,"purva"]))
# print(r.choices([1,2,3,4,5,"purva"],k=3))

"""
l1=[1,2,3,4,5]
r.shuffle(l1)
print(l1)
"""

# game  :  rock  paper scissor 
"""
userscore =0  
computerscore = 0 

for loop (10)
user   vs  computer 
choice ==> rock  paper  scissor  computer ==> rock paper scissor
randint  , choice : 

if user ==rock and computer ==rock or :
    draw 
elif user ==rock and computer ==scissor or  user ==scciosor and computer ==paper  :
    usercore +=1 
    print(user win )
else :
    computerscore +=1
    print(computer win )

print(usercore,computerscore)

"""

"""string = "my name is x"
for i in string:
    print (i, end=", ")
"""

# for i in range(10): 
#     if i == 5:
#        break
#     else:
#           print(i)
# else:
#      print("Here")
# 4.Given the nested if-else below, what will be the value x when the code executed successfully
"""x = 0
a = 5
b = 5
if a > 0:
    if b < 0: 
        x = x + 5 
    elif a > 5:
        x = x + 4
    else:
        x = x + 3
else:
    x = x + 2
print(x)

"""
a = [10, 20]
b = a
b = b +[30, 40]
print(a)
print(b)

# i = i +1   i +=1 
"""a={"phy" :90}
b=a
a["che"]=99
print(a)
print(b)
"""

"""i = 0
while i < 5:  #  
    print(i)  # 0 1 2   
    i += 1  #3   
    if i == 3:
        continue
else:
    print(0)"""

"""i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)
"""
"""for i in range(10): 
    if i == 5:
          continue
    else:
          print(i)
else:
     print("Here")
"""
# s = "abcdef"
# print(s[  :  :  2])

s = "Python"
s = s[::-1]   # nohtyp 
print(s[-2])
"""
a. h  b. y c. p d. t
"""

tup = (1, 2, (3, 4, (5, 6)))
#      0  1  2 
print(tup[2][2][1])

"""
a.3,4 
b.5,6 
c.6 
d.none 
"""

# v ==>d  p ==> b p ==>b  s ,s,h,h,b,b ==>b  

"""x = [0] * 3
x[0] = [1]

print(x)
"""
"""a = [1, 2, 3]
b = a
b[0] = 0

print(a)
print(b)
""" 
# 19. What will be the output of the following code? 
"""d = {}
d[1] = 'a'
d[True] = 'b'
print(d)
"""

d = dict.fromkeys(['a', 'b'], [])
d['a'].append(1)
print(d)