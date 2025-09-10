#tuple  : immutable  not  changes in tuple  .

"""
t1=(1,2,3,4,5,6,7,8,"aarav",8j,90.89)
print(t1)
print(type(t1)) 
"""
"""
t2 = 1,2,3,4,5,6,7,8
print(t2)
print(type(t2))
"""

# built in function  :  len  min max  sorted sum 

"""
t1=(1,2,3,80,45,8,9)

print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))  # asc to desc 
print(sum(t1))
"""

# slicing : 
t1=(1,2,3,80,45,8,9)
# pos  index :  l to   r   : 0 1 2 3 ... 
# neg index  :  r ot  l  : -1 -2 
"""print(t1[4])
print(t1[6])
print(t1[2:4])   #  2 start index  4 ending  index

print(t1[ :6])
print(t1[1 :])
print(t1[ : ])

print(t1[-3])

print(t1[2 : 5 :2])   #  2 start index  5 ending  index  2 step
print(t1[1 : 5 :2])   #  1 start index  5 ending  index  2 step
print(t1[ :  :2])   #   start index   ending  index  2 step
print(t1[ :  :-2])   #   start index   ending  index  -2 step
print(t1[ :  :-1])   #   start index   ending  index  -1 step
"""

# method : 
"""
t1=(1,1,2,3,80,45,8,9,1)

print(t1.count(1))
print(t1.index(1))
print(t1.index(1,2,10))  # 1  ==> 2 indexnumber  10 indexnumber 
"""

# not changes in tuple  :  
"""
l1=(1,2,3,4,54)
l1[2] ="saumya"  # immutable  
print(l1)
"""

# task  : 1  hint  convert  list : 
"""
input  : l1=(1,2,3,4,54)
output  : l1=(1,2,3,4,54,"vishal")
"""

"""l1=(1,2,3,4,54)
l2 =list(l1)
print(l2)
l2.append("vishal")
print(tuple(l2))
"""

# mcq : 

"""
1. what is  output  ? 

t1 =(1,2,3,[6,7,8],10)
t1[3].append("aarav")
print(t1)

a.error   # a 
b.(1,2,3,[6,7,8],"aarav",10)
c.not  changes in tuple 
d.(1,2,3,[6,7,8,"aarav"],10)    # s==>a c   v ==>c d  v =>d  d ==>d 
"""

# dict : mutable  changes in dict ==>  key value  pair 

"""
d1 ={"phy":90 ,"math":80 ,"chemistry":70}

# phy ==> key  value  90  math  key  value  80  che key value  70 

print(d1)
print(type(d1))
"""
"""d2={90 :34 ,89 :67 }
print(d2)
print(type(d2))

d3={90 :"phy" ,"math" :99}
print(d3)
print(type(d3))
"""
# built in function  :  len  min max  sorted sum

# d1 ={"phy":90,"math":80,"chemistry":70}
"""d1={90 :"phy" ,89 :99}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

# ADD : 
"""
d1 ={"phy":90,"math":80,"chemistry":70}

d1["eng"]=89
d1["phy"]=67
print(d1)
"""

# method  : 

d1 ={"phy":90,"math":80,"chemistry":70}

"""
print(d1.keys())
print(d1.values())
print(d1.items())
"""
"""d2={"ss":90}
d1.update(d2)
print(d1)
"""

# print(d1.get("phy"))

"""
l1=["aarav","harshil"] 
# {"aarav":100,"harshil":100}
d2 =dict.fromkeys(l1,100)
print(d2)
d2["aarav"]=200
print(d2)
"""

"""l1=["aarav","harshil"] 

for i in range(3):
    d2 =dict.fromkeys(l1,100+i)
print(d2)
"""

"""d2=d1.copy()
print(d2)

d1.clear()
print(d1)
"""
d1 ={"phy":90,"math":80,"chemistry":70}

"""d1.pop("math")  # key 
print(d1)
"""

# d1.popitem()   # last key value  pair 
# print(d1)

# d1.setdefault("ss",100)
# print(d1)

"""
task  :1 

ask user to enter the name and  marks  store in dict .
3  raj   simran  jivan   100  200 300 
d1={"raj":100,"simran":500,"jivan":300}

sorted above  dict using marks . 
d1={"raj":100,"jivan":300,"simran":500,

"""
"""d1={}
for i in range(3):
    name =input("enter the name  : ")
    marks=int(input("enter the marks : "))
    d1[name]=marks
print(d1)  # {'meet': 95, 'vidhi': 90, 'saumya': 67}

sorted_marks = sorted(d1.values())
print(sorted_marks)  #[67, 90, 95]
d2={}
for  j in sorted_marks: #[67, 90, 95]
    for name,marks in d1.items(): #{'meet': 95, 'vidhi': 90, 'saumya': 67} 
        if marks==j:
            d2[name]=j
print(d2)
"""

# task  : 2 
"""
ask user to enter the string  and  count  letter  and  store  in to the dict. 

input  : dishaant 
output d1={"d":1,"i":1,"s":1,"h":1,"a":2,"n":1,"t":1}
"""