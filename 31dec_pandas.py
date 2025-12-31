#join  : 
import pandas as pd

users =pd.DataFrame({
    "user_id" :[1,2,3],
    "name" :["shalin","purva","om"]    
})
# print(users)

msgs = pd.DataFrame({
    "user_id" :[1,1,2,4],
    "msg" :["hmm","okkk","how are you","yoyo"]
})
# print(msgs)

# print(pd.concat([users,msgs]))
# print(pd.concat([users,msgs],axis=0))
# print(pd.concat([users,msgs],axis=1))

# print(users.merge(msgs))  # inner join  

users.rename(columns={"user_id" :"id"},inplace=True)
# print(users)

# r =users.merge(msgs,left_on="id",right_on="user_id")
# print(r)
# r =users.merge(msgs,left_on="id",right_on="user_id",how="left")
# r =users.merge(msgs,left_on="id",right_on="user_id",how="right")
r =users.merge(msgs,left_on="id",right_on="user_id",how="outer")

print(r)

# movies and  director  ===> common column   == > join   ==> movies ==> last director_name 
