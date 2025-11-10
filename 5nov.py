# task :1 

# disarium number  : 
"""
for i in range(1,101):
    temp =i    # 1
    digits = str(temp)  # str 
    length = len(digits)  # len ==> int  
    sum =0 
    while temp >0 :
        r = temp %10 
        sum = sum + r ** length  
        temp = temp //10 
        length = length -1 
        
    if sum == i :
        print(i,end=" ")"""
        
        
# 5. output  ? 

"""class A:
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        super().__init__()
        print("B")

B()
"""

# 7. What is the output?
"""class Base:
    def __init__(self):
        self.value = 100

class Derived(Base):
    def __init__(self):
        super().__init__()
        self.value += 50

d = Derived()
print(d.value)"""

# 9. What is the output ?
"""class A:
    def display1(self): 
        print("A")
class B(A):
    def display(self):
         
        print("B")
        
class C(A):
    def display(self): 
        print("C")
class D(C,B):
    pass

D().display()
"""
"""class A:
    def __init__(self):
        print("A")
class B(A):
    def __init__(self):
        print("B")
        super().__init__()
class C(A):
    def __init__(self):
        print("C")
        super().__init__()
class D(B, C):
    def __init__(self):
        print("D")
        super().__init__()
D()"""
"""
a. D B A   ==> s ,p ,v, s h 
b. D B C A 
c. D C B A 
d. D A B C
"""

class test: 
    def show(self):
        return super().show()

test().show()