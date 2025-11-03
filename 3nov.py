# polymorphism  :  many forms same name  diffrerent behavior
"""
1. method overriding  
2. method overloading
"""

# method  overloading  function  overloading with default arg  : 

"""class calculation  : 
    def add(self,a=10,b=90,c=0):
        return a+b+c 

    def sub(self,a,b):
        return a-b 
    
c=calculation() 
print(c.add()) # 3 ==>   10 +90 +0  ==> 100   ==>default  arg 
print(c.add(a=90,b=10,c=5))  #  90 +10 +5 =105 
print(c.add(a=100,b=89))    # 100 +89 + 0 =189 
print(c.add(b=67))  # 10 +67 +0 =77
print(c.sub(12,56))  # its is compulsory to pass 2 arg bcz no default arg set. 
"""

# method  overriding  : 

"""class animal : 
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):  
        print("dog sound")

class cat(animal):
    def sound(self):
        print("cat sound")
        
d=dog()
d.sound() 


animal = [dog(), cat()]
for i in animal :
    i.sound()
"""
# sound() ==> in subclass override the  parent class method  ==> this is called run time polymorphism. 

# poly  + inheri + overloading  + riding  : 

class bank : 
    def __init__(self,name,balance =0):  # default arg  : balance  =0 
        self.name =name  
        self.balance =balance
    
    def deposit(self,amt=0,bonus=0):
        self.balance += amt +bonus  # self.bal = self.bal +amt +bonus 
        print(f'deposited {amt} + bonus :{bonus} = {amt +bonus}')
        
    def display(self):
        print(f'name : {self.name} balance : {self.balance}')

# base  class overriding  method 
class savings(bank):
    def __init__(self, name, balance=0,int_rate=5):
        super().__init__(name, balance)
        self.int_rate = int_rate
        
    def display(self):
        print(f'savings account info  || balance : {self.balance} || interest_rate : {self.int_rate}')
        
class current(bank):
    def __init__(self, name, balance=0,trasacation_limit=50000):
        super().__init__(name, balance)
        self.trasacation_limit = trasacation_limit
    
    def display(self):
        print(f'current account info  || balance : {self.balance} || trasacation_limit : {self.trasacation_limit}')

s1=savings("saumya",80000) 
c1 =current("harshil",900000)

# method  overloading  : (same funcation diff arg  )

s1.deposit(10000)
c1.deposit(50000,200) 

# method  overriding  (same name  diff class behaviour )

s1.display()
c1.display()