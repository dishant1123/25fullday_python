import  numpy as np 

# intrinsic method : 

"""a=np.arange(10)   # last value is not included
print(a)

b=np.arange(1,10,2)   # last value is not included
print(b)

c=np.arange(1,21).reshape(4,5)
print(c)

d=np.zeros(10,dtype="int64").reshape(2,5)
print(d)

e=np.ones(9,dtype="int64").reshape(3,3)
print(e)

f=np.full((3,4),fill_value=100)
print(f)

g=np.array([
    [1,2,3,4,5,6],
    [7,8,9,10,11,12],
    [13,14,15,16,17,18],
    [19,20,21,22,23,24],
    [25,26,27,28,29,30]
],dtype="int64")

h=np.full_like(g,fill_value=23)
print(h)
"""

# random  module  : 
"""import random 

a= np.random.random(10)  # 0-1 float 
print(a)

b=np.random.randint(low=-10,high=10,size=12).reshape(3,4)
print(b)

c=np.random.sample(10) 
print(c)

d= np.random.randint(low=0,high=20,size=(3,3))
print(d)
"""

# line space : 
"""
end -start / number of points
"""
a=np.linspace(0,9.5,20)  # 9.5-0 /20  
print(a)

"""
task  :1 
[
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1],
[1,1,1,1,1]]

output  :
[
[1,1,1,1,1],
[1,0,0,0,1],
[1,0,9,0,1],
[1,0,0,0,1],
[1,1,1,1,1]]

"""
