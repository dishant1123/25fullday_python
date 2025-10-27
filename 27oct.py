"""
inheritance  : 

1. single  level inheritance 

class a      ==>  base class 

class b (a)  ===>  derived class

2. mulple inheritance            vs     multi level  

class a     ==> base class                class a 

class b    ==> base class                 class b (a)

class c(a,b)   ==> derived class          class c(b)
======================
constructor  : def __init__(self) 

======================
private  : 
class a : 
    __name  
    __age 
    
    def display(self): 
        print(self.__name)
        print(self.__age)
"""

# hirechy  level of inheritance : multiple derivred class inhereit  from same base class.

"""
class a :  

class b(a) : 

class c (a)

class d(a): 
"""

class vehicle : 
    def __init__(self):  # name  model year ==> private 
        self.__name ="honda"
        self.__model="civic"  # non parameterized constructor
        self.__year=2012 
        
    def show(self):
        print("name : ",self.__name)
        print("model :",self.__model)
        print("year :",self.__year)
        
class car(vehicle):
    def __init__(self,color):
        super().__init__()  # call the base class constructor
        # vehicle.__init__(self)  # call the base class constructor
        self.color =color   # parameterized constructor
    
    def display(self):
        # vehicle.show(self)
        # self.show()
        print("color :",self.color)
        
class car1(vehicle):
    def __init__(self,seats):
        super().__init__()
        self.seats =seats
    
    def display1(self):
        self.show()  # method  
        print("seats :",self.seats)

c=car("red")
c.display()
c.show()

c1=car1(5)
c1.display1()
