import pandas as pd
import numpy as np
# group by  :

"""
sql  : 
1.summary function  : sum count min max avg 
2. nested summary   
    ex : department wise   min  or max salary . 
        select min(salary) from   employees group by department_id ; 
"""


movies = pd.read_csv("movies.csv")
directors = pd.read_csv("directors.csv")
movies = movies.drop(columns="Unnamed: 0")
directors = directors.drop(columns="Unnamed: 0")


df = pd.merge(
    movies, 
    directors,
    left_on="director_id",
    right_on="id",
    how="left"
)
# print(df.head())


#task :1  total movies directed by each director:
movies_per_director = df.groupby("director_name")["title"].count().sort_values(ascending=False)
print(movies_per_director) 

# task :2 avg movies rating by director 
