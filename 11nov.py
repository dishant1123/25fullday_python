"""class Demo:
    def __init__(self):
        self.x = 0
    def change(self):
        self.x = 10
        
class Demo_derived(Demo):
    
    def change(self):
        super().change()
        self.x=self.x+1
        print(self.x)
obj = Demo_derived()
obj.change()
"""

class Demo:
    def check(self):
        return " Demo's check "  
    def display(self):
        print(self.check())

class Demo_Derived(Demo):
    def check(self):
        return " Derived's check "
a =Demo()
a.display()
b= Demo_Derived()
b.display()