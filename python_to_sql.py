"""
employees region department locations:

database ==> emp 
        tables   ==> employees regions department locations 
CREATE DATABASE database_name;   or 

create database if not exists database_name;

table : 

CREATE TABLE  table_name 
id number primary key auto_increment, 
name varchar(20),
salary number

insert row  : 

insert into table_name (name, salary) values ('name', 'salary');
"""

import  mysql.connector 

conn =mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root", 
    password="root",
    database="employees"
)

cursor=conn.cursor()

# cursor.execute("CREATE DATABASE IF NOT EXISTS employees")

# cursor.execute("CREATE TABLE IF NOT EXISTS emp (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), salary INT)")

# cursor.execute("INSERT INTO emp (name, salary) VALUES ('John Doe', 30000)")
# cursor.execute("INSERT INTO emp (name, salary) VALUES ('Alice Smith', 25000)")
# cursor.execute("INSERT INTO emp (name, salary) VALUES ('Bob Johnson', 35000)")
# cursor.execute("INSERT INTO emp (name, salary) VALUES ('ramesh', 45000)")

# cursor.execute("UPDATE emp SET salary = salary +10000 WHERE name = 'ramesh'")

# cursor.execute("DELETE FROM emp WHERE name = 'Bob Johnson'")

cursor.execute("SELECT * FROM emp")
row =cursor.fetchall()

for i in row :
    print(i)

# conn.commit()
# print("deleted successfully")
cursor.close()
conn.close()
