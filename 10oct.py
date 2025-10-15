"""a = [1, 2, 3]
b=a    # shallow copy
b = a.copy()  # deep  copy 
b.append(4)
print(a)
print(b)
"""
"""a={"1":2} + {3:4}
print(a)
"""

"""_ = '1 2 3 4 5 6' 
print(_) 
"""
# print(print(print("python")))

"""if "4" + 5 == 10:
       print("TRUE")
else: 
      print("FALSE")
print("TRUE")

"""

"""a= [1,2,3,4]

print(a.pop(2))  # 3 
print(a)
"""

"""a = [1, 2, 3]
print(a.insert(1, 100))
print(a)
"""

"""d = {}
d[1] = 'a'
d[False] = 'b'
print(d)
"""

"""for i in range(0,1,-1):
      print("Hello")
"""
"""a = {1, 2, 3}
b = {2, 3, 4}
print(a or b)  # union ==>1 2 3 4 
"""
"""s = set([1, 2 ,3, 4],[11,12])
print(s)
"""

"""for i in range(10):
    if i == 5:
        pass 
    else:
            print(i)
else:
      print("Here")  
"""

"""
Write a python program that prompts the user to enter numbers and stops only when the use enter “QUIT” . After this 
print sum  and average of the numbers, minimum and maximum number from given numbers entered by user.
 Note: you are not allowed to use any built in structures like, list ,tuple etc. or any  builtin function like min, max  etc.
 For 
 Example:  Input:  4,1,5,”QUIT”
 Output:
 Sum=10
 Average=3.333
 Minimum number=1
 Maximum number=5
"""

#
"""
Write a program that enters a single digit integer number and produces all possible 6-digit numbers for which the product 
of their digits is equal to the entered number.
 Example: "number" → 2   
 •111112 → 1 * 1 * 1 * 1 * 1 * 2 = 2
 •111121 → 1 * 1 * 1 * 1 * 2 * 1 = 2
 •111211 → 1 * 1 * 1 * 2 * 1 * 1 = 2
 •112111 → 1 * 1 * 2 * 1 * 1 * 1 = 2
 •121111 → 1 * 2 * 1 * 1 * 1 * 1 = 2
 •211111 → 2 * 1 * 1 * 1 * 1 * 1 = 2
"""

"""
*               * 
* *           * *  
* * *       * * *
* * * *   * * * *
* * * * * * * * *
* * * *   * * * *
* * *       * * *
* *           * *
*               *
"""
"""num =int(input("enter the number  : "))  # 2
for i in range(100000 ,1000000) :
    mul =1 
    
    temp =i 
    while temp > 0 :
        r = temp %10 
        mul = mul *r 
        temp  = temp //10 
    if mul ==num:
        print(i)
"""
