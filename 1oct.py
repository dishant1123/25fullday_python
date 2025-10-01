# multiple  inheritance : 
"""
class a : 
class b :
class (a,b):
"""

"""class father :  # base  class 
    def skill(self):
        print("father skill driving")

class mother :  # base class 
    def skill(self):
        print("mother skill cooking")

class child(father,mother):  # derived class  ==> two base class ==> inherit 
    def skill(self):
        super().skill() # MRO:method resolution order
        print("child skill playing")
        
c=child()
c.skill()
"""
# using constructor : 

class student :
    def __init__(self):
        self.name ="Om"
        self.age =20 
        
class teacher :
    def __init__(self):
        self.t_name ="prof. rahul kirpekar"
        self.t_age =35 
        
class clg(student,teacher):
    def __init__(self,c_name):
        self.c_name=c_name
        student.__init__(self)
        teacher.__init__(self)
        
    def display(self):
        print("============CLG INFORMATION===============")
        print("name :",self.c_name)
        print("*********STUDENT INFORMATION*************")
        print("name :",self.name)
        print("age :",self.age)
        print("*********TEACHER INFORMATION*************")
        print("name :",self.t_name)
        print("age :",self.t_age)

c=clg("GLS")
c.display()