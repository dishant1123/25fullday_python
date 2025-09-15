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

"""accounts={}
logged_in_user =None
account_type =None 

def open_account():
    global accounts,account_type
    username =input("enter the username : ")
    if username in accounts :
        print("account already exists")
        return 
    password =input("enter the password : ")
    # intial balance =25000 
    accounts[username]={
        "password":password,
        "balance":25000,
        "type":account_type
        }
    print("account created successfully")

def login():
    global logged_in_user
    username =input("enter the username : ")
    password =input("enter the  password : ")
    if username in accounts and accounts[username]["password"]==password :
        logged_in_user=username
        print("login successful")
    else :
        print("login failed") 

def deposit():
    global logged_in_user 
    if logged_in_user is None :
        print("you are not logged in")
        return 
    amount =int(input("enter the  amount  you want  to deposit :"))
    accounts[logged_in_user]["balance"] +=amount 
    print("deposit successful")

def withdraw():
    global logged_in_user
    if logged_in_user is None :
        print("you are not logged in")
        return 
    amount = int(input("enter the  amount  you want  to withdraw :"))
    account_type=accounts[logged_in_user]["type"]

    if account_type =="savings" :
        if accounts[logged_in_user]["balance"]  -amount >=10000 :
            accounts[logged_in_user]["balance"] -=amount
            print("withdraw successful")
        else :
            print("insufficient balance min balance required is 10000")
    elif account_type =="current" :
        # tax ==>  facilities :  2 % or 5% 
        # with _amt  ==>  > 50000  == >tax 5 %  < 50000 ==>tax 2% 
        # taxable  amt deducted ==> final  balance 
        over_draft= 5000 
        if accounts[logged_in_user]["balance"]  -amount >=over_draft :
            accounts[logged_in_user]["balance"] -=amount
            print("withdraw successful")
        else :
            print("insufficient balance min balance required is 5000")
    
def check_balance():
    global logged_in_user
    if logged_in_user is None :
        print("you are not logged in")
        return 
    account_type=accounts[logged_in_user]["type"]
    
    print("your balance is :",accounts[logged_in_user]["balance"])

def logout():
    global logged_in_user
    if logged_in_user :
        print("goddbye  thx for using our app")
        logged_in_user=None
    else :
        print("you are not logged in")

def main() :
"""
# task  : 1  menu driven 
"""
1. saving  acc 
2. current acc
3 . exit 

    1.open account 
    2. login 
    3. deposit
    4. withdraw
    5. check balance
    6. logout/ exit 
    7. back  to  bank 
"""
"""
HW : 
    VEHICLE MANAGEMENT SYSTEM

1. add == > create a vehicle 
2. delete == > delete a vehicle
3. update == > update a vehicle
4. search == > search a vehicle
5. display == > display all the vehicles
6. exit == > exit the program

use list  ==> []
menu driven :  
"""