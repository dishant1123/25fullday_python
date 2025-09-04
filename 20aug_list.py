# 
"""
Write a Python program that accepts a list of integers and calculates the length and the 
	fifth element. Return true if the 
	length of the list is 8 and the fifth element occurs thrice in the said list.
	Input:
	[19, 19, 15, 5, 5, 5, 1, 2]
	Output:
	True
	Input:
	[19, 15, 5, 7, 5, 5, 2]
	Output:
	False

"""
l1=[19,19,7,7,90,89,90,900]

"""for i in l1 : 
    if len(l1) ==8 and l1.count(l1[4]):
        print(True)
        break
else :
        print(False)
"""

"""if len(l1) ==8 : 
    l5=l1[4]
    if l1.count(l5) ==3 :
        print(True)
    else :
        print(False)
"""

# tuple  :  immutable   ==>  cannot change

"""t1=(1,2,3,4,5,6,7,8,9,10,"ram",12.56)

print(t1)
print(type(t1))

t2 = 1,2,3,4,5,6,7,8,9,10,"ram",12.56
print(t2)
print(type(t2))
"""

# built in function  :  len min max sorted sum 

"""
t1= 1,2,3,4,5,900,7,200
print(len(t1))
print(min(t1))
print(max(t1))
print(sorted(t1))
print(sum(t1))
"""

# slicing  : 
# t1= 10,20,30,40,50,900,7,200

"""print(t1[4])
print(t1[3:4])
"""
"""t1[2]="purva"
print(t1)  # error  bcz  tuple  immutable 
"""
"""print(t1[2 :4 :1])
print(t1[2 :-2 :2])
"""

# method  : 

t1= 10,20,30,40,50,900,7,200,50,50

"""# print(t1.count(50))
print(t1.index(50))
print(t1.index(50,5,10))
"""

# task :1 
"""
t1= 10,20,30,40,50,900,7,200,50,50
output : t1= 10,20,30,40,50,900,7,200,50,50,"harshil"
 
"""

"""t1= 10,20,30,40,50,900,7,200,50,50
l1 =list(t1)
print(l1)
l1.append("harshil")
print(tuple(l1))"""
# mcq : 
"""
1.
t1 = (10,20,30,[3,4,5],90) 
t1[3]="harshil"
print(t1)

options :

a.error     ==> D s p H  n h 
b.t1= (10,20,30,[3,4,5],90,"harshil")
c.t1= (10,20,30,[3,4,5],90)
d.t1= (10,20,30,["harshil",4,5],90)

"""

"""t1 = (10,20,30,[3,4,5],90) 
t1[3][0]=("harshil")
print(t1)
"""

"""
Write a Python program to replace the last value of tuples in a list.

Sample list: [(10, 20, 40), (40, 50, 60), (70, 80, 90)]
Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]
"""

"""
t1 =[(10, 20, 40), (40, 50, 60), (70, 80, 90)]

l1=[] 
for i in t1:
    temp=list(i)  # [10 20 40]
    temp[-1]= 100
    l1.append(tuple(temp))
print(l1)

"""
