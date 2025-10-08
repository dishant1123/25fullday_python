# built module  :  random,math cmath datetime time delta calender

import random as r 

import  math  as m 

"""print(m.sqrt(4))
print(m.factorial(5))
print(m.pi)
print(m.floor(4.5))
print(m.ceil(4.22))
print(m.e)

print(m.pow(2,3))
"""

# random  : 

# print(r.random())  # 0 -1 ==> float 
# print(r.randrange(1,10,2))  # last value is not included

# print(r.randint(1,5)) # both value included

# print(r.choice([1,2,3,4,5,"aarav","prathan"])) # random choice
# print(r.choices([1,2,3,4,5,"aarav","prathan"],k=3)) # random choice

"""l1=[1,2,3,4,5,"aarav","prathan"]
print(l1)
r.shuffle(l1)
print(l1)
"""

# game : 
"""
1. rock 2. paper 3. scissor

user  vs  computer   ==> loop  :  10 

user  choice : randint (1,3)  or  randrange(1,4) 
computer  choice : randint (1,3)  or  randrange(1,4)

combination  : 

if u ==1 and c==1   ==>  match  tie  ==>  user score computer ==> no changes 
    print("tie")
elif u==1 and c==3 or u==3 and c==2  or u==2  and c==1 
    print("user wins")
    user_score +=1
else :
    print("computer wins")
    computer_score +=1

user 
computer 

"""
