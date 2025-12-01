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
    def delete_student():
    
    @staticmethod 
    def search_student():
        
    
            

 