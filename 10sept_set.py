# string , tuple  ==> immutable  dict , list ==> mutable 

#set :mutable  no repeation allowed in set, unordered. 

"""
s1={1,2,3,4,5,6,"harshil",9j,8.90,2} 
print(s1)
"""
# built  in function  :   len  min max sorted sum 

"""
s1={1,2,3,4,5,6,90,90,11,8.90,2}
print(len(s1)) 
print(min(s1)) 
print(max(s1)) 
print(sum(s1))
print(sorted(s1))   # asc to desc 
"""

# task  :1 
"""
remove the duplicate element  from the  set  and print  in to the  list.
input  : s1 ={1,2,3,4,5,6,90,90,11,8.90,2}
output : s1 =[1,2,3,4,5,6,8.90,90,11]
""" 
# declare empty set : 

"""s2=set()
print(s2)
print(type(s2))
"""
# method : 

s1 ={1,2,3,4,5,6,90,90,11,8.90,2}

"""s1.add(900)
print(s1)

s1.add(2)
print(s1)
"""
"""s1.clear()
print(s1)
"""
"""s2=s1.copy()
print(s2)
"""

# set theory :
"""s1={1,2,3,4,5,6}
s2={3,4,5,7}
s3={1,2,3,4,5,6,7,8,9}
"""
"""
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))  # s1-s2 
"""
"""
print(s1.difference(s2))  # s1-s2 
print(s1.symmetric_difference(s2))
"""

"""print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)
"""
"""
s1.symmetric_difference_update(s2)
print(s1)
s1.difference_update(s2)
print(s1)
"""

"""s1={1,2,3,4,5,6}
s2={1,2,3}
s3={1,2,3,4,5,6,7,8,9}
"""
# print(s1.isdisjoint(s2))
# print(s2.issubset(s1))
# print(s3.issuperset(s1))

s1 ={900,13,3,4,5,6,90,90,11,8.90}

# discard ,remove,  pop , update : 

"""
s1.remove(900)  # specific element 
print(s1)

s1.discard(900)
print(s1)
"""
"""
s1.pop()
print(s1)

s1.pop()
print(s1)
"""

"""s2= {"apple"}
s1.update(s2)
print(s1)
"""

# frozen set : immutable , no changes in frozenset .

"""
fz =frozenset({1,2,3,4,5,6,900,90,11,8.90,2})
print(fz)
"""

# function  : 
"""
4 type  : 

1. no arg no return  
2. no arg  with return  
3. with arg no return 
4. with arg with return 
"""

#1. no arg no return  :  

"""
def d():
    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))
    c=a+b
    print(c)
d()
"""
# 2 : with arg  no return  
"""
def d(a,b):
    c=a+b
    print(c)
a=89
b=67
d(a,b)
"""
# 3. no arg  with return  : 
"""def d():
    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))
    c=a+b
    return c 
print(d())
"""
#4.with arg with return : 
"""def d(a,b):
    c=a+b
    return c 
print(d(12,90.89))

"""

# local variable , global variable : 

"""def x():
    a=10     # local variable  ==> with in function access 
    print(a) 
x()
# print(a)   not accessible  bcz of local 
"""

# global variable :
"""
y=0
x=100 
def a():
    global x
    global y 
    x=y 
    # print(x)
    print(y)
a()
# print(x)
print("harshil")
print(y)
"""

"""from mypackage import calculator as c ,saumya

print(c.sum(12,13))
print(c.mul(12,14))

saumya.s()

"""
