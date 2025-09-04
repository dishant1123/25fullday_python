# loops in pyhton ; 
"""
1.for 
2.while  
3.while true  
"""

# for loop  : 
"""
syntax : 

for  (variable name) in range(start , stop  , step):
    statement/print
"""

#1-100 : 

"""
for i in range(1,101):
    print(i,end=" ")
"""

# 100 -1 : 
"""
for x in range(100,0,-1):
    print(x,end=" ")
"""

# for i in range(1,101,2):
#     print(i,end=" ")

"""
for i in range(0,101,2):
    print(i,end=" ")
"""

"""n=int(input("enter the  number  : "))

for i in range(1,n+1):
    print(i,end=" ")

"""    

# start  and end : 

"""
start = int(input("enter the start : "))
end = int(input("enter the end : "))

for i in range(start,end+1):
    print(i,end=" ")
"""

# prime  number  :  
"""
2 factors : 1 , num it self 

6 = 1,2,3,6  not prime 
5 = 1,5 ==> prime 

"""

"""n=int(input("enter the number : "))
count =0

for i in range(1,n+1):
    if n % i==0 : 
        count+=1
if count ==2 :
    print(n,"is prime")
else :
    print(n,"is not prime")
"""

# break continue pass :

"""
for i in range(1,10):
    if i==5:
        break
    print(i,end=" ")
"""

"""
for i in range(1,10):
    if i==5:
        continue
    print(i,end=" ")
"""

"""
for i in range(1,10):
    if i==5:
        pass
    print(i,end=" ")
"""


"""
username ="harshil"
password =123 

for i in range(3):
    username = input("enter the username : ")
    password = int(input("enter the password : "))

    if username == "harshil" and password == 123 :
        print("welcome harshil")
        break
    else :
        print("invalid username or password")
"""
# armstrong  number  : 
"""
153 : digit : 3 

1**3  5 **3  3**3 
1     125     27 
sum = 1+125 +27 =153   amg 

1634 :

3  step  : 
digit =4
r = num % 10  // 1 %  10 =1 
sum = sum + pow(r,digit)  // sum =1634
num = num // 10   //num =  1 //10 =0

"""

# built in function  :  len min max  sorted  sum  .... 

# s1=123
# print(s1)
# s2=str(s1)
# print(type(s2))
# print(len(s2))

"""
num =int(input("enter the  number : "))
digits =len(str(num))
sum =0 
temp =num 
for i in range(digits):
    r = temp %10 
    sum =sum + pow(r,digits)
    temp = temp //10 

if sum == num : 
    print(num,"is armstrong number")
else :
    print(num,"is not armstrong number")
"""

#twin  : 
"""
number  =123 

sum = 1+2+3 =6 
mul = 1*2*3 =6 


"""

# strong  number  : 
"""

145 : 
1 != 1 
4! = 24 
5! =120 

sum =120 +24 +1 =145 
"""
