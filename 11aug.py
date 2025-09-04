# strong number  : 
"""
145 : 

1 ! = 1 
4!= 24
5 ! =120 

sum = 1+120 +24 =145 
"""

"""
\num =int(input("enter the number  : "))  # 145 
digits = len(str(num))   # 3
sum =0 
temp =num 
for x in range(digits):  # 2,3 
    r =num %10      # r= 1 %10 = 1 
    fact =1 
    for  i in range(1,r+1):
        fact =fact *i   # fact =1 
    sum =sum +fact    # sum =145
    num = num //10    # num =1 //10 =0    
if sum ==temp : 
    print(temp,"is strong number")
"""

# homework : reverse , pelindrome  

# nested loop  :  prime  amg  strong  perfect  twin 

# prime  : 

"""
start =int(input("enter the starting  number  : "))
end =int(input("enter the ending  number  : "))

for  i in range(start,end+1):   # start 11   end 31 
    count=0 
    for j in range(1,i+1): # 1,12 :    num % i ==0 
        if i % j==0 :       # 10 % 10==0 
            count +=1   # count = 2 
    if count ==2 :  # 2==2  
        print(i)  # 11 
"""
"""
r = num %10  
sum =sum  +pow(r,digits)
num = num //10 

"""
# amg : 
"""start =int(input("enter the starting  number  : "))
end =int(input("enter the ending  number  : "))

for i in range(start,end+1):  # 101  ,10001 
    digits =len(str(i))     # 3 
    temp =i     # temp =100 
    sum =0     #sum=0 
    for j in range(digits):  # 2,3 
        r =temp %10     # r = 1 %10  =1 
        sum = sum + pow(r,digits)   # sum =1
        temp = temp //10    # temp =1 //10 =0   
    if sum ==i :  # 1 ==100 
        print(i,end=" ")
"""

# strong number using  nested loop : 

# pattern  : 

"""
1.         2.            3.            4 .         5.            6. 
        
* * * * *  *             * * * * *    1             5 4 3 2 1     1 2 3 4 5 
* * * * *  * *           * * * *      1 2           5 4 3 2       2 3 4 5
* * * * *  * * *         * * *        1 2 3         5 4 3         3 4 5
* * * * *  * * * *       * *          1 2 3 4       5 4           4 5 
* * * * *  * * * * *     *            1 2 3 4 5     5             5

row =5 col = 5 
for(i=0; i<5; i++)
    for(j=5; j>i; j--)
    {
        printf("* ");
    }
    printf("\n")
"""
#1 :
"""
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()
"""

#2 :
"""
for i in range(5):
    for j in range(i+1):
        print("*",end=" ")
    print()
"""

# 3: 
"""for i in range(5):
    for j in range(5,i,-1):
        print("*",end=" ")
    print()

"""

# 8. What is the output of the following for loop and  range() function
# for num in range(-2,-5,-1):
#     print(num, end=", ")

"""
a.-2, -1, -3, -4     ==> 
b.-2, -1, 0, 1, 2, 3, ==> 
c.-2, -1, 0      ==> 
d.-2, -3, -4,   ==> h a d o k n s p d   


"""
# 11. What will be the output of the following Python code?
i = 0
while i < 3:
    print(i)
    i += 1
else:
    print(0)

"""
a. 0 1 2 3 0 
b. 0 1 2 0   ==> d h n n h 
c. 0 1 2
d. error ===> k s p a o
"""

# 13.What will be the output of the following Python code?
"""for i in range(10):
    if i == 5:
        break
    else :
        print(i)
else:
    print("Here")
"""
"""
a. 0 1 2 3 4 Here  ==> p h  k n h  
b. 0 1 2 3 4 5 Here  ==> a o 
c. 0 1 2 3 4   ==>d  s  n  
d. 1 2 3 4 5   

"""