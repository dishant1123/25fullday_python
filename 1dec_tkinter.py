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
        return f"{self.rollno} ,{self.name},{self.marks}\n"
        
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
    def add_student(s):
        with  open(filemanager.FILE,"a") as f :
            f.write(s.display())
    
    @staticmethod 
    def delete_student(rollno):
        data = filemanager.read_all()  #rollno  name age 
        new_data=[] 
        for  i in data : 
            first_value = i.strip().split(" ")[0]  # rollno 
            if int(first_value) !=int(rollno) :
                new_data.append(i)
        filemanager.write_all(new_data)
    
    @staticmethod 
    def search_student(rollno):
        data = filemanager.read_all()  #rollno  name age 
        for  i in data : 
            r,name,marks =i.strip().split(",")
            if int(r)== int(rollno) :
                return i 
        return None 
    @staticmethod
    def update_student(s):
        data = filemanager.read_all()
        updated = []

        for line in data:
            r = line.strip().split(",")[0]
            if int(r) == s.rollno:
                updated.append(s.display())   # Replace old data
            else:
                updated.append(line)

        filemanager.write_all(updated)
        
class student_GUI :
    def __init__(self,root):
        self.root = root
        self.root.title("Student Management System with CRUD")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

        tk.Label(root, text="Student Management System", font=("Arial", 16, "bold")).pack(pady=10)

        tk.Label(root, text="Roll No:", font=("Arial", 12)).place(x=40, y=70)
        tk.Label(root, text="Name:", font=("Arial", 12)).place(x=40, y=110)
        tk.Label(root, text="Marks:", font=("Arial", 12)).place(x=40, y=150)

        self.roll_entry = tk.Entry(root, width=25)
        self.roll_entry.place(x=150, y=72)

        self.name_entry = tk.Entry(root, width=25)
        self.name_entry.place(x=150, y=112)

        self.marks_entry = tk.Entry(root, width=25)
        self.marks_entry.place(x=150, y=152)

        tk.Button(root, text="Add Student", width=18, bg="#62AB65", fg="white",
                  command=self.add_student).place(x=30, y=200)

        tk.Button(root, text="Search Student", width=18, bg="#A773B0", fg="white",
                  command=self.search_student).place(x=240, y=200)

        tk.Button(root, text="Update Student", width=18, bg="#FF9800", fg="white",
                  command=self.update_student).place(x=30, y=250)

        tk.Button(root, text="Delete Student", width=18, bg="#F44336", fg="white",
                  command=self.delete_student).place(x=240, y=250)

        tk.Button(root, text="View All Students", width=18, bg="#2196F3", fg="white",
                  command=self.view_students).place(x=135, y=300)
    
    def add_student(self) : 
        try : 
            roll =int(self.roll_entry.get())
            name =self.name_entry.get()
            marks=int(self.marks_entry.get())
            
            s=student(roll,name,marks)
            filemanager.add_student(s)
            messagebox.showinfo("success","student added successfully")
            self.clear_fields()
        except ValueError :
            messagebox.showerror("error","please enter valid input")

    def update_student(self):
        try:
            roll =int(self.roll_entry.get())
            name=self.name_entry.get()
            marks=int(self.marks_entry.get())
            
            if filemanager.search_student(roll):
                s=student(roll,name,marks)
                filemanager.update_student(s)
                messagebox.showinfo("success","student updated successfully")
            else :
                messagebox.showerror("error","student not found")
        except ValueError :
            messagebox.showerror("error","please enter valid input")
            
    def delete_student(self):
        try: 
            roll =int(self.roll_entry.get())
            if filemanager.search_student(roll):
                filemanager.delete_student(roll)
                messagebox.showinfo("success","student deleted successfully")
            else :
                messagebox.showerror("error","student not found")
        except ValueError :
            messagebox.showerror("error","please enter valid input")
            
    def search_student(self):
        try :
            roll=int(self.roll_entry.get())
            result = filemanager.search_student(roll)
            
            if result :
                r,name ,marks =result.strip().split(",")
                messagebox.showinfo("student found",f"name : {name} marks : {marks}, rollno : {roll}")
            else :
                messagebox.showerror("error","student not found")
        except ValueError :
            messagebox.showerror("error","please enter valid input")
    
    def view_students(self):
        win = tk.Toplevel(self.root)
        win.title("all students information display")
        win.geometry("480x450")
        tk_area = tk.Text(win, height=20, width=40)
        tk_area.pack(fill=tk.BOTH,expand=True)
        
        data =filemanager.read_all()
        if data :
            for i in data :
                tk_area.insert(tk.END,i)
        else :
            tk_area.insert(tk.END,"no student found")
            
    def clear_fields(self):
        self.roll_entry.delete(0,tk.END)
        self.name_entry.delete(0,tk.END)
        self.marks_entry.delete(0,tk.END)

root = tk.Tk()
s=student_GUI(root)
root.mainloop()
            
    