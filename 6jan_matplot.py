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

"""movies =pd.read_csv('movies.csv')
directors =pd.read_csv('directors.csv')

movies=movies.drop(columns=['Unnamed: 0'])
directors=directors.drop(columns=['Unnamed: 0'])
"""
# print(movies.head())
# print(directors.head())

# analysis 1 : year  wise  movies ==> line graph  
# analysis 2 :   top 10 directors rating (vote_average) wise  movies ==> bar graph
# analysis 3 :  scatter graph
# analysis 4 : gender  distribution  using pie chart . 
"""
year   movie_count
1970     4 
"""
# analysis : 
"""movie_count = movies.groupby('year').size()
plt.plot(movie_count,marker='o',color='red')
plt.title('movies count')
plt.xlabel('year')
plt.ylabel('movie count')
plt.show()
"""

# 7 jan  : 
movies =pd.read_csv('movies.csv')
directors =pd.read_csv('directors.csv')

movies=movies.drop(columns=['Unnamed: 0'])
directors=directors.drop(columns=['Unnamed: 0'])

df = pd.merge(
    movies,
    directors,
    left_on="director_id",
    right_on="id",
    how="left"
)
# print(df)
# scatter plot  : 

"""plt.figure()
plt.scatter(movies["budget"],movies["revenue"],color='red')
plt.xlabel('budget')
plt.ylabel('revenue')
plt.title('scatter plot')
plt.show()
"""
#average rating per director  : 

"""avg_rating_directors= df.groupby("director_name")["vote_average"].mean().sort_values(ascending=False).head(10)
# print(avg_rating_directors)

plt.figure()
avg_rating_directors.plot(kind="bar",color="green")
plt.title("Average Rating Directors")
plt.xlabel("Directors")
plt.ylabel("Average Rating")
plt.show()
"""

#top  director by movie count : 

"""director_count = df["director_name"].value_counts().head(10)
print(director_count)

plt.figure()
director_count.plot(kind="barh",color="green")
plt.title("Top Director by Movie Count")
plt.xlabel("Movie Count")
plt.ylabel("Directors")
plt.show()
"""

# which gender has higher / lower rating . 
