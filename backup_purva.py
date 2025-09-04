'''print("hello")
print("purva")
'''
# commment : 

"""
2 type  : 

1. single  line  : # 
2. multi  line  : """ """ or ''' ''' 
"""

# escape sequence character :
"""
1. \n :new line  
2. \t :tab
3. \b :backspace
4. end = remove the  white space  after the character
"""

"""print("purva",end="\b\b")
print("dave")

"""
# comma  create space in python  :
# print("my name is  purva","live in ahmedabad")


# data type  : 
"""
1. int  : pos or neg value  ==> no limit 
2. float : decimal value 
3. str / chr : a to z , name  , special character
4.bool :  true or false 
5. complex number  : 2 part :  1 real   2 imaginary
"""

"""a=10 
print(a)
print(type(a))

b=12345678923456784567856789567856789
print(b)
print(type(b))

c=12.34 
print(c)
print("c=",c)
print(type(c))

d=1234567.23456789456789
print(d)
print("d=",d)
print(type(d))

e ="@purva@"
print(e)
print("e=",e)
print(type(e))
"""
"""g= 23 +9j  
# real part : 23  imaginary part : 9j
print(g)
print(type(g))
h=90 +7j
print(g+h)
"""

# user input  : 

"""a=str(input("enter your name : "))
b=input("enter your sur-name : ")
print(a)
print(b)
print(a+b)
"""

# user input  number  : 

"""
a=int(input("enter the  number  1:"))
b=int(input("enter the  number  2:"))
print(a)
print(b)
print(a+b)
"""

"""a=float(input("enter the  number  1:"))
b=float(input("enter the  number  2:"))
print(a)
print(b)
print(a+b)
"""

# task  :1 
"""
ask user to enter the 2  int  type number   and concate them. 

input  :1 23 
input  :2 45 
output  :2345
"""

# operator  : 
"""
1. airthematic : + - * / % // 
2. comparsion : == != > < >= <=      ==> bool value  ==> True or False
3. logic : and  or 
4. membership : in  not in
5. assignment : +=, -=, *=, /=, %=, //=
"""

# print(10/3)
# print(10//3)
# print(10 % 3)
# a=10 
# b=100
# print(a!=b)
# print(a>b or a!=b)

# l1=[1,2,3,4,5,"ketan"]

# print("ketan" in l1)
# print("ketan" not in l1)


# a= a+b  
# a/=b
# print(a)

# conditional statement : 
"""
if else : 

syntax : 

if con : 
    print
else :
    print
"""

"""
a=int(input("enter the  number  1:"))
b=int(input("enter the  number  2:"))

if a>b :
    print("a is big")
else :
    print("b is big")
"""

# ladder : 

"""
if con : 
    print 
elif con :
     print 
else : 
    print
"""
"""
a=int(input("enter the  number  1:"))
b=int(input("enter the  number  2:"))
c=int(input("enter the  number  3:"))

if a>b and a>c :
    print("a is big")
elif b>a and b>c :
    print("b is big")
elif c>a and c>b :
    print("c is big")
else :
    print("same")
"""

# nested : 
"""a=int(input("enter the  number  1:"))
b=int(input("enter the  number  2:"))
c=int(input("enter the  number  3:"))

if a>b :
    if a>c:
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

#loops in python   : 
"""
1. for loop  : 
2. while  loop : 
3. while true : 
"""

#for : 
"""
syntax : 

for variable name in range(start , stop , step):
    print()
"""

# 1-100 : 

"""
for i in range(1,101):
    print(i,end=" ")
"""
# 100-1 : 

# for x in range(100,0,-1):
#     print(x,end=" ")

# for x in range(1,100,2):
#     print(x,end=" ")

"""for x in range(0,100,2):
    print(x,end=" ")
"""

# prime  , amg twin  strong  perfect : 

#perfect : 
"""
6 factors : 1,2,3,6   sum = 1+2+3 =6 
28 factors :1,2,4,7,14,28 :sum =1+2+4+7+14=28
"""

# twin : 
"""
123 : 

sum =1+2+3 =6 
mul = 1*2*3 =6   sum ==mul  twin 
"""

#strong number : 
"""
145 : 

factorial : 1! = 1  4! = 24 5! =120
sum 1 +120 +24 =145

"""


"""n=int(input("enter the  number  : "))
count =0 

for i in range(1,n+1):
    if n % i==0 :
        count +=1
if count ==2 :
    print("prime") 
"""

# amg : 
"""

153 : 3 digit   

1**3  5 **3  3*** 
1     125    27 
sum = 1+125 +27 =153 

"""

# s1="my name is purva dave."
# s1=15356
# print(len(str(s1)))

"""n=int(input("enter the  number  : "))  #153 
digit = len(str(n))  #3 
sum =0
temp =n    # temp =153 
for i in range(digit):   # 2 , 3  
    r= temp %10            # r=  1 %10 =1 
    sum =sum + pow(r,digit)  # sum =153 
    temp = temp //10     # temp  =0

if sum ==n :  #153 ==153
    print("amg")
"""

n=int(input("enter the  number  : "))  #153
temp =n
count =0 
for _ in range(len(str(n))) : 
    temp = temp //10 
    count +=1
print(count)