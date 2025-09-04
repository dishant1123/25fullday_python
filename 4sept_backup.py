# while : 

"""
syntax : 

i=intial value 
while con :
    print 
    i +=1 

"""
# 1-100 : 

"""
i=1 
while i <=100 :
    print(i,end=" ")
    i+=1
"""
# while  True :
"""
syntax : 
i=intial value
while  True :
    print 
    i+=1
    if value 
        break 
""" 

# 1-100 :

"""i=1 
while True :
    print(i,end=" ")
    i+=1
    if i==10 :
        break
"""

# match :
"""while True :
    a=int(input("enter the number  1: "))
    b=int(input("enter the number  2: "))
    while True :
        print("WELCOME  MY CALCULATOR")
        print("1.addition")
        print("2.subtraction")
        print("3.multiplication")
        print("4.division")
        print("5.modulus")
        print("6.floor division")

        choice =int(input("enter the choice  : "))
        match choice :
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
                print("new  number : ")
                break
            case 8 :
                print("exit")
"""
# task  :
"""
1. exit () ==> condition 
2. if user enter the 7 then   
""" 

# nested  match : 

"""print("WELCOME MY SHOP ")
print("1.FRUITS")
print("2.VEGETABLES")

choice =int(input("enter the choice  : "))
match choice :
    case 1 :
        print("you selected  FRUITS")
        print("1.APPLE : rs 100")
        print("2.BANANA : rs 50")
        print("3.ORANGE : rs 200")
        subchoice =int(input("enter the subchoice  : "))
        match subchoice :
            case 1 : 
                print("you selected APPLE")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," APPLE and your bill is  : ",qty*100)
            case 2 : 
                print("you selected BANANA")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," BANANA and your bill is  : ",qty*50)
            case 3 :
                print("you selected ORANGE")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," ORANGE and your bill is  : ",qty*200)
    
    case 2 :
        print("you selected VEGETABLES")
        print("1.CARROT : rs 100")
        print("2.POTATO : rs 60")
        print("3.ONION : rs 70")
        subchoice =int(input("enter the subchoice  : "))
        match subchoice :
            case 1 :
                print("you selected CARROT")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," CARROT and your bill is  : ",qty*100)

            case 2:
                print("you selected POTATO")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," POTATO and your bill is  : ",qty*60)
            
            case 3 :
                print("you selected ONION")
                qty =int(input("enter the quantity  : "))
                print("you ordered  ",qty," ONION and your bill is  : ",qty*70)

"""
# hw : selected both item in 1 time  and print  total  bill for fruits  and  vegetables combine. 

# python data type  : 
"""
1. string  :  immutable  ==>  no chages in string . 
2. list : mutable   ==> changes in list 
3. tuple : immutable  ==> no changes in tuple
4 .dictionary : mutable  ==> changes in dictionary 
5. set : mutable  ==> changes in set
"""

# list  : mutable   ==> changes in list

"""
l1 =[1,2,3,4,5,8j ,True ,12.56]

print(l1)
print(type(l1))
"""
# list  element access  thorough index :

l1 =[10,20,30,40,50,8j ,True ,12.56]

# index : start  0 1 2 3 ....   pos ==> l to r 
# neg  index : -1 -2 -3   .... r  to  l   

# print(l1[4])

# list update : 
"""
l1[3] ="vishal"
print(l1)
"""

# python  built  in function  :  len min max sorted sum 
 
"""
l1 =[10,20,30,40,50,8,12.56,True]

print(len(l1))
print(min(l1))
print(max(l1))
print(sorted(l1))  # asc to desc 
print(sum(l1))
"""

# method  : 

l1 =[10,20,30,40,50,8,12.56,10,10]

"""l1.append(800)  # last element add 
print(l1)
"""

"""l1.insert(3,900)  # pos , element  
print(l1)
"""
"""l1.remove(8)   # element remove 
print(l1)
"""
"""l1.pop(4)  # index number 
print(l1)
"""
"""l1.clear()
print(l1)
"""

"""l2 =l1.copy()
print(l2)"""

"""l2=["apple","banana","orange"]
l1.extend(l2)
print(l1)
"""
l1 =[10,20,30,40,50,8,12.56,10,900,10,800]

"""
print(l1.index(12.56))  # element   ==> output  index number print  
print(l1.index(10))
print(l1.index(10,1,12))
l1.index(10,9,11)
"""

"""
l1.sort()
print(l1)

l1.reverse()
print(l1)
"""

# task :1 ask user to enter the  list element  and  store  into the list  and  print  sum . 
"""
n=int(input("enter the number you want  store in list   : "))
l1=[] 

for i in range(n):
    element  =int(input("enter the element  : "))
    l1.append(element)
print(l1) # [1,2,3,4,5]
evesum =0
oddsum=0
for i in l1 : 
    if i %2==0 :
        evesum +=i 
    else :
        oddsum +=i
print("even sum is  : ",evesum)
print("odd sum is  : ",oddsum)
"""
# task :2 ask user to enter the  list element  and  store  into the list  and  print  evensum  and oddsum. 

#task  :3 ask user to enter the  list element  and  store  into the list  and  remove the duplicate element. 
"""
input  : l1 =[1,2,2,3,3,4,4,5,5,6]
output : l1 =[1,2,3,4,5,6]
"""
# n=int(input("enter the number you want  store in list   : "))
# l1=[] 

# for i in range(n):
#     element  =int(input("enter the element  : "))
#     l1.append(element)
# print(l1) # [1,1,3,3,4,5,7,8,8,9]

"""l1 =[1,2,2,3,3,4,4,5,5,6]
l2=[]
for i in l1 : 
    if i not in l2 : 
        l2.append(i)  # l2 =[1,3,]
print(l2)
"""

# l1 =[1,2,3,4,5,6,7,8,9,10 ]
# second  largest  element  : 9

# l1 =[100,20,3,4,5,6,7,8,9,10,900,899]
# index pos :  l to  r   
# neg : r to  l 

n=int(input("enter the number you want  store in list   : "))
l1=[] 

for i in range(n):
    element  =int(input("enter the element  : "))
    l1.append(element)
print(l1) # [1,1,3,3,4,5,7,8,8,9]

l2=sorted(l1)
print(l2)
print("second  largest element  : ",l2[-2])
