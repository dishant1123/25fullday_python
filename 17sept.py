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
