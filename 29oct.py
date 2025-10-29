# encapsulation  : 
"""
use ==> private data member  directly  access  

1. get method  :data  print   
2. set  method : new value  set 
"""
 
# without using encap : 
"""
class person : 
    def __init__(self):
        self.__name = "saumya"   # private  data member 
        self.__age = 21

    def show(self):
        print(f"name : {self.__name} , age : {self.__age}")
p=person()
# print(p.__name)  # not  accessible bcz  of private  data member
p.show()
"""

# with using encap :

class person : 
    def __init__(self):
        self.__name = "saumya"   # private  data member
        self.__age=20 
        
    # def get_name(self):
    #     return self.__name 

    # def get_age(self):
    #     return self.__age 
    
    # def set_name(self,new_name):
    #     self.__name = new_name  
        
    # def set_age(self,new_age):
    #     self.__age = new_age
p=person()
# print("without using  set method")

# print(p.get_name())        
# print(p.get_age())

# print("using set method")

# p.set_name("shalin")  # __name = shalin 
# p.set_age(21)  # __age = 21

# print(p.get_name())        
# print(p.get_age())


print(getattr(p,"_person__name"))  # _class__private name   
print(getattr(p,"_person__age"))   # 
setattr(p,"name","shalin")
setattr(p,"age",21)
print(getattr(p,"name"))
print(getattr(p,"age"))
