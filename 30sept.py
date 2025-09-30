# constructor  : automatically called  when  object  is  created. 
"""
type : 

1. default  constructor 
2. parameterized  constructor
3. non parameterized  constructor
"""

# default constructor  :

"""class person : 
    def __init__(self):  # special method , constructor 
        print("my name is saumya.")
        print("live in ahmedabad.")
        
p=person()
"""

# constructor overloading  :
"""
class employees: 
    def __init__(self):
        print("my name is purva.")
        print("live in ahmedabad.")
    
    def __init__(self):
        print("my name is harshil.")
        print("live in gandhinagar.")

e=employees()
"""

# non- parameterized constructor  :

"""class employees:
    def __init__(self):
        self.name ="purva"
        self.age =21 
        self.clg ="old lj"

    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)
e=employees()
e.show()
e.name="harshil"
e.age=22
e.clg="pdu"
e.show()
"""
# parameterized constructor  :

"""
class employees:
    def __init__(self,name,age,clg):
        self.name =name
        self.age =age
        self.clg =clg
    
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)

e=employees("saumya",20,"grow-more")
e.show()
"""

# *args , **kwargs  :

"""def d1(*args):
    return sum(args)
print(d1(1, 2, 3, 4, 5, 6, 7, 8, 8.90,89))
"""

# **kwargs  : ==>dict 

"""def d2(**kwargs):
    for  i ,j in kwargs.items():
        print(i,j)
d2(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)
"""
# using  *args  and  **kwargs  in class :

"""class employees:
    def __init__(self,**kwargs):
        for  i ,j in kwargs.items():
            print(i,j)
e=employees(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)
"""

"""
class person :
    def __init__(self,*args,**kwargs):
        self.args=args
        self.kwargs=kwargs
    
    def show(self):
        for i in self.args:
            print(i)
    def display(self):
        for j in self.kwargs:
            print(f"{j} : {self.kwargs[j]}")
p=person(10,20,30,name="saumya",age=21,clg="old lj")
p.show() # ==> args  
p.display() # ==> kwargs
"""

class employees:
    def __init__(self,name,age,clg):
        self.name =name
        self.age =age
        self.clg =clg
    
    def show(self):
        print("name is  :",self.name)
        print("age is  :",self.age)
        print("clg is  :",self.clg)
name =input("enter name : ")
age =int(input("enter age : "))
clg =input("enter clg : ")

e=employees(name,age,clg)
e.show()
