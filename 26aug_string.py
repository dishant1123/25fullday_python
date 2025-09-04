# string  methods : 

# s1= "My name Is Ketan."

"""
print(s1.capitalize())
print(s1.lower())
print(s1.upper())
print(s1.title())
print(s1.swapcase())
print(s1.casefold())
"""

"""
s2 ="happy ganesh"
print(s2)
print(s2.center(50,"*"))
print(s2.ljust(50,"*"))
print(s2.rjust(50,"*"))
"""
s1= "my name is ketan."

# index find rindex rfind : 

"""
print(s1.index("y"))
print(s1.index("i"))
print(s1.index("a"))
print(s1.index("a",5,20))
print(s1.index("na"))
print(s1.index("k"))
print(s1.index("etan"))
print(s1.index(" ketan"))

print(s1.find("y"))
print(s1.find("k"))
print(s1.find("etan"))
print(s1.find(" ketan"))
"""

s1= "my name is ketan."

"""print(s1.rindex("a"))
print(s1.rindex("e"))
print(s1.rindex("is"))

print(s1.rfind("a"))
print(s1.rfind("e"))
print(s1.rfind("is"))
"""

# task  :1 
"""
input  : "i am going  to goa next month."
output  : first "o" index number is  :6
          second "o" index number is  :12
          third "o" index number is  :15
          fourth "o" index number is  :24

"""

"""s1 ="i am going to goa next month."

for i in range(len(s1)): 
    if s1[i] =="o":
        print(i)
"""

# replace : 

"""s3 ="the lion in the cage."

print(s3.replace("the"," "))
print(s3.replace("the","90",1))
"""

"""
task  :2 
change the  second "r" with "@" .
hint :  slicing +  replace 

input : restart 
output : resta@t

task  : 3 
ask user to enter the string and  first  and  last space with underscore (_). 
hint :  slicing +  replace

input : my name is harshil thakkar and i am master of table tennis.
output :my_name is harshil thakkar and i am master of table_tennis.  

"""

"""
s1="my name is harshil thakkar and i am master of table tennis."

s2= s1.replace(" ","_",1)[ : : -1].replace(" ","_",1)[ : : -1]
print(s2)
"""

# split , rspilt  : 

s1="my name is het." 

"""print(s1.split())
print(s1.split("a"))
print(s1.split("e"))

# rsplit : diff between split and rsplit .

print(s1.rsplit("e"))
"""

# partition  : 

s1="my name is het." 

# print(s1.partition("e"))
# print(s1.partition("name"))

"""print(s1.rpartition("e"))
print(s1.rpartition("si"))
"""

# print(s1.partition())  # error 

