# lambda function  : one  line function  

"""
syntax : 

lambda arg : expression 
""" 

"""
def add(a,b):
    c =a+b
    return c 
print(add(1,3))
"""
"""x = lambda a,b : a+b 
print(x(12,67))
"""
# built in function  :  len  min max sorted sum 
"""
a = lambda x : sorted(x)
print(a([1,2,3,4,5,6]))

"""

# conditional  statement  using lambda

"""
def big(a,b):
    if a>b :
        print("a is bigger")
    else :
        print("b is bigger")
big(12,45)
"""
"""x =lambda a,b : ("a is big") if a>b else ("b is big") 
print(x(12,45))
"""

# list : 

l1=[[-1,2,3], [0,1,89] , [-4,5,67]]

# normal function  : 
# ans : [[0,1],[1,2],[4,5]]
"""
index 0 = [1,2]  ==> 1 index 0 2 index 1 
index 1 = [0,1]  ==> 0 index 0 1 index 1
index 2 = [4,5]  ==> 4 index 0 5 index 1
"""

"""def sorted_func(l1):
    return l1[0] 

l1.sort(key = sorted_func)  # key ==> built in function ==> len min max  sorted , function
print(l1)

"""

"""for i  in l1:
    print(i)
"""    
"""l1.sort(key=lambda x : x[1])  # lambda function
print(l1)
"""    
    
"""

1 2 3 
4 5 6 
7 8 9 
"""    

# filter  map  : 
"""
filter  : 
jan dec  ==> fin  ==> trasc  1 june  30 june   
"""
l1=[1,2,3,4,5,6,7,8,9]
"""even=[]
odd =[]
for i in l1 :
    if i % 2 ==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)"""

"""
a =tuple(filter(lambda x : x%2 ==0,l1))
b =list(filter(lambda x : x%2 ==1,l1))

print(a)
print(b)
"""
# datatype(filter (lambda condition,l1))


# map  : 

l2=[2,4,8,34,6]

# 4 8 68  12 

a =tuple(map(lambda x : x *2,l2))
print(a)
