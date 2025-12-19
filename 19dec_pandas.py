import pandas as pd 

"""
t2=pd.DataFrame({
    "name":["saumya","om","purva","reagen","het","harshil","vidhi"],
    "age":[19,19,21,19,25,19,20],
    "salary":[25000,35000,45000,75000,250000,350000,450000]
})
"""

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
"""
df =pd.read_csv("mckinsey.csv")
df["next_survery_year"] =df["year"]+3
print(df)

"""
# isin , where ==> sql  
t2=pd.DataFrame({
    "name":["saumya","om","purva","reagen","het","harshil","vidhi"],
    "age":[19,19,21,19,25,19,20],
    "salary":[25000,35000,45000,75000,250000,350000,450000]
})

# selected_names =["om","purva"]

# print(t2["name"].isin(selected_names))
"""
age_t2 = t2[t2["age"].isin([19,25])]
print(age_t2)
print(t2[t2["age"].isin([19,25])])
"""

# task :1 where ==> select  * from employees where age >20 

# print(t2[t2["age"]>20])

# task :2 selct * from employees where name in ("om","purva") 

# task  :3 select * from employees where age >25 and salary >50000 
# print(t2[(t2["age"]>=25) & (t2["salary"]>50000) ])

#task :4 SELECT * FROM employee WHERE age = 19 OR age = 22;
print(t2[(t2["age"]==19) | (t2["age"]==21)])
