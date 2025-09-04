# operator  : 
"""
1. airthematic  operator  : + - * / % // * 
2.comaprison  operator  : ==  !=  >  <  >=  <=   ==> bool 
3.logical  operator  : and or not
4.relational  operator  : in  not in
5.assignment  operator  :  =  +=  -=  *=  /=  %=  //=  **=  //=
""" 

# print(10/3)   #
# print(10//3)  # floor division

# a=10   
# b=110 
# print(a!=b)

# print(a>b and a!=b) 
# print(a==b or a>b) 

# l1=[1,2,3,4,5]
# print(3  not in l1)

# a=10
# b=2

# a**=b 
#a+=b   a-=b  a*=b  a/=b  a%=b  a//=b  a**=b
# print(a)

# conditional statement : 
"""
if else : 

syntax : 

if con : 
    statement/print 
else : 
    statement/print

"""
"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b :
    print("a is big")
else :
    print("b is big")
"""

"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))

if a>b :
    print("a is big")
if b>a :
    print("b is big")
else :
    print("both are equal")
"""

#ladder if : 
"""
if con :
    statement/print
elif con:
    statement/print
else :
    statement/print
"""  

"""
a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b and a>c :
    print("a is big")
elif b>a and b>c :
    print("b is big")
elif c>a and c>b :
    print("c is big")
else :
    print("same")
"""

# nested if : 
"""
if con :
    if con :
        print()
    else :
        print()
"""
"""a=int(input("enter the  number  : "))
b=int(input("enter the  number  : "))
c=int(input("enter the  number  : "))

if a>b:
    if a>c :
        print("a is big")
    else :
        print("c is big")
elif b>a :
    if b>c :
        print("b is big")
    else :
        print("c is big")
else :
    print("same")
"""
"""
task  : 1  

ask  user to enter the  number  and  check  number  is div by  5 or 11 or both . 
input  :55   ==> num is  div by  both 5 and 11   22  25   

task  2 : ask user to enter the character is convert to upper case or lower case and  
vice versa .
hint  : ascci table      A =65  a =97 diff ==>32 
input : a   output  =A
input  :B   ouput  ==b 

"""
# task :1 
"""num =int(input("enter the number  : "))

if num  % 5==0 and num % 11 ==0 :
    print("num is div by  5 and 11 ")
elif num % 5 ==0 :
    print("num is div by  5")
elif num % 11 ==0 :
    print("num is div by  11")
else :
    print("num is not div by  5 and 11")
"""
# 2 :     
# ord : char to ascci

"""ch = input("enter the char : ")  # R 
if ch >='A' and ch <='Z':
    ch =ord(ch) +32
    print("lower : ",chr(ch)) 
else :
    ch =ord(ch) -32
    print("upper : ",chr(ch))
"""
"""
Write a python  program to input electricity unit charges and calculate total electricity bill according to the given condition:

For first 50 units Rs. 0.50/unit
For next 100 units Rs. 0.75/unit
For next 100 units Rs. 1.20/unit
For unit above 250 Rs. 1.50/unit
An additional surcharge of 20% is added to the bill

"""

"""
units range    price 
0-50           0.50 
51-150         0.75
151-250        1.20
251 above      1.50

units =25   if units >50 :

bill = units *0.50  =25 * .50 =12.5
surchage = bill *.2 =12.5 * .2 =2.5 
total  = bill +surchage =12.5 +2.5 =15

units =125  elif units >=51  and  units <=150 

bill =25+(units -50) * 0.75 =25 +(125 -50)*0.75 = 81.25 
surchage = bill *.2 =81.25 * .2 =16.25
total  = bill +surchage =81.25 +16.25 =97.5
print("total  = ",total)

units =175 
#  ans : 308   
"""

# loop  : 
"""
1. for loop  : 
2. while  loop  : 
3. while True 

HW : is  for  loop  entry  control  loop  or  exit  ? 
"""

"""
c : syntax : 

for(start ;condition ; inc/dec)
{
printf()
    }

python  syntax : 
for var in range(start,stop ,step):
    print(var)
"""

#1-100 : 
"""for i in range(1,101):
    print(i,end=" ")
"""
# 100-1 : 
"""
for  x in range(100,0,-1):
    print(x,end=" ")
"""    

"""for  x in range(1,101,1):
    print(x,end=" ")
"""

"""for  x in range(100,0,-2):
    print(x,end=" ")
"""

# user input  : 
"""n=int(input("enter the  number  : ")) 
for i in range(0,n+1,2):
    print(i,end=" ")
"""
# both  user ; 
"""start =int(input("enter the  start  number  : "))
end =int(input("enter the  stop  number  : "))

for x in range(start,end+1,2):
    print(x,end=" ")
"""

# break : 
"""
for i in range(1,20) :
    if i==6:
        break
    print(i,end=" ")
"""

# contunie : 
"""for i in range(1,20) :
    if i==6:
        continue
    print(i,end=" ")
"""

# pass : 
"""for i in range(1,20) :
    if i==6:
        pass
    print(i,end=" ")
"""

# prime , perfect ,amg , reverse , pelindrome , twin ,strong :
 
n=int(input("enter the number  : "))
count =0 
for i in range(1, n+1):
    if n % i ==0 :
        count +=1 
if count ==2 :
    print("prime")
else :
    print("not prime")
    
# perfect : 
"""
6 factors : 1 2 3 6   
sum = 1+2+3 =6 perfect 
28 factors : 1 2 4 7 14 28 perfect 
100  factors  : 1 2 4 5 10 20 25 50 100  :

"""