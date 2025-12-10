import numpy as np 
import  random 

"""
x=np.random.randint(low=-10,high=10,size=12).reshape(3,4)

print(x)
print(x.shape)
print(x.ndim)
print(x.size)
print(x.itemsize)
print(x.nbytes)

print(x.T)  # transpose

a= np.identity(3)
print(a)
"""

# mathematical method : 
"""
axis =0 col wise 
axis =1 row wise 
"""

"""a=np.random.randint(low=1,high=20,size=12).reshape(3,4)
b=np.random.randint(low=1,high=20,size=12).reshape(3,4)

print(a)
print(a.sum())  # sum of all elements
print(a.sum(axis=0))  #col wise  sum 
print(a.sum(axis=1))  #row wise  sum 

print(a+10)
print(a-10)
print(a*10)
print(a/10)
print(a//10)
print(a%10)
"""

"""
a=np.random.randint(low=1,high=20,size=12).reshape(3,4)
b=np.random.randint(low=1,high=20,size=12).reshape(4,3)

print("a=\n",a)
print("b=\n",b)

print(a+b)  # element wise addition
print(a*b)  # element wise multiply

c= np.matmul(a,b)
print(c)

d=np.sin(a)  # radian
print(d)
"""

# np.where() : 

"""c=np.random.randint(low=-10,high=10,size=10)

print(c)
print(np.where(c>0))

print(np.count_nonzero(c))  # values  ==> count number  of element 
print(np.nonzero(c))  # index number 
"""

# vstack , hstack :

a=np.random.randint(low=1,high=20,size=12).reshape(3,4)
b=np.random.randint(low=1,high=20,size=12).reshape(3,4)

print(a)
print(b)
# print(np.vstack((a,b)))
print(np.hstack((a,b)))
