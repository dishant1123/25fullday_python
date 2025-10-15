# *arg  : num arg   

"""def d(*args):
    return sum(args)  # sum ==> built in function . 

result =d(1,2,3,4,5,6,7,8,9,12.45)
print(result)
print(type(result)) 
"""

# **kwargs : dict  , key value  

"""def d1(**kwargs):
    for i ,j in kwargs.items():
        print(f"{i} :{j}") 
d1(name="sachin", age=24, city="pune")
"""
# default arg  : 

"""def d2(a,b=34,c=45):
    return a+b+c
print(d2())
"""
# print(d2(12))
# print(d2(1,2,3))
# print(d2(12,10))

# v 91 6  67   s no output    o 91 40 67  h      h     d       s
"""value="global"
def func():
   global value
   value = "Local"  
value = "Global"
func()
print(value)
"""
"""def function1(var1=5, var2=7):
    var2=9
    var1=3
    print (var1, " ", var2)
function1(10,12)
"""
"""
def fun1(num):
    return num + 25
fun1(5)
print(num)
"""
"""
recursion function  : 

c : 
int facto(int  n)  # 5 
{
    if (n==1) 
        return 1;
    else 
        return n * facto(n-1);  # recursive 
    
}
int main()
{
    printf("%d",facto(5);
}

factorial maths  : 

n! = n * (n-1)! 
"""