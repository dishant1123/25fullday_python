# class : 
"""class person : # person is  class name   
    def saumya(self):  # function == > self ==> key word ==> function , data member  ==>access self   
        print("hello saumya")

p=person()  # p  object ==> class person 
p.saumya()  # object though function calling 
"""

# type  : 
"""
1. public :
2. private :
3. protected :
"""
"""
class person :
    name ="purva"  # name  age  clg  ==> data member  ==> class ==> person 
    age =21
    clg ="old lj"

    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)
p=person()
# print("name is  :",p.name)
# print("age is  :",p.age)
# print("clg is  :",p.clg)
p.show()
"""

# ex :
"""class employee :
    def staff(self):
        return "50 staff in my company"

    def staff(self):
        return "5000 staff in my company"
e=employee()
print(e.staff())  # func ==> overwrite 
"""

# ex :
"""class person :
    name ="purva"  # name  age  clg  ==> data member  ==> class ==> person 
    age =21
    clg ="old lj"

    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)
p=person()
# print("name is  :",p.name)
# print("age is  :",p.age)
# print("clg is  :",p.clg)
p.show()

p.name="harshil"
p.age=22
p.clg="pdu"
p.show()
"""

# private  : data member  == > with class accessible only  

"""class employee :
    __name ="purva"   # name  age  clg  ==> private data member  ==> class ==> person
    __company="PWC"
    __salary=90000 
    
    def show(self):
        print("name is  :",self.__name)
        print("company is  :",self.__company)
        print("salary is  :",self.__salary)
    
e=employee()  # e ==> object 
# print(e.__name)  # not accessible  bcz of  private
# print(e.__company)
# print(e.__salary)
e.show()

e.__name="harshil"  # not  change  bcz  of  private  only  accessible within class 
e.__company="KPMG"
e.__salary=100000
e.show()
"""

# private  function  : 

"""class vehicle :
    def __show(self):  # __show ==> private 
        print("vehicle class")
        __name="four wheeler"
        __model="s24"

    def display(self):
        self.__show()
        __name="two wheeler"
        __model="s22"
        print("vehicle name is  :",self.__name)
        print("vehicle model is  :",self.__model)
v=vehicle()
v.display()
"""
# bank  : 

class bank : 
    acc_holder_name="saumya"
    acc_number =7201345780 
    balance =90000  
    
    def depsoit(self,amt):
        self.balance +=amt 
        print("deposited amount is  :",amt)
    
    def withdraw(self,amt):
        if self.balance -amt >=10000: 
            self.balance -=amt
            print("withdrawed amount is  :",amt)
        else :
            print("not enough balance")
    
    def check_balance(self):
        print("balance is  :",self.balance)
    
    def show(self):
        print("account holder name is  :",self.acc_holder_name)
        print("account number is  :",self.acc_number)
        print("balance is  :",self.balance)

b=bank()
b.show()
b.depsoit(10000)
b.withdraw(45000)
b.check_balance()

# task :  1 
"""
generate  pin  : 
"""
