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

# b=np.genfromtxt('data3.txt',delimiter=",",dtype=str)
# print(b)
# print(np.genfromtxt('data3.txt',delimiter=",",dtype=str,skip_header=1))
# print(np.genfromtxt('data3.txt',delimiter=",",dtype=str,skip_footer=1))

# print(np.loadtxt('data1.txt',dtype=int,skiprows=1))


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

"""air = np.loadtxt("airbnb_large_dataset.txt",dtype=float,skiprows=1)
print(air)

total =len(air)
print(total)

"""

# fitbit : 

"""
task  :1 Print number of days user was sedantary (< 5000 steps), low active (5000 to 7499 steps), somewhat active (7500 to 9999 steps) and active (10k to 12499 steps).
"""