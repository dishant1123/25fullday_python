# encapsulation  : 
"""
1. get method : data print
2. set method : new value set 
"""

"""class person : 
    def __init__(self):
        self.__name ="het"
        self.__age =26 
        
    def show(self):
        print(f"name: {self.__name}")
        print(f"age: {self.__age}")
p=person()
p.show()
# print(p.__name)  # object though print
# print(p.__age)

p.__name ="chandan"
p.__age =25
p.show()
"""

# encapsulation  :

class employee :
    def __init__(self):
        self.__name ="het"
        self.__age =26
        self.__salary =80000 
        
    def get_print(self):
        print("name :",self.__name,"age :",self.__age,"salary: ",self.__salary)
    
    def set_salary(self,new_salary,new_name,new_age): 
        self.__salary = new_salary
        self.__name = new_name
        self.__age = new_age
e=employee()
print("before using set")
e.get_print()
e.set_salary(89000,"chandan",25)
print("after using set")    
e.get_print()




  
