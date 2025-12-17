"""
use :
1. csv access , read . 
2. data cleaning  
3. data manipulation 
"""
import pandas as pd    # pip install  pandas 

# df=pd.read_csv("mckinsey.csv")
# print(df)

# sql first  5 row  :  fetch , last 5 row  ==> offset, 12 -18 ==> offset 
"""
head , tail 
"""
# print(df.head(10))
# print(df.tail(10))

# print  ==> country , and  print  multiple  rows :  
"""
print(df["country"])
print(df.info())
print(df[["country","year","gdp_cap"]].head(20))
"""

# create  dataframe : 
"""
t1 =pd.DataFrame([
    ["saumya",19,25000],
    ["om",19,35000],
    ["purva",21,45000],
    ["reagen",19,75000],
    ["het",19,250000],
    ["harshil",19,350000],
    ["vidhi",20,450000]],columns=["name","age","salary"]
    
)"""
# print(t1)


t2=pd.DataFrame({
    "name":["saumya","om","purva","reagen","het","harshil","vidhi"],
    "age":[19,19,21,19,None,19,20],
    "salary":[25000,35000,45000,75000,250000,350000,450000]
})
# print(t2)
# print(t2.columns)
# print(t2.info())

t2= t2.rename(columns={
    "name" :"Name", 
    "salary":"Stipend"
})
# print(t2)

t2["Gender"]=["M","M","F","M","M","M","F"]
print(t2)