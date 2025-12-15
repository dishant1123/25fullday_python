import tkinter as tk 


root =tk.Tk()
root.title("Royal")
root.geometry("500x500")

# root.config(bg="yellow")

# button= tk.Button(root,text="Click me").pack()
# button =tk.Button(root,text ="ok").grid(row=0,column=1)
# button =tk.Button(root,text ="exit").grid(row=0,column=0)

# button =tk.Button(root, text="Submit").place(x=100, y=150)

# root.mainloop()
"""label =tk.Label(root,text="enter the  name :",font=("times",20),bg="yellow").pack()
name_box =tk.Entry(root,width=50).pack()
root.mainloop()
"""
import tkinter as tk

"""root = tk.Tk()
root.title("Name Input")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your name :", font=("Times", 20), bg="yellow")
label.pack(pady=10)

# Entry Box
name_box = tk.Entry(root, width=40, font=("Times", 16))
name_box.pack(pady=10)

# Function to print name
def print_name():
    name = name_box.get()
    print("Your Name is:", name)      # Print in terminal
    output_label.config(text=f"Your Name is: {name}")  # Print on GUI

# Button
btn = tk.Button(root, text="Print Name", font=("Times", 18), command=print_name)
btn.pack(pady=10)

# Output label
output_label = tk.Label(root, text="", font=("Times", 20), fg="blue")
output_label.pack(pady=10)

root.mainloop()
"""

label = tk.Label(root, text="Hello")
label.pack()
label.pack(side="left")
label.pack(side="right")
label.pack(side="top")
label.pack(side="bottom")
root.mainloop()
