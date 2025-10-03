# multiple  inheritance :

"""
class a    # base  class 

class b    # base class 

class c (a,b)  # derived class  ==> two base class ==> inherit
"""

"""class vehicle : 
    def __init__(self):
        self.name ="four wheeler"
        self.capacity_of_seating=5
class car :
    def __init__(self):
        self.model ="m-4"
class owner(vehicle,car):
    def __init__(self):
        super().__init__()   # base class constructor  called 
        # vehicle.__init__(self)
        car.__init__(self)
    def display(self,name):
        print("vehicle name is  :",self.name)
        print("capacity of seating is  :",self.capacity_of_seating)
        print("model is  :",self.model)
        print("owner name is  :",name)

o=owner()
o.display("harshil")
"""

# multi level inheritance  : 
"""
class a : 

class b(a):  ==> b  inherit  a

class c(b)  ==> c  inherit  b  inherit  a
"""

class person :
    def show(self):
        print("person class")

class employee(person):
    def show1(self):
        print("employee class")

class manager(employee):
    def show2(self):
        print("manager class")
        
m=manager()
m.show()   #==> person  
m.show1()  #==> employee
m.show2()  #==> manager

e=employee()
e.show()   #==> person
e.show1()  #==> employee

