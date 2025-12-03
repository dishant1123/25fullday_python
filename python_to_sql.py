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

cursor.execute("CREATE TABLE IF NOT EXISTS emp (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(20), salary INT)")

print("table created successfully")
cursor.close()
conn.close()
