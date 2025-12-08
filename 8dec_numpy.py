# numpy  ==> array  , list  manupulation  
"""
1.matrix
2.picture manupulation   
"""

# creating a array  : 

import numpy as np 

"""
a=np.array([1,2,3,4,5,6,"purva",8j,True,23.78])
print(a)
print(type(a))
"""
"""
b=np.array([1,2,3,4,5,6,12.56],dtype="float64")
print(b)
"""

"""
l1=[1,2,3,4,5,6]
c=np.array(l1)
print(c)
"""

"""d=np.array([[1,2],
            [3,4],
            [5,6]],dtype="int64")
print(d)
print(d.ndim)  # number of dimensions
print(d.shape)  # shape  of array  how  many row and  col in array . 
"""

"""e=np.array([[1,2,3],
           [5,6]])
print(e)  # error : array has an inhomogeneous shape after 1 dimensions.
"""

# slicing  : 

"""a=np.array([12,13,14,15,16,19,70,56])

# update in array :
a[1] =100
print(a)

print(a)
print(a[3])
print(a[3:5])
print(a[2: 6 :2])

"""

# 2d array slicing  : 

a=np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30]
],dtype="int64")
print(a)

# print(a[0])
print(a[1:2])
print(a[1:3])
#       r  , c
print(a[1:3,1:3])
print(a[1:4:2,0:3])
print(a[2,::2])
print(a[1,::-1]) 

# task  :1  
"""
output  : [[13,14], 
            [19,20]]
"""

# task  :2 
"""
output  : [[2,9,16,23,30]]
"""

