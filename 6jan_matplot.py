# pip install matplotlib 

import matplotlib.pyplot as plt 
import pandas as pd
import seaborn as sns
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
"""movies =pd.read_csv('movies.csv')
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
"""
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

# multiple line graph ==> budget and revenue trend  

"""year_data =df.groupby("year")[["budget","revenue"]].mean()

plt.figure()
plt.plot(year_data.index,year_data["budget"],color="red")
plt.plot(year_data.index,year_data["revenue"],color="blue")
plt.title("Budget and Revenue")
plt.xlabel("Year")
plt.ylabel("Amount")
plt.legend(["Budget","Revenue"])
plt.show()
"""

# using titanic  dataset : 

# analysis 1 : survival count  
# analysis 2 : survival count  by gender   ==> male  1  female 0 
# analysis 3 : survival by passenger_class  ==> 1st class  3  2nd class  2  3rd class  1  crew  0 
# analysis 4 : avg age male  or female   ==> age distribution  
# analysis 5 : fare vs survival 
# analysis 6 : age  bin  ==>10-20  20-30  30-40  ==>count  ==>survival vs age 
# analysis 7 : survival analysis using embark 

# df = pd.read_csv("Titanic-Dataset.csv")
# print(df)

# print(df.info())  # prints the shape of the dataframe , number missing value 
 
# ===== data cleaning  ======

# df["Age"] = df["Age"].fillna(df['Age'].mean())
# print(df)
# print(df.info())
# print(df[['PassengerId','Age']].head(50))

# embark :

# df['Embarked'] =df['Embarked'].fillna(df['Embarked'].mode()[0])
# print(df[['PassengerId','Age','Embarked']].head(65))


# drop  cabin  col  : 

# print(df.columns)
"""
if 'Cabin' in df.columns:
    df.drop(columns=['Cabin'],inplace=True) """
# print(df)
# print(df.info())

# analysis 1 : survival count

"""plt.figure() 
df["Survived"].value_counts().plot(kind="bar",color="green")
plt.xlabel("Survived")
plt.ylabel("Count")
plt.title("Survived Count")
plt.show()
"""
#  analysis 2 : survival  by gender : 

"""plt.figure()
df.groupby("Sex")["Survived"].sum().plot(kind="bar",color="red")
plt.xlabel("Sex")
plt.ylabel("Survived")
plt.title("Survived by Gender")
plt.show()
"""

# analysis  :3 

"""plt.figure()
df.groupby("Pclass")["Survived"].sum().plot(kind="bar",color="red")
plt.xlabel("Pclass")
plt.ylabel("Survived")
plt.title("Survived by Pclass")
plt.show()
"""

# age  distribution  : 
"""plt.figure()
plt.hist(df["Age"],bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
"""
# task : 4 adult  age  > 18  , < 18 


# ============================================================================== 

# seaborn :
"""
extention of  matplotlib . 
provides beautiful statistical graphics and easy to use plots with very little code. 

new : 

1. co relation  , regression  , distribution  
 ex.  dependent , independent  
2. normal distribution : 
  
"""

movies = pd.read_csv("movies.csv")
directors = pd.read_csv("directors.csv")

movies = movies.drop(columns=['Unnamed: 0']) 
directors = directors.drop(columns=['Unnamed: 0'])

# merged = movies.merge(
#     directors,
#     left_on="director_id",
#     right_on="id",
#     how="left"
# )
# print(movies.head())
# print(directors.head())

# pip install seaborn 

"""
sns.scatterplot(x="budget",y="revenue",data=movies)
plt.title("Budget vs Revenue")
plt.show()
#  ===> insights :1. movies with higher budgets generally earn higher revenues .
#   ===> 2. some outliners exist higher budget  but lowe revenue. 
"""

# popularity  vs  vote  avg : 

"""
sns.scatterplot(x="popularity",y="vote_average",data=movies)
plt.title("Popularity vs Vote Average")
plt.show()

# insights  ==> popular movies usually have  rating  between 6- 8. 
"""
 
# avg rating by director gender : 

"""merged = movies.merge(
    directors,
    left_on="director_id",
    right_on="id",
    how="left"
)

# print(merged.head())

sns.barplot(x="gender",y="vote_average",data=merged)
plt.title("Average Rating by Director Gender")
plt.show()

# insights  ==> avg  movies ratings by male and female  directos are almost similar. 
"""

# regression   analysis :
"""
it used to understand the relationship between two variables. 
that is  independent variable  and dependent variable. and also predict their values. 


regplot() 
lmplot()
"""

# budget  vs  revenue  :
"""
sns.regplot(x="budget",y="revenue",data=movies)
plt.title("Budget vs Revenue")
plt.show()

# insights  ==> regression  line slopes upward so  it positive  relationship between budget and revenue.  budget is strong predictor of revenue.
"""

# popularity  vs  vote avg  :

sns.regplot(x="popularity",y="vote_average",data=movies)
plt.title("Popularity vs Vote Average")
plt.show()

