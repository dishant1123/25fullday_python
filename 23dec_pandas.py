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

df.fillna(value =0,inplace=True)
print(df)