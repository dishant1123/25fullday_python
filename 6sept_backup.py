# string  : immutable  ==> no changes in string. 

"""
s1="my name is saumya."

print(s1)
print(type(s1))
"""
# built in function  : len  min max sorted  

s1="my name is saumya."

"""
print(len(s1))
print(min(s1))  # ascci value 
print(max(s1))
print(sorted(s1))

"""
# slicing : 
"""
s1="my name is saumya."
#   012345678
print(s1[4])
print(s1[3])
print(s1[4:8])
print(s1[4:10])
print(s1[2:4])
print(s1[5:9])
print(s1[-2 ])
print(s1[-12 :-2 ])

print(s1[2: 8 :2])
print(s1[ :   :-2])
print(s1[ :   :-1])
"""

"""
task :1 

input  : "dishant dipakkumar shah"
ouptut : d.d.shah

task  :2 
ask user  to enter the  two string  and  interchange the  first  three character. 

input  1 : color 
input  2 :full 

output 1 : fulor 
output 2 : coll

"""

"""d1="dishant dipakkumar shah"
print(d1[0] +"."+d1[8]+"."+d1[19:])
"""

# method  : 
s1="my name is saumya."

"""print(s1.capitalize())
print(s1.upper())
print(s1.lower())
print(s1.title())
print(s1.swapcase())
print(s1.casefold())

"""
"""
s2="happy diwali"

print(s2.center(50,"="))
print(s2.ljust(50,"="))
print(s2.rjust(50,"="))
"""

# index r index  find  rfind : 

s1="my name is saumya."

"""
print(s1.index("i"))
print(s1.index("name"))
print(s1.index("ame"))
print(s1.index("a"))
print(s1.index("a",5,20))
print(s1.index("a",13,20))

print(s1.find("i"))
print(s1.find("name"))
print(s1.find("ame"))
print(s1.find("me"))
"""
"""
print(s1.rindex("a"))
print(s1.rindex("s"))

print(s1.rfind("a"))
print(s1.rfind("s"))
"""

"""s1="my name is saumya."
print(s1.count("a"))
print(s1.count("a",10,20))
"""

#task  :3 
"""
input  : s1 ="i am going to goa next month." 
output : first "o" index number  :6 
         second "o"  index number :12
         third "o" index number  :15 
         fourth "o" index number :24  
"""