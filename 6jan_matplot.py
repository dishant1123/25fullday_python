# pip install matplotlib 

import matplotlib.pyplot as plt 
import pandas as pd
"""
plt.plot() ==> line graph 
plt.scatter() ==> scatter graph
plt.hist() ==> histogram
plt.bar() ==> bar graph
plt.boxplot() ==> box plot

plt.title() ==> title   ==> heading  
plt.xlabel() ==> x label 
plt.ylabel() ==> y label

plt.figure() ==> create a figure  ((6,4))
plt.show() ==> graph  show 
"""

# line graph 

"""
x=[1,2,3,4,5]
y=[1,4,9,16,25] 

plt.figure(figsize=(6,4))
plt.plot(x,y,marker='o',color='red')
plt.title('line graph')
plt.xlabel('x axis')
plt.ylabel('y axis')

plt.show()
"""
# bar graph : 

"""name=["purva","bhagyashree","jaya","kaushik","deepak"]
marks=[90,78,56,45,66]
marks_sorted =sorted(marks,reverse=True)
plt.bar(name,marks_sorted,color='red',align='center')
plt.title('bar graph')
plt.xlabel('name')
plt.ylabel('marks')
plt.show()
"""

# histogram : 

"""marks = [
    45, 55, 60, 70, 72, 75, 80, 82, 85, 88,
    90, 92, 95, 78, 68, 58, 48, 65, 73, 77
]

plt.hist(marks,bins =10)
plt.title('histogram')
plt.xlabel('marks')
plt.ylabel('frequency')
plt.show()
"""

# scatter graph :

"""x=[1,2,3,4,5]
y=[1,4,9,16,25]
plt.scatter(x,y,marker='o',color='red')
plt.title('scatter graph')
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.show()
"""

# movies , directors : 

movies =pd.read_csv('movies.csv')
directors =pd.read_csv('directors.csv')

movies=movies.drop(columns=['Unnamed: 0'])
directors=directors.drop(columns=['Unnamed: 0'])

# print(movies.head())
# print(directors.head())

# analysis 1 : year  wise  movies ==> line graph  
# analysis 2 :   top 10 directors rating (vote_average) wise  movies ==> bar graph
# analysis 3 :  scatter graph

"""
year   movie_count
1970     4 
"""
# analysis : 
movie_count = movies.groupby('year').size()
plt.plot(movie_count,marker='o',color='red')
plt.title('movies count')
plt.xlabel('year')
plt.ylabel('movie count')
plt.show()
