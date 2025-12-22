import  pandas as pd 
import numpy as np
t2=pd.DataFrame({
    "name":["saumya","om","purva","reagen","het","harshil","vidhi"],
    "age":[26,19,21,19,25,19,20],
    "salary":[25000,35000,45000,7500,250000,350000,450000]
})
 
# task :1 select  * from  employees where salary  >10000 
# print(t2[t2["salary"]>10000])

# task  :2 select  * from employees where name in ("om","purva")
# print(t2[t2["name"].isin(["om","purva"])])

# task :3 select * from employees where age >25 and salary  >90000 
# and ==>&   or ==> |  

# print(t2[(t2["age"]>=25)&(t2["salary"]>90000)])
# print(t2[(t2["age"]>25)|(t2["salary"]>90000)])

# task :4 select  * from employees where name NOT IN ("om","purva")
# print(t2[~t2["name"].isin(["om","purva"])])

#task :5 select  * from  employees where  salary between 50000 and 100000 
# print(t2[t2["salary"].between(10000,400000)])

# task :6 select * from employees where name like "s%"
# print(t2[t2["name"].str.startswith("s")])
# print(t2[t2["name"].str.contains("h")])

# task  :7  np.where()
"""
select name case when salary >50000 
            THEN "high salary"
            else "low salary"
        end 
        from employees
"""
"""
t2["salary_type"] =np.where(t2["salary"]>50000,"high salary","low salary")
print(t2)
"""

# print(t2.query("salary >50000"))
# print(t2.query("salary >25000 and name =='om'"))
print(t2.query("name in ['om','purva']"))