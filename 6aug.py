"""
loops in python : 

1. for loop 
2. while loop
3. while True
"""

"""
c : loop syntax : 
1-100

for(start; con ; inc/dec)


python  : 

for  (variable name) in range(start,stop,step):
    statement/print
"""

#1-100 : 

"""for x in range(1,101):
    print(x,end=" ")
"""

# 100-1: 

"""for  i in range(100,0,-1):
    print(i,end=" ")
"""    

"""
for  y in range(1,100,2):
    print(y,end=" ")
"""

# 100 - 0  ==> print even : 

# user input  : 
"""
n=int(input("enter the number : "))

for i in range(1,n+1):
    print(i,end=" ")
"""

# break continue pass : 

"""
for i in range(1,10):
    if i==5 :
        break
    print(i,end=" ")
"""
# continue : 
"""for i in range(1,10):
    if i==5 :
        continue
    print(i,end=" ")
"""

#pass : 
"""
for i in range(1,10):
    if i==5 :
        pass
    print(i,end=" ")
"""

# prime  : 
"""
prime  : 2  factors : 1, num it self 
"""
n=int(input("enter the number : "))
count=0
for i in range(1,n+1):
    if n % i==0: 
        count+=1
if count ==2 :
    print(n,"is prime")
else :
    print(n,"is not prime")

# perfect number  : 
"""
6 factors  : 1,2,3,6 
sum = 1+2+3 =6  perfect 

28 factors : 1,2,4,7,14,28
sum = 1+2+4+7+14 =28 perfect 

100 factors : 1,2,4,5,10,20,25,50,100
sum = 1+2+4+5+10+20+25+50 = 117 not perfect  
"""
