import  tkinter  as tk 
from tkinter import ttk 

root =tk.Tk()
root.title("CALCULATOR")
root.geometry("500x500")
root.config(bg="lightblue")

# input  1 : 

tk.Label(root,text="enter the first number  :",font=("times",20)).pack(pady=10)
a_box =tk.Entry(root,width=50)
a_box.pack()

#input  2 : 
tk.Label(root,text="enter the second number  :",font=("times",20)).pack(pady=10)
b_box =tk.Entry(root,width=50)
b_box.pack()

# list  operation  list : 
operation = [
    "1. addition",
    "2. subtraction",
    "3. multiplication",
    "4. division",
    "5. modulus",
    "6. floor division"
]

op_box =ttk.Combobox(root,values=operation,width=50)
op_box.current(0)   # index number  : add index =0 sub 1 
op_box.pack(pady=5)

result_label = tk.Label(root,text="result",font=("times",20))
result_label.pack(pady=10)

# match  operation  :
def calculator():
    a= int(a_box.get())
    b=int(b_box.get())
    
    choice = op_box.current() +1 
    match choice:
        case 1 :
            result =a+b
        case 2 :
            result =a-b
        case 3 :
            result =a*b
        case 4 :
            result =a/b
        case 5 :
            result =a%b
        case 6 :
            result =a//b
        case _:
            result ="invalid operation"
    result_label.config(text=result)
    
tk.Button(root,text="calculate",font=("times",18),command=calculator).pack(pady=10)
root.mainloop()\

#task:1 modify 
#task :2 reg forms   ::

"""
1.name  
2. age  
3. email  
4. phone 
5. address 
"""  
