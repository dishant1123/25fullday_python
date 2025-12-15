import numpy as np
# loadfrom txt ,  genfromtxt : 
"""
loadtxt ==> missing values are not  handle .
only int value not string 
"""
"""a= np.loadtxt('data1.txt',dtype=str)
print(a)
"""
# genfromtxt ==> missing values are handle .


"""a=np.genfromtxt('data2.txt',delimiter=",",dtype=int)
print(a)
"""

b=np.genfromtxt('data3.txt',delimiter=",",dtype=str)
# print(b)
# print(np.genfromtxt('data3.txt',delimiter=",",dtype=str,skip_header=1))
# print(np.genfromtxt('data3.txt',delimiter=",",dtype=str,skip_footer=1))

print(np.loadtxt('data1.txt',dtype=int,skiprows=1))


# task  :1 
"""
nps: Net Promoters' Score
Score
1 to 6: Detractors
7 or 8: Neutral
9 or 10: Promoters
nps = % of promters - % of detractors

Example
60% - Promoters
10% - Neutral
30% - Detractors
nps = 60 - 30 = 30
Therefore, usually nps above 70 is considered excellent.
"""