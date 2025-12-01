# add update delete serach   ==> function  
"""
class object : 
"""
import tkinter  as tk 
from tkinter import messagebox 

class student :
    def __init__(self,rollno,name,marks):
        self.rollno = rollno
        self.name=name 
        self.marks=marks
    
    def display(self):
        print(f"rollno :{self.rollno} name:{self.name} marks:{self.marks}")
        
class filemanager : 
    FILE ="25_fullday.txt"
    
    @staticmethod 
    def read_all():
        try :
            with open(filemanager.FILE,"r") as f :
                return f.readlines() 
        except FileNotFoundError:
            return [] 
    @staticmethod 
    def write_all(lines):
        with open(filemanager.FILE,"w") as f :
            f.writelines(lines)
            # (["my name is saumya.\n","my age is 20.\n","study in royal"])
    @staticmethod 
    def add_student():
        with  open(filemanager.FILE,"a") as f :
            f.write(student.display())
    
    @staticmethod 
    def delete_student(rollno):
        data = filemanager.read_all()  #rollno  name age 
        new_data=[] 
        for  i in data : 
            first_value = i.split(" ")[0]  # rollno 
            if first_value !=rollno :
                new_data.append(i)
        filemanager.write_all(new_data)
    
    @staticmethod 
    def search_student(rollno):
        data = filemanager.read_all()  #rollno  name age 
        for  i in data : 
            r,name,marks =i.strip().split(",")
            if r== rollno :
                return i 
        return None 
        
class student_GUI :
    def __init__(self,root):
        # self.root  = root , 
        # self.root.title() , self.root.geometry()

        # tk.label ==>rollno , name  , marks 
        
        # entry  :  rollno name  marks 
        
        # button  : command ==>self.add_student()
        """
        4 . button  ==> add student , update student, delete student , search student 
        """
    
    def add_student(self) : 
        