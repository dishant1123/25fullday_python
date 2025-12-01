# tkinter : GUI  
import  tkinter as tk 

"""root = tk.Tk()
root.title("Royal")
root.geometry("500x500")
root.config(bg="lightblue")
"""
# button  : 
"""button =tk.Button(root,text="click me").pack()
button =tk.Button(root,text="exit").pack(side="left")
"""

"""label = tk.Label(root,text ="hello",font=("times",20),bg="yellow").pack()
name_box =tk.Entry(root,width=50).pack()
root.mainloop()
"""

"""root = tk.Tk()
root.title("print name")
root.geometry("400x300")

# label  : 
label = tk.Label(root, text="enter the name :",font=("times",20),bg="yellow").pack()
name_box = tk.Entry(root, width =50)
name_box.pack(pady=10)
# function  to print name  : 

def print_name():
    name =name_box.get()
    print("your name is :",name)  # terminal  
    output_label=tk.Label(root,text=f"your name is : {name}").pack()  # GUI

# button  : 

btn = tk.Button(root,text="frist name",font=("times",18),command=print_name).pack(pady=10)

root.mainloop()

"""

