# perfect : 
"""
n=int(input("enter the number  : "))
sum =0 

for i in range(1,n): # 5,6
    if n % i ==0 :    # 6 %5 ==0  
        sum =sum +i   # sum =6
if sum ==n :
    print("perfect number")
"""
# amg : 
"""
153 : 3 
1**3 5 **3  3**3  =1 +125 +27 =153 

1634 :4 
    1**4  6**4 3**4   4**4  =1+ 1296 +81 +256 =1634 

52748  : 5

#include<math.h>
count =0
while num >0 :  0 > 0 
    num //10   1 //10 =0 
    count +=1     count =4 

while temp >0 :  0 >0 
    r = temp %10   r = 1 %10 =1 
    sum =sum + pow(r,count)   sum = 1634
    temp = temp //10      temp =1 //10 =0 
"""

"""n=int(input("enter the number  : "))
sum =0 
digit =len(str(n))  #4 
temp= n 
for  i in range(digit): # 
    r = temp %10 
    sum =sum + pow(r,digit)
    temp = temp //10 
if sum==n:
    print("amg")
"""

# twin  : 
"""
123 : 
each digit sum  : 1+2+3 =6 
each multiply = 1*2*3 =6 

22 :
"""
"""n=int(input("enter the number  : "))
digit =len(str(n))
sum =0 
mul =1 
for i in range(digit): # 0,3
    r = n %10       # 1 %10 =1 
    sum =sum +r   # sum  =6 
    mul =mul *r   # mul =6 *1 =6
    n =n //10     # 1 //10=0
if sum==mul:
    print("twin")
"""

# pelindrome  : 
"""
r = n %10 
rev = rev *10 +r 
temp = temp //10 
"""

# nested loop  : 

"""
ask user to enter the starting  number  and  ending number  print  prime  between  the  two  numbers.  
start =10   end =90 
"""
"""
start =int(input("enter the starting  number  : "))
end =int(input("enter the ending  number  : "))

for i in range(start ,end +1) :   # start  : 11  end : 90 
    count =0 
    for j in range(1,i+1) :
        if i % j==0 :
            count +=1 
    if count ==2 :
        print(i,end=" ")
"""

# perfect twin amg pelindorme :

"""start =int(input("enter the starting  number  : "))
end =int(input("enter the ending  number  : "))

for i in range(start ,end +1) :   # start  : 100  end : 90000
    sum =0 
    digit = len(str(i))
    temp =i
    for j in range(digit):
        r = temp %10 
        sum =sum + pow(r,digit)
        temp  = temp //10 
    if sum ==i :
        print(i,end=" ")

"""
# pattern : 
"""
1.         2.            3.            4 .         5.            6. 
        
* * * * *  *             * * * * *    1             5 4 3 2 1     1 2 3 4 5 
* * * * *  * *           * * * *      1 2           5 4 3 2       2 3 4 5
* * * * *  * * *         * * *        1 2 3         5 4 3         3 4 5
* * * * *  * * * *       * *          1 2 3 4       5 4           4 5 
* * * * *  * * * * *     *            1 2 3 4 5     5             5

7.                8.             9.        10 .         11.            

* * * * *     * * * * *           *         *             * 
  * * * *      * * * *          * *        * *           * *
    * * *       * * *         * * *       * * *         * * * 
      * *        * *        * * * *      * * * *       * * * *
        *         *       * * * * *     * * * * *     * * * * *
                                                       * * * *
                                                        * * *
                                                         * *
                                                          *
"""
"""
for (i=5; i>0; i--)
    for(j=0; j<i; j++)
        printf("*")
    printf("\n")
"""
# 1: 

"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()
"""

# 2 : 
"""
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#3 : 
"""
for i in range(6,0,-1):
    for j in range(1,i):
        print("*",end=" ")
    print()
"""

# 7 : 
"""
for i in range(1,6):
    for k in range(1,i):
        print(" ",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
# 8 : 
"""
for i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

# 9: 
"""for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
# 10 : 
"""
for i in range(1,6):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#11 : 
"""for i in range(1,5):
    for k in range(5,i,-1):
        print(" ",end="")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i in range(1,6):
    for k in range(1,i):
        print(" ",end="")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""