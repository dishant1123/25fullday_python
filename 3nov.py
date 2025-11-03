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

class animal : 
    def sound(self):
        print("animal sound")

class dog(animal):
    def sound(self):  
        print("dog sound")

class cat(animal):
    def sound(self):
        print("cat sound")
        
"""d=dog()
d.sound() 
"""
animal = [dog(), cat()]
for i in animal :
    i.sound()

# sound() ==> in subclass override the  parent class method  ==> this is called run time polymorphism. 