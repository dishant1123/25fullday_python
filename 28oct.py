# menu  driven  program using inheritance : 
# single  multi ple  multi level 
"""
emp  manag  system :    
"""

class person : 
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    
    def show_person(self):
        print(f"name : {self.name} , age : {self.age} , gender : {self.gender}")

# hirechy  inheritance : multiple derived class inherit  from  same base class 
class employess(person):
    def __init__(self, name, age, gender,emp_id,salary,dept):
        super().__init__(name, age, gender)
        self.emp_id=emp_id
        self.salary =salary 
        self.dept=dept 
    
    def show_employess(self):
        print(f"emp id : {self.emp_id} , salary : {self.salary} , dept : {self.dept}")
        self.show_person()

class student(person):
    def __init__(self, name, age, gender,rollno,course):
        super().__init__(name, age, gender)
        self.rollno=rollno
        self.course=course
    
    def show_student(self):
        print(f"rollno : {self.rollno} , course : {self.course}")
        self.show_person()
        
class manager(employess):
    def __init__(self, name, age, gender, emp_id, salary, dept,size):
        super().__init__(name, age, gender, emp_id, salary, dept)
        self.size=size
    
    def show_manager(self):
        print(f"size : {self.size}")
        self.show_employess()
# multi ple  : inherit  from  both  emp  , student 
class intern(employess,student):
    def __init__(self, name, age, gender, emp_id, salary, dept,rollno,course,duration):
        employess.__init__(self,name, age, gender, emp_id, salary, dept)
        student.__init__(self,name,age,gender,rollno,course)
        self.duration=duration
    
    def show_intern(self):
        print(f"duration : {self.duration}")
        self.show_person()
        print(f"student rollno : {self.rollno} , course : {self.course}")
        print(f"employess emp id : {self.emp_id} , salary : {self.salary} , dept : {self.dept}")

class employee_management_system:
    
    def __init__(self):
        self.emp_list = [] 
        
    def add_emp(self):
        print(":::::add emp :::::")
        id =int(input("enter emp id : "))
        name =input("enter name : ")
        age=int(input("enter  age : "))
        gender=input("enter gender :")
        salary =int(input("enter salary : "))
        dept =input("enter dept : ")
        emp =employess(name,age,gender,id,salary,dept)
        self.emp_list.append(emp)