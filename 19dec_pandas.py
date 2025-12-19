import pandas as pd 

t2=pd.DataFrame({
    "name":["saumya","om","purva","reagen","het","harshil","vidhi"],
    "age":[19,19,21,19,25,19,20],
    "salary":[25000,35000,45000,75000,250000,350000,450000]
})

# print(t2)
# col wise drop : 
"""
print(t2.drop("age",axis=1))
print(t2.drop(["age","salary"],axis=1))
print(t2.drop(columns="age"))
print(t2.drop(columns=["age","salary"]))

"""
#row wise  drop :
"""
print(t2.drop(t2[t2["name"] == "purva"].index))
print(t2.drop(columns='purva'))
print(t2.drop(t2[t2["age"] == 19].index))
print(t2.drop(index=2))

"""

# give me new  col  for  year+3 :