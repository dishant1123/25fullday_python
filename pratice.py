import tkinter as tk
from tkinter import messagebox
class Student:
    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks
    def to_string(self):
        return f"{self.roll},{self.name},{self.marks}\n"
class FileManager:
    FILE = "students_db.txt"
    @staticmethod
    def read_all():
        try:
            with open(FileManager.FILE, "r") as f:
                return f.readlines()
        except FileNotFoundError:
            return []
    @staticmethod
    def write_all(lines):
        with open(FileManager.FILE, "w") as f:
            f.writelines(lines)
    @staticmethod
    def add_student(student):
        with open(FileManager.FILE, "a") as f:
            f.write(student.to_string())
    @staticmethod
    def search_student(roll):
        data = FileManager.read_all()
        for line in data:
            r, name, marks = line.strip().split(",")
            if r == str(roll):
                return line
        return None
    @staticmethod
    def delete_student(roll):
        data = FileManager.read_all()
        new_data =[]
        for line in data:
            first_value = line.split(",")[0]   # get roll number from line
        if first_value != str(roll):       # keep only other roll numbers
            new_data.append(line)        
        FileManager.write_all(new_data)
    @staticmethod
    def update_student(student):
        data = FileManager.read_all()
        new_data = []
        for line in data:
            r, _, _ = line.strip().split(",")
            if r == str(student.roll):
                new_data.append(student.to_string())  # update
            else:
                new_data.append(line)
        FileManager.write_all(new_data)
class StudentGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System with CRUD")
        self.root.geometry("480x450")
        self.root.resizable(False, False)

        tk.Label(root, text="Student Management System", font=("Arial", 16, "bold")).pack(pady=10)

        # Labels
        tk.Label(root, text="Roll No:", font=("Arial", 12)).place(x=40, y=70)
        tk.Label(root, text="Name:", font=("Arial", 12)).place(x=40, y=110)
        tk.Label(root, text="Marks:", font=("Arial", 12)).place(x=40, y=150)

        # Entry
        self.roll_entry = tk.Entry(root, width=25)
        self.roll_entry.place(x=150, y=72)

        self.name_entry = tk.Entry(root, width=25)
        self.name_entry.place(x=150, y=112)

        self.marks_entry = tk.Entry(root, width=25)
        self.marks_entry.place(x=150, y=152)

        # Buttons
        tk.Button(root, text="Add Student", width=18, bg="#4CAF50", fg="white",
                  command=self.add_student).place(x=30, y=200)

        tk.Button(root, text="Search Student", width=18, bg="#9C27B0", fg="white",
                  command=self.search_student).place(x=240, y=200)

        tk.Button(root, text="Update Student", width=18, bg="#FF9800", fg="white",
                  command=self.update_student).place(x=30, y=250)

        tk.Button(root, text="Delete Student", width=18, bg="#F44336", fg="white",
                  command=self.delete_student).place(x=240, y=250)

        tk.Button(root, text="View All Students", width=18, bg="#2196F3", fg="white",
                  command=self.view_students).place(x=135, y=300)


    def add_student(self):
        try:
            roll = int(self.roll_entry.get())
            name = self.name_entry.get()
            marks = float(self.marks_entry.get())

            s = Student(roll, name, marks)
            FileManager.add_student(s)

            messagebox.showinfo("Success", "Student added successfully!")
            self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid input! Check roll and marks.")

    def search_student(self):
        try:
            roll = int(self.roll_entry.get())
            result = FileManager.search_student(roll)

            if result:
                r, name, marks = result.split(",")
                messagebox.showinfo("Student Found", f"Roll: {r}\nName: {name}\nMarks: {marks}")
            else:
                messagebox.showwarning("Not Found", "Student not found!")

        except ValueError:
            messagebox.showerror("Error", "Enter a valid roll number!")

    def update_student(self):
        try:
            roll = int(self.roll_entry.get())
            name = self.name_entry.get()
            marks = float(self.marks_entry.get())

            s = Student(roll, name, marks)
            if FileManager.search_student(roll):
                FileManager.update_student(s)
                messagebox.showinfo("Updated", "Student updated successfully!")
            else:
                messagebox.showwarning("Not Found", "Roll number not found!")

            self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Invalid input!")

    def delete_student(self):
        try:
            roll = int(self.roll_entry.get())
            if FileManager.search_student(roll):
                FileManager.delete_student(roll)
                messagebox.showinfo("Deleted", "Student deleted successfully!")
            else:
                messagebox.showwarning("Not Found", "Roll number not found!")

            self.clear_fields()

        except ValueError:
            messagebox.showerror("Error", "Enter a valid roll number!")

    def view_students(self):
        win = tk.Toplevel(self.root)
        win.title("All Students")
        win.geometry("400x350")

        text_area = tk.Text(win, wrap=tk.WORD)
        text_area.pack(expand=True, fill=tk.BOTH)

        data = FileManager.read_all()
        if data:
            for line in data:
                text_area.insert(tk.END, line)
        else:
            text_area.insert(tk.END, "No student records found...")

    def clear_fields(self):
        self.roll_entry.delete(0, tk.END)
        self.name_entry.delete(0, tk.END)
        self.marks_entry.delete(0, tk.END)


root = tk.Tk()
app = StudentGUI(root)
root.mainloop()


