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
"""d1={}

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
"""
srno   name    salary  
1      aarav   9000
2      harshil 99000
"""

"""
Royal Kids Bank :

Design a Banking App in c  that has the following functionalities:-
User can:-
◆OPEN ACCOUNT by username and password of his choice. On Opening account, his initial balance will be ₹ 25,000/-. 
Once he opens account, he can login by re-entering the same username & password.
◆LOGIN is compulsory to perform any task such as withdrawal, deposit or balance check. If the user name or password do 
not match, he can not Login. Once he is logged in, he can do as many transactions as he wants. He needs to Logout after 
he finishes all the transactions
◆DEPOSIT will enable user to deposit amount of money of his choice. His balance should be updated after the task 
completes.
◆WITHDRAW will enable user to withdraw amount of money of his choice. The only condition is that his balance at any 
point can not go less than ₹10,000/-. If this can happen after his withdrawal, your program must not allow that
transaction. His balance should be updated after the task completes.
◆CHECK BALANCE will show the latest updated balance to user.
◆LOGOUT will exit the user from the program
You should use these functions in your program: login(), deposit(), withdraw(), checkBalance()
"""

"""
1.  create : username  , password create :   username =aarav  ,password =aaru@123 
2 . login 
    username =aarav
    password = aaru@123
user = 25000 
1.deposit   ==>1000  ==>26000  
2.withdraw   min _balance =10000    === >2000 ==>24000  ===>18000 
3.check balance    ==> 24000 
4.exit 
"""