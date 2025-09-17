# lambda function  : one liner function  
"""
syntax : 

lambda arg : expression 
""" 

"""
def add(x,y):
    return x+y
print(add(2,3)) 
"""
"""
x =lambda a,b : a+b 
print(x(45,45))
"""

# built in function  :  len min max sorted sum 

"""
x = lambda a : sorted(a)
print(x((1,2,3,4,5)))
"""
"""def add(x,y):
    return x+y
print(add([1,2,3,4],[5,6,7,8])) 
"""

# task  :1 
"""
input  : using  function sorted 2 value. ==> def 

l1= [[1,5], [0,2], [3,4]]
output  : [[0,2], [3,4],[1,5]]
"""

"""
def sorted_matrix(l1):
    for i in range(len(l1)):
        for j in range(i+1,len(l1)) :
            if l1[i][1] > l1[j][1]:
                l1[i],l1[j]=l1[j],l1[i]
    return l1 

l1= [[1,5], [0,2], [3,4]]
result = sorted_matrix(l1)
print(result)
"""
"""l1= [[1,5], [0,2], [3,4]]
result = sorted(l1,key=lambda x :x[1])
print(result)
"""
"""
def d1(l1):
    return l1[0]

l1= [[1,5], [0,2], [3,4]]
result= sorted(l1,key=d1)
print(result)
"""

"""
task  :2 
Write a Python program to sort a list of tuples using Lambda.

Original list of tuples:
[('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
Sorting the List of Tuples:
[('Social sciences', 82), ('English', 88), ('Science', 90), ('Maths', 97)]

"""
# map , filter  : 

l1=[1,2,3,4,5,6,7,8,9,10]

"""
even=[]
odd=[] 
for i in l1: 
    if i % 2==0:
        even.append(i)
    else :
        odd.append(i)
print(even)
print(odd)
"""

"""a =tuple(filter(lambda x : x % 2 ==0,l1))
b =list(filter(lambda x : x % 2 ==1,l1))

print(a)
print(b)
"""
# task  :3 
"""
input  : ["php","java","c","python","maam"]
output : ["php","maam"]
"""
#map : new list 

"""
l1=[12,2,3,45,5,6,7,8,9]

a =list(map(lambda x :x **2 ,l1)) 
print(a)
"""