"""class test:
     def __init__(self,a="Hello World"):
         self.a=a
 
     def display(self):
         print(self.a)

obj=test("harshil")
obj.display()
"""
"""class Student:
  def __init__(self):
    self.id=1
    self.age=20
    print("hello harshil are you busy ???")

std=Student()
"""

"""class A():
    def __init__(self,count=100):
        self.count=count
obj1=A()
obj2=A(1000)
print(obj1.count)
"""

"""class A:
   def __init__(self,num):
      num=3
      self.num=num
   def change(self):
      self.num=7
a=A()
print(a.num)
a.change()
print(a.num)
"""

"""class Point:
   
    def __init__(self):
        self.x = 0
        self.y = 0
p = Point()         
q = Point()         
print(p.x)
print(q)
print(p.x is q.y)
"""
"""class Employee:
    empcount=0
    def __init__(self,name):
        self.name=name
        self.empcount+=1
    def display_count_emp(self):
        print("There are",self.empcount,"employees")

emp1=Employee("s1")
emp2=Employee("h1")
emp3=Employee("s1")
emp2.display_count_emp()
emp1.display_count_emp()
"""

"""class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        super().__init__()
        self.y = 1
def main():
     b = Derived_Test()
     print(b.x,b.y)
main()
"""

# abstraction  : 
"""
abstraction means  hiding the detalis and showing only the  essential features of an object.

ABC : ==> abstract base class   ==> from abc import ABC 
method  ==>@abstractmethod  
"""
from abc import ABC,abstractmethod
"""
class vehicle(ABC):
    # start stop ==> pass  
    @abstractmethod
    def start(self):  #
        pass 
    
    @abstractmethod
    def stop(self):
        pass 
    
class car(vehicle):
    def start(self):  # over ride
        print("car started")
    
    def stop(self):
        print("car stopped")
        
class bike(vehicle):
    def start(self):
        print("bike started")
    
    def stop(self):
        print("bike stopped")

b=bike()
c=car()
b.start()
b.stop()

c.start()
c.stop()
"""
"""
Abstraction hides the complex implementation (how a vehicle starts or stops) and shows only what actions can be performed.
"""

# using  constructor  : 

class vehicle (ABC):
    def __init__(self,name,model):
        self.name=name
        self.model=model
    
    @abstractmethod
    def start(self):
        pass 
    
    @abstractmethod
    def display(self):
        pass 
    
class car(vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)
        
    def start(self):
        print("car started")
    
    def display(self):
        print("car model is",self.model)
        print("car name is",self.name)

class bike(vehicle):
    def __init__(self, name, model):
        super().__init__(name, model)
    
    def start(self):
        print("bike started")
    
    def display(self):
        print("bike model is",self.model)
        print("bike name is",self.name)
        

c=car("BMW","M 4")
c.start()
c.display()

b=bike("yamaha","R-one5")
b.start()
b.display()
