# create dataframe : 

import pandas as pd
import numpy as np 

df = pd.DataFrame({
    "name":["saumya","om","purva","reagen",None,"harshil","vidhi"],
    "age" :[21,19,21,19,25,19,np.nan],
    "salary":[25000,35000,45000,None,250000,350000,np.nan],
    "city":[None,"ahmedabad","bangalore","chennai","Mumbai","bangalore","manali"]
    
}
)
# print(df)

# delete  missing value :  function  ==>df.isna() , return true==>df.isnull()
"""
print(df.isna())
print(df.isnull())
"""
# count  :  missing count  :
"""
print(df.isna().sum())
"""

# remove rows missing value : 

"""df.dropna(inplace=True)
print(df)

df.dropna(how="all",inplace=True)
print(df)

df.dropna(how="any",inplace=True)
print(df)
"""

# fill missing value :

"""
df.fillna(value =0,inplace=True)
print(df)
"""

# data type ==> string  ==> object  null   ==> data type  ==> int  ==> 0.0 

"""for i in df.columns: 
    if df[i].dtype == "object":
        df[i]=df[i].fillna("null")
    else :
        df[i]=df[i].fillna(0.0)
print(df)
"""
# df.apply() : 

"""df2= pd.DataFrame({
    "a":[10,20,30],
    "b":[2,3,4]
}
    
)
print(df2)
print(df2.apply(sum))
"""
df =df.apply(lambda x :x.fillna("null") if x.dtype =="object" else x.fillna(0.0))
print(df)
print(df.info())


#loc  iloc : ,reset index 

"""
1.create dataframe 
2.add new column 
3.column name  ==> rename 
4.drop  ===> column  
5.where  ==> ex : salary   ==> between use  
6.missing  value  find  and count 
7.missing fill_value  
"""
