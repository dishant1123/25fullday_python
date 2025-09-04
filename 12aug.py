"""
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
#1 : 
"""
for i  in range(1,6):
    for k in range(1,i):
        print("",end="  ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""
#2: 
"""
for i  in range(1,6):
    for k in range(1,i):
        print("",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()
"""

#3: 

"""
for i  in range(1,6):
    for k in range(5,i,-1):
        print("",end="  ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""
#4 : 
"""
for i  in range(1,6):
    for k in range(5,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
"""

"""for i  in range(1,6):
    for k in range(5,i,-1):
        print("",end=" ")
    for j in range(1,i+1):
        print("*",end=" ")
    print()
for i  in range(1,6):
    for k in range(1,i):
        print("",end=" ")
    for j in range(5,i-1,-1):
        print("*",end=" ")
    print()

"""

#  
"""
1. 
* * * * * 
*       *
*       *
*       *
* * * * *
"""

"""
for i in range(1,6):
    for j in range(1,6):
        if i==1 or j==1 or i==5 or j==5 :    
            print("*",end=" ")
        else :
            print(" ",end=" ")
    print()
"""


# while loop : 
"""
syntax : 

i=intial value 
while con :
    statement/print
    inc/dec   ==> i+=1
"""

# while  : 

"""i=1 
while i<=100:
    print(i,end=" ")
    i+=1
"""

# nested while  : 

"""start =int(input("enter the starting  number  : "))
end=int(input("enter the ending number :"))

i=start 

while i<=end:
    count =0 
    j=1 
    while j<=i: 
        if i% j==0 :
            count +=1 
        j+=1
    if count ==2 :
        print(i)
    i+=1 
"""

# while True :

"""
syntax : 

i=intial value
while True:
    statement/print
    inc/dec   ==> i+=1

"""

"""i=1 
while True:
    print(i,end=" ")
    i+=1
    if i==10 :
        break
"""

# match  : 
"""while  True :
    a=int(input("enter the  number  : "))
    b=int(input("enter the  number  : "))
    while True:
        print("1. addition")
        print("2. subtraction")
        print("3. multiplication")
        print("4. division")
        print("5. modulus")
        print("6. floor division")
        choice =int(input("enter the choice : "))

        match choice:
            case 1 :
                print(a+b)
            case 2 :
                print(a-b)
            case 3 :
                print(a*b)
            case 4 :
                print(a/b)
            case 5 :
                print(a%b)
            case 6 :
                print(a//b)
            case 7 :
                break
            case _ :
                print("invalid choice")
"""
# exit 
#

# nested  match : 
print("1.FRUITS")
print("2.VEGETABLES")

choice =int(input("enter the choice : "))
match choice :
    case 1 :
        print("1.APPLE rs :100")
        print("2.KIWI rs :150")
        print("3.ORANGE rs :90")
        subchoice =int(input("enter the subchoice : "))
        match subchoice:
            case 1:
                print("you selected apple ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",100*qty)
            case 2 :
                print("you selected kiwi ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",150*qty)
            case 3 :
                print("you selected orange ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",90*qty)
    case 2:
        print("1.POTATOES rs :60")
        print("2.TOMATO rs :40")
        print("3.METHI rs :10")
        subchoice =int(input("enter the subchoice : "))
        match subchoice:
            case 1:
                print("you selected potatoes ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",60*qty)
            case 2 :
                print("you selected tomato ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",40*qty)
            case 3 :
                print("you selected methi ")
                qty =int(input("enter the quantity : "))
                print("bill is  :",10*qty)