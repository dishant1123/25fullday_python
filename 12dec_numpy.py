import numpy as np 

# statistical method 

# a= np.array([
#     [2,3,9],
#     [2,-3,5]
# ])

"""
a=np.array([2,3,9,2,-3,5]) 

print(np.mean(a))
print(np.median(a))
print(np.std(a))  # standard deviation
print(np.var(a))  # variance
"""

a= np.array([
    [1,3,-9],
    [27,-3,-5]
])

# print(np.max(a,axis=None))
# print(np.max(a,axis=0))
# print(np.max(a,axis=1))  om 

# print(np.argmax(a,axis=None))  # saumya
# print(np.argmax(a,axis=0))
# print(np.argmax(a,axis=1))  vidhi 

print(np.argmin(a,axis=None))  # 3    3      3  
print(np.argmin(a,axis=0))   # 0 1 2  0 1 1  0 1 1  # rd  
print(np.argmin(a,axis=1))   # 0 1    1 0 0  0 0 2    harshil 

print(np.argsort(a,axis=None))#
print(np.argsort(a,axis=0))  #
print(np.argsort(a,axis=1))  # purva




