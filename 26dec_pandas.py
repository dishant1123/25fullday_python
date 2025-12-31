import pandas as pd 

df = pd.DataFrame({
    "ID": [1,2,3,4,5,6,7],
    "name":["om","saumya","het","harshil","vidhi","purva","shalin"],
    "age":[19,20,25,23,19,20,20], 
    "marks":[81,89,87,82,90,78,95],
    "city":["nagpur","ahmedabad","delhi","mumbai","kolkata","pune","bangalore"]
})
# print(df)

# sort marks : asc to desc  
# print(df.sort_values("marks",ascending=True))
# print(df.sort_values("marks",ascending=False))

# sort  by  city and  marks  : 
# city  ==>asc to desc  marks  ==>desc to asc  ==> sql  ==>  

# select city , marks from employees order by city asc, marks desc ; 

# print(df.sort_values(["age","marks"],ascending=[True,True]))

# filter  : 

# print(df[df["marks"]>90])
"""a= df.query("marks>=90")
print(a)
"""

# top  3 marks  : 
"""print(df.nlargest(3,"marks"))
print(df.nlargest(3,"marks"))
"""
# bottom 3 marks : 
# print(df.nsmallest(3,"marks"))

# print(df.filter(like="ar"))
# print(df.filter(like="a"))

# random 5 sample  : 
print(df.sample(3))

import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9,10])
print(np.average(a))


a=np.ones(4).reshape(2,2)
print(a)