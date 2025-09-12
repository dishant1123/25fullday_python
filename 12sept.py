# arg , kwrgs : 

"""def sum1(a,b):
    return  a+ b 

print(sum1(12,90))
"""
#* args : only number  

"""def sum1(*args):
    return sum(args)   # sum ==> built in function  

print(sum1(1,2,3,4,5,6,7,8,9))
"""
# ** kwargs : 
"""
def d1(**kwargs):
    for  i ,j in kwargs.items():
        print(i,j)
d1(a="aarav",b=90)
"""

#app : emp  management system  : 
"""
1.add 
2.delete 
3.update 
4.search 
5.display 
"""
d1={}

def add_emp():
    srno=int(input("enter the  sr no :"))
    name =input("enter the  name :")
    salary=int(input("enter the  salary :"))
    d1[srno] =[name,salary]
    print("emp added successfully")

def delete_emp():
    srno=int(input("enter the  srno : "))
    if srno in d1 :
        del d1[srno]
    else :
        print("emp not found")
    print("emp deleted successfully")

def update_emp():
    srno=int(input("enter the  srno : "))
    if srno in d1 :
        name=input("enter the  name : ")
        salary=int(input("enter the  salary : "))
        d1[srno]=[name,salary]
        print("emp updated successfully")
    else :
        print("emp not found")
add_emp()
add_emp()
print(d1)
update_emp()
print(d1)
delete_emp()
print(d1)

"""
srno   name    salary  
1      aarav   9000
2      harshil 99000
"""