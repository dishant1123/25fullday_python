"""
dict : a dictionary is a collection of key-value pairs. ==> mutable 
"""

d1={"phy" :[89,90,92,78],
    "maths":(55,90,78,56),
    "com" :["shain","remo","maam","harshil"]
    }
# print(d1)

"""for  i ,j in d1.items(): 
    if i == "phy":
        print(i,j)
"""
"""
result =  {i:j for i,j in d1.items() if i=="phy"}
print(result)
"""
"""
print(d1["maths"])

d1["phy"].append(99)
print(d1)
"""

"""d1={"phy" :[89,90,92,78],
    "maths":(55,90,78,56),
    "com" :["shain","remo","maam","harshil"]
    }

for  i in d1["com"]:
    if i == i[: : -1]:
        print(i)
"""

"""
d2 ={"students":{"harshil":90,"shalin":89,"saumya":78,"om":91,"het":99}}

# print only those name  whose marks is  greater than 85.

for i ,j in d2["students"].items():
    if j >85 :
        print(i)
"""

"""
Print key having the longest string value.
input  : d3 = {"n1": "hello", "n2": "programming", "n3": "AI"}
output : n2
"""
d3 = {"n1": "hello", "n2": "programming", "n3": "AI"}

max_len =0   # values
max_key =""  # key 

for i ,j in d3.items():  #  {"n1": "hello", "n2": "programming", "n3": "AI"}
    if len(j) > max_len:   # 2 > 11  
        max_len=len(j)     #     max_len=11
        max_key=i           # max_key = "n2"
print(max_key)
