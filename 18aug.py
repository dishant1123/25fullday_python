"""
task  :  ask user to  enter the number and store in to the list .

input  5 = 1 2 3 4 5 

l1=[1,2,3,4,5]
"""

"""n=int(input("enter the number :"))
l1=[]
for i in range(n):
    element =int(input("enter the  element : "))
    l1.append(element)
print(l1)
# output : l1 =[1,2,3,4,5]
l2=[]
for  i in  l1 : 
    count =0 
    for j in range(1,i+1):
        if i % j ==0 :
            count +=1 
    if count ==2 : 
        l2.append(i)
print(l2)
"""

"""task  : 5 take list from user append all element in list and print pelindorme num in list 
 
         input : [121 , 131 , 123 ,145 , 789 ]
         output :  [121,131]
"""

l1= [121,131,123,145,789]
# l2=[]
# for i  in l1 : 
#     if str(i) == str(i)[: : -1]:  # "123" == "321" 
#         l2.append(i)
# print(l2)
l2=[]
for i in l1 :
    temp = i 
    rev =0 
    while temp >0 : 
        r = temp %10 
        rev = rev *10 +r 
        temp =  temp //10 
    if rev ==i :
        l2.append(i)
print(l2)