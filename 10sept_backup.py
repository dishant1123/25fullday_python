# split  , r split  , partition , r partition : 

s1="my name is vidhi."
"""print(s1.split())   # list 
print(s1.split("a"))   # list 
"""
# print(s1.rsplit())

# print(s1.partition("a"))  # 3 ==>  tuple  
# print(s1.partition("i"))  # 3 ==>  tuple  

# print(s1.rpartition("i"))
# print(s1.rpartition("a"))
"""print(s1.rpartition(" "))
print(s1.partition(" "))
"""
# join  : 
"""
l1=["my","name","is","vidhi."]
# my name is vidhi. 
s2=" ".join(l1)
print(s2)
"""

"""s1="my name is  the vidhi the tanna."

print(s1.replace("vidhi","saumya"))
print(s1.replace("the",""))
print(s1.replace("the","",2))
"""

# startwith ,endwith, removepreffix, removesuffix :

s1="my name is vidhi."
"""
print(s1.startswith("my n"))
print(s1.startswith(" n"))
print(s1.endswith("."))
print(s1.endswith("vidhi."))
print(s1.endswith(" vidhi."))
"""

"""print(s1.removeprefix("my"))
print(s1.removeprefix("my "))
print(s1.removeprefix(" name"))
"""

"""print(s1.removesuffix("."))
print(s1.removesuffix("vidhi."))
print(s1.removesuffix(" vidhi."))
print(s1.removesuffix("is"))
"""
# isalpha : 

"""s2="vidhi"
print(s2.isalpha())

s3="vidhi123"
print(s3.isalnum())

s4 ="my name is vidhi."
print(s4.islower())

s5="1234"
print(s5.isdigit())  # 0 -9 

s6="١٢٣٤٥"  # Arabic-Indic numerals # 
print(s6.isdecimal())
"""
print("½".isnumeric())       # True (Unicode fraction)
print("²".isnumeric())  

