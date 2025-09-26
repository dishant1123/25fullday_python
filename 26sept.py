# oop  :  object oriented programming
"""
class  object : 

class : class is template of  object
object : is instance  of  class  

fruits ==>class 
                apple kiwi banana mango chiku  ==> object ==> fruits 

type  : 

1.  public 
2.  private
3.  protected
"""

# ex :1
"""class student :   # student ==>is  class  name 
    def remo(self): # remo ==>  function  :  self keyword ==>function , constructor  ==> access    
        print("good dancer.")
    
    def shalin(self): 
        print("good listener.")

s=student()  # s object  == >student class 
# s.remo()
# s.shalin()
student().remo()
"""

# ex :2 
"""
class vehicle : 
    print("vehicle class")
    print("four wheeler and  two wheeler")

v=vehicle()
"""

# ex :3 

"""class employee :
    def staff(self):
        return "50 staff in my company"
    
    def salary(self):
        return "salary is 100000"

e=employee()
print(e.staff())
print(e.salary())
"""

# ex :4 

"""class employee :
    def staff(self):
        return "50 staff in my company"

    def staff(self):
        return "5000 staff in my company"

e=employee()
print(e.staff())  # overwrite  the  first function  always call  second function  if  same  name of  function. 
"""

# ex :5 

class student : 
    name ="purva"   # name  , age  city  clg ==> class data member 
    age =20 
    city ="ahemadabad"
    clg ="LJ"
    
    def show(self):
        print("name  is :",self.name)
        print("age  is :",self.age)
        print("city  is :",self.city)
        print("clg  is :",self.clg)
   
s=student()
# print("name is ",s.name)
# print("age is ",s.age)
# print("city is ",s.city)
# print("clg is ",s.clg)
s.show()
s.name="harshil"
s.age =22 
s.city="gandhinagar"
s.clg="PDU"
s.show()
