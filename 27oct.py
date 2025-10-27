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

"""class vehicle : 
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
"""

# hybrid level  of inheritance  : 
"""
it is  combination of  two or more inheritance ex : multiple  , multi level 
"""
class a : 
    def __init__(self):
        print("constructor  of A (non parameterized)")
        self.a_data="data from A class "
    
    def showA(self):
        print("class A method :",self.a_data)

class b (a) : 
    def __init__(self,b_data):
        super().__init__()  # call the base class constructor
        print("constructor  of B (parameterized)")
        self.b_data=b_data
        
    def showB(self):
        print("class B method :",self.b_data)

class c : 
    def __init__(self,c_data):
        print("constructor  of C (parameterized)")
        self.c_data=c_data
    
    def showc(self):
        print("class C method :",self.c_data)

class d(b,c):
    def __init__(self,b_value,c_value,d_value):
        b.__init__(self,b_value)  # call the base class constructor
        c.__init__(self,c_value) 
        self.d_value=d_value
        
        print("constructor  of D (parameterized)")
        
    def showD(self):
        print("class D method :",self.d_value)

obj =d("value from B","value from C","value from D")
print("all details of D class : ")


obj.showA()
obj.showB()
obj.showc()
obj.showD()