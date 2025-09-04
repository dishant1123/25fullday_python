# data type  : 
"""
1. string   
2. list 
3. tuple 
4. dictionary 
5. set
"""

# list :  mutable squence  == > changes in list. 

"""
l1= [1,2,3,4,5,6,"aarav",12.56,5j]
print(l1)
print(type(l1))
"""

# list element access : 

# l1=       [1,2,3,4,5,6,"aarav",12.56,5j]
# index :  0 1 2 3 4 5  6       7    8
# index start :0 1 2 3 4 ... l to r      
# negative  index : start : -1  r to  l 
"""
print(l1[3])
print(l1[-1])
print(l1[-6])
"""

# built in function  : len min max  sorted sum 

# l1=[100,2,3,4,5,6,12.56,-9]

# print(len(l1))
# print(min(l1))
# print(max(l1))
# print(sorted(l1))  #asc to desc 
# print(sum(l1))

"""
for i in l1 :
    print(i)
"""

# method  : 

# l1=[100,2,3,4,5,6,12.56,-9]

"""
l1.append(101)  # append  ==> to add element in to the list ==>last  
print(l1)

l1.insert(0,101)  # 2 arg  ==> 1 index 2 value 
print(l1)

l1[4] =190  # list update 
print(l1)

l1.remove(-9)
print(l1)


l1.pop(3)
print(l1)
"""
# l2 =l1.copy()
# print("l2=",l2)

# desc to asc :
 
"""
l1.sort(reverse=True)
print(l1)  
"""

"""l1=[100,2,3,4,5,6,12.56,-9]
temp = l1.copy()
print(temp)
for  _ in range(len(temp)):  # len(8)
    m=max(temp)        # m = max(temp) 12.56
    print(m,end= " ")  # 100 12.56
    temp.remove(m)    #(100)
print()
"""

# l1 = [100,2,3,4,5,6,12.56,-9,100,100]

"""
l1.clear()
print(l1)
"""
"""l3 =l1.copy()
print(l3)
"""

"""
l2 =["mango","banana","apple","orange","kiwi"]

l1.extend(l2)  # merge two  list 
print(l1)
"""

# print(l1.count(100))

"""l1.reverse()
print(l1)

l1.sort()
print(l1)
"""

# index: 
"""l1 = [100,2,3,4,5,6,12.56,-9,100,100]

# print(l1.index(12.56))
# print(l1.index(100))
print(l1.index(100,9,20))   # value  ==> 100 , start ==> 0 index end ==>10 index 

"""

# slicing  : 
# l1=       [10,20,30,40,50,60,"aarav",12.56,5j]
#          0   1  2 3                        -3     -2     -1
# index :  0  1   2 3   4  5   6       7    8
# index start :0 1 2 3 4 ... l to r      
# negative  index : start : -1  r to  l 

"""print(l1[3])
print(l1[-1])
print(l1[-6])
print(l1[3 :6])  # 3 ==> start index 6 ==>end  index 
print(l1[ :6])
print(l1[1 :])
print(l1[3 : -3]) # 3 start  -3 end 
print(l1[-3 : 3]) # -3 start  -3 end 
print(l1[-5 : -2]) # -3 start  -3 end 
print(l1[-2 : -5]) # -3 start  -3 end 
"""

l1= [10,20,30,40,50,60,12.56,5]

"""print(l1[2 : 8 :2])
print(l1[2 : 7 :3])
print(l1[ : : 2])
print(l1[ : : -2])
print(l1[ : : -1])
"""
#asc  to desc : 

l2 =sorted(l1)  
print(l2)  # asc to  dec 

# desc to asc ; 
print(l2[ : : -1])

""" 
task  :1  remove the duplicate element from the list

l1 = [1,2,2,3,3,4,4,5,5,6,7,8,8,9,10]
output  : [1,2,3,4,5,6,7,8,9,10]
"""

"""
l1 = [1,2,2,3,3,4,4,5,5,6,7,8,8,9,10]
l2=[] 

for i in l1 :  # 1 2 2 
    if i not in l2 : # if 2 not in l2 
        l2.append(i)   # l2 =[1 2 ] 
print(l2)    

"""

# task  :2 

# input  : l1=[2,3,4,5,6,7,8,9,10]
# output : l1=[2,3,5,7]  print  only  prime element in list 