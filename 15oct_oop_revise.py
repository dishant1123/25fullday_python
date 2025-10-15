# oop  : 
"""
class object : 
"""
"""class student:
    name ="purva"  # name ,age  , clg ==> class data member 
    age=20          # by default ==> public  
    clg ="LJ"
    
    def show(self):
       print(self.name)
       print(self.age)
       print(self.clg)
    
s=student()
s.show()
# print(s.name)
# print(s.age)
# print(s.clg)
"""

# private : 

"""class vehicle : 
    __name="vehicle"  # name type model  ==> private 
    __type ="two wheeler"
    __model="honda"
    
    def __show(self):
        print(self.__name)
        print(self.__type)
        print(self.__model)
    
    def display(self):
        self.__show()
v=vehicle()
# print(v.__name)# bcz of private you can't access though object 
# v.show()
v.display()
"""
# constructor   : 

"""class student : 
    def __init__(self):
        self.name ="purva"  # name ,age  , clg ==> class data member
        self.age=20          # by default ==> public
        self.clg ="LJ"
        
s=student()
print(s.name)
print(s.age)
print(s.clg)
"""

"""class vehicle :
    def __init__(self,name,type,model):
        self.name=name
        self.type=type
        self.model=model
        
v=vehicle("honda","two wheeler","2020")
# print(v.name)
v.model="toyota"
print(v.model)
"""

# type  : 
"""
single level inheritance :

class a       ==> base class /parent class

class b(a)   ===> derived class /child class
"""

# multiple level inheritance  vs multi level: 
"""
class a                class a 

class b                class b (a)  ==>b ==>a 

class c(a,b)           class c(b)  ==> c ==>a ,b 
"""

# app :  employee management system : 

class employees : 
    def __init__(self):
        self.data ={}
        print("base class constructor  called ...")
        
class employeesDB(employees):   # single level inheritance 
    def add(self):
        id =int(input("enter the  employee id : "))
        name =input("enter the  employee name : ")
        salary =int(input("enter the  employee salary : "))
        self.data[id]=[name,salary]
        print("data added successfully ...")

class employeesoperation(employeesDB):  # multi level inheritance
    def delete_emp(self):
        id =int(input("enter the  employee id  you want to delete: "))# 1 
        if id  in self.data:
            del self.data[id]
            print("data deleted successfully ...")
        else :
            print("data not found ...") 
    def update_emp(self):
        id =int(input("enter the  employee id  you want to update: "))
        if id  in self.data:
            name =input("enter the  employee new name : ")
            salary =int(input("enter the  employee new salary : "))
            self.data[id]=[name,salary]
            print("data updated successfully ...")
        else :
            print("data not found ...")

class serach_display():
    def serach(self):
        id =int(input("enter the  employee id  you want to serach: "))
        if id  in self.data:
            print(f" name : {self.data[id][0]}, salary : {self.data[id][1]}")
        else :
            print("data not found ...")
            
    def display_all(self):
        print("===========all employee data ===========")
        for i ,j in self.data.items():
            print(f" id : {i} , name : {j[0]} , salary : {j[1]}")

class emp_manag_system(employeesoperation,serach_display):  # multi ple 
    def __init__(self):
        super().__init__()  # base  class constructor  called ...
        # employees.__init__(self)

obj =emp_manag_system() 

while True :
    print("============employee management system ===========")
    print("1.add")
    print("2.delete")
    print("3.update")
    print("4.serach")
    print("5.display all")
    print("6.exit")
    
    choice =int(input("enter your choice : "))
    if choice==1:
        obj.add()
    elif choice==2:
        obj.delete_emp()
    elif choice==3:
        obj.update_emp()
    elif choice==4:
        obj.serach()
    elif choice==5:
        obj.display_all()
    elif choice==6:
        print("thanks for using ...")
        break 
    else :
        print("invalid choice")
        break


"""
                            key : [value]
id    name   salary       id : name , salary   
1     ram    90000        1     ram   90000 
2     shyam  80000        2     shyam 80000
"""