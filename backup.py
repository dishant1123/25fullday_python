'''print("hello")  # string : 

print("aarav")
print("harshil")
print("crickter")
print("om")
'''
# comment : 
"""
1. single  line comment: # 
2. multi line comment  :"""  """   or ''' ''' 
"""

# python  comma create space in python  : 

# print("aarav  shah""live  in ahmedabad")

"""
escape squence character : 

1.\n  : new line  
2.\t : tab 
3. \b : backspace 
4 . end=  : remove the white space after the end of the string
"""
# naimish patel 
"""print("naimish",end="\b\b")
print("patel")

"""

# data type in python  : 
"""
1. int  :  pos   or  neg value  ==> no  limit   
2 . float: decimal value 
3. chr /string  :  a  to z , name  , special character,number 
4.bool :  true or false
5.complex number :  real part  ,imaginary part

"""
# variable declaration rules :

"""a=10 
print(a)
print("a=",a)
print(type(a))

b=1234567823456782345678456784567856789
print(b)
print("b=",b)
print(type(b))

c=12.34 
print(c)
print("c=",c)
print(type(c))

d=12345678.123456783456789
print(d)
print("d=",d)
print(type(d))

e="w123"
print(e)
print("e=",e)
print(type(e))
"""

"""g =12 +5j
h=13+56j
# real part :  12 imaginary part : 5j
print(g)
print(type(g))
print(g+h)
"""

# user input string  : 

"""a=str(input("enter the name  : "))
b=input("enter the sur-name  : ")
print(a)
print(b)
print(a+b)   # "123"
"""

#user  input  number  :

"""
a=int(input("enter the number 1 : "))
b=int(input("enter the number 1 : "))
print(a)
print(b)
print(a+b) 
"""

"""a=float(input("enter the number 1 : "))
b=float(input("enter the number 1 : "))
print(a)
print(b)
print(a+b) 
"""

"""
task :1 
ask user to enter the 2 interger type number and  concate them. 
note : no converted in to the string. 
input a =10 
input b =20
output  :1020 

"""
"""
a=int(input("enter the number 1 : "))
b=int(input("enter the number 1 : "))
print(a,end="")
print(b)
"""

# operator : 
"""
1.airthematic : + - * / % //
2.comparsion : < > <= >= == != 
3.logic :  and or 
4.assignment : +=, -=, *=, /=, %=, //=
5.membership : in ,not in
"""

a=1
b=10 
# c=a+b
# print(c)
# print(a/b)  # division  : 3.3333333
# print(a//b)  # floor  division   :  
# print(a!=b)   
# print(a>b or a!=b)

# a=a+b
# a+=b
# print(a)

"""
l1=[1,2,3,4,5,"ketan"]

print(5 in l1)
print(7 not in l1)
"""
#conditional  statement :
"""
if condition:
    statement/print
else:
    statement/print
"""

# a=int(input("enter the  number : "))
# b=int(input("enter the  number : "))

"""if a>b:
    print("a is big")
else:
    print("b is big")
"""
"""
if a>b :
    print("a is big")
if b>a :
    print("b is big")
"""

"""
ladder : 

if con :
    print
elif con :
    print
else :
    print
"""

# a=int(input("enter the  number : "))
# b=int(input("enter the  number : "))
# c=int(input("enter the  number : "))

"""
if a>b and  a>c :
    print("a is big")
elif b>a and b>c :
    print("b is big")
elif c>a and c>b:
    print("c is big")
else :
    print("same")
"""

# netsed : 
"""
if con :
    if con :
        statement
    else :
        statement
elif con :
    if con :
        statement
    else:
        statement
else :
    statements
"""

"""a=int(input("enter the  number : "))
b=int(input("enter the  number : "))
c=int(input("enter the  number : "))

if a>b :
    if a>c :
        print("a is big")
    else:
        print("c is big")
elif b>a :
    if b>c :
        print("b is big")
    else:
        print("c is big")
else :
      print("same")
"""      

"""
task  :2  

ask user to enter the three number  and  check which number is small medium or large.
a=10 b=34 c =7    small  c   big b  10 medium 


task :3 
ask user to enter the character and convert into lowercase or uppercase and vice versa.
hint  :  ascci value 

A  =65   a 97  diff =32    
input  : a   output  :A    

if ch >='A'  and ch <='Z'
ch =ch +32   ch =ch -32 
"""
# ord :  convert ascii value to character
ch=input("enter the character : ")

if ch >='A'  and ch <='Z':
    ch =ord(ch) +32 
    print("lower case :",chr(ch)) 
else :
    ch =ord(ch) -32
    print("upper case :",chr(ch))


