# matrix : 
"""
l1 = [1,2,3,4,5,6,7]  ==> one  dementional  array

l2 =[[1,2], [3,4] ,[4,5]]   ===> 2  d array  ==> matrix 
"""

# l1=[[1,2,3],   # row ==>1,2,3  ==>1 index 0 2 index 1 3 index 2 
#     [4,5,6],
#     [7,8,9]]

"""
matrix components : 

(0,0) ==>1 (0,1)==>2 (0,2)==>3
(1,0)==>4 (1,1)==>5 (1,2)==>6
(2,0)==>7 (2,1)==>8 (2,2)==>9
"""
"""
print(l1)
for i in l1:
    print(i)
"""
#slicing  : 

"""
l1=[[1,2,3,10],   # row ==>1,2,3  ==>1 index 0 2 index 1 3 index 2 
    [4,5,6,11],
    [7,8,9,12]]
"""
"""
print(l1[0])
#        r  c 
print(l1[0][2])
print(l1[1][1])
print(l1[0][0 : 2])
print(l1[2][1 : 2])
"""
"""print(l1[2][ 0: 3 :2])
print(l1[1][ 1: 3 :1])
print(l1[0][ :  :-2])
"""
# print(l1[1:3][1:3])


# dict : mutable ==> changes in dict ==> key value pair 

d1={"phy" :90 , "math" :89}

# phy  ==> key value ==> 90  math ==> key  value ==>89
"""
print(d1)
print(type(d1)) 
"""

"""d2 ={False: 89 , "math" :90}
print(d2)
print(type(d2))
"""
"""d3 ={89 :False ,90 :"math"}
print(d3)
print(type(d3))
"""
# built in function :  len  min max sorted 

"""
d1={"maths" :90 , "phy" :89}

print(len(d1))
print(min(d1))
print(max(d1))
print(sorted(d1))
"""

#add in dict :  
"""
d1={"maths" :90 , "phy" :89}
d1["com"]=100
d1["maths"] =89 
print(d1)
"""

# method : 
# d1={"maths" :90 , "phy" :89}

"""d1.clear()
print(d1)
"""
"""d2 =d1.copy()
print(d2)

print(d1.keys())
print(d1.values())
print(d1.items())

for i in d1.keys():
    print(i)
"""
l1=["aarav","harshil"]
#output : {"aarav" :100,"harshil":100}

"""x =dict.fromkeys(l1,100)
print(x)
x["harshil"]=150
print(x)
"""

"""d2= {"com" :90}
d1.update(d2)
print(d1)
"""
d1={"maths" :90 , "phy" :89}

# print(d1.get("s.s"))
"""
d1.setdefault("s.s",100)
print(d1)
"""

"""
task :1 

ask user to enter the  5 students name  and  marks  ans store in to the dict. 

ketan 90  aarav 89  harshil 88  shalin 99 purva 98 
output : {"ketan" :90 , "aarav" :89 , "harshil" :88 , "shalin" :99 , "purva" :98}

task  :2 
values  sort :
{"harshil" :88 ,"aarav" :89,"ketan" :90 , "purva" :98 , "shalin" :99}

task :3 

ask user to enter the string  and store  in to the dict . 

input  :"mississiappi" 
output :{"m" :1 ,"i" :4,"s" :4 ,"p" :2, "a" :1}

"""
"""d1={}
for i  in range(3): 
    name =input("enter the name " )
    marks =int(input("enter the marks : "))
    d1[name]=marks
print(d1)

sorted_marks = sorted(d1.values())
print(sorted_marks)

d2={}
for i in sorted_marks:  #[55, 56, 90]
    for name  , marks in d1.items(): # {'t': 90, 'q': 56, 'j': 55}
        if marks ==i :  
            d2[name]=marks 
print(d2)
"""