import  pandas as pd 
import numpy as np
"""
loc : explicit index 
iloc : implicit  index 
"""

df= pd.read_csv("mckinsey.csv")
# print(df)

# print(df.loc[1])
# print(df.iloc[1])

# print(df.loc[5:13])  # first  and  last both included 
# print(df.iloc[5:13])     # last excluded 
# print(df)
# print(df.loc[2:5,"year":"gdp_cap"])
# print(df.iloc[2:5,1:4])
# print(df.iloc[[1,4,6,7],[0,3,4]])
# print(df.loc[0:20:2])

# print(df.iloc[[2,7]])  # 2,7 
# print(df.loc[[2,7]])  # 2,7 ,2 

# print(df.loc[-1])  # key error  not  possible  in loc minus  index .
# print(df.iloc[-1])  # give  output  of  last row.

# print(df.iloc[[-1,0,1]])
# print(df.iloc[[-1,1703]])
  

# temp = df.set_index("country")
# print(temp)

# india =temp.loc["India"]
# print(india)

# df.index = np.arange(1,1705)
# print(df)

# specific year information  to print  using  loc or  iloc : 

# print(df.loc[df["year"]==2007])

