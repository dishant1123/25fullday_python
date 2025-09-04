# string  :  immutable  ==>  you can't  change the string  . 

"""s1="my name is ketan."
print(s1)
print(type(s1))
"""
# s1[0]="om"  #error  bcz of string  is  immutable . 
# print(s1)

# built in function :  len  min max sorted

"""
s1 ="my name is ketan."
print(len(s1))
print(min(s1))
print(max(s1))
print(sorted(s1))
print(sum(s1))
"""

# slicing  : 
"""s1 ="my name is ketan."
#
print(s1[4])
print(s1[2:4])
print(s1[-4:-2])

print(s1[2:-5])
print(s1[1:10:2])
print(s1[ -1:10:-2])
print(s1[11:2:-2])
print(s1[ : :-2])
print(s1[ : :-1])
print(s1[ : :1])
"""
# task  :1 
"""
input  :  "dishant dipakkumar shah
output  : d.d.shah
"""
# task  :2 
"""
ask user to  enter the  two string and  interchange  the  first three letter . 

input  1 :color 
input  2 :full

output :1 fulor 
output :2 coll
"""

"""s1="dishant dipakkumar shah"
print(s1[0] + "." +s1[8] + "." + s1[19 : ])
"""

"""s1=input("enter the string 1: ")  # color
s2=input("enter the string 2: ")  # full 

a= s2[ 0:3] + s1[3 :]
b= s1[ 0:3] + s2[3 :]

print(a)
print(b)
"""

"""
home work : 

input  :1 
Original dictionary: sort by value asc to desc 

d1 = {'name1': 'Theodore', 'name2': 'Mathew', 'name4': 'Roxanne', 'name3': 'David'}
output : {'name3': 'David', 'name2': 'Mathew', 'name4': 'Roxanne','name1': 'Theodore'}
"""