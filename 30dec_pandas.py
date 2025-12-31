# movies data set : 

import pandas as pd

df = pd.read_csv('movies.csv')
print(df)

#task :1  select * from movies where vote_average > 7

# task  :2 select title, director_name, revenue from movies where vote_average > 7

#task :3 Get me the movies which were released in or after 2015 and having vote_average more than 7

#task  :4 Print title, vote_average and revenue of movies released on weekends 

# task :5 Print title, vote_average of top 10 popular movies. 