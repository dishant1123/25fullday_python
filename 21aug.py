# matrix  : 

#c : 
"""
int a[3][3] 
"""

"""
l1= [[1,2,3],
     [4,5,6] ,
     [7,8,9]]

for  i in l1:
    print(i)
"""

l1= [[1,2,3],
     [4,5,6],
     [7,8,9]]

"""
r c 
(0,0)1 (0,1)2 (0,2)3
(1,0)4 (1,1)5 (1,2)6
(2,0)7 (2,1)8 (2,2)9
"""
# print(l1[0][0])
# print(l1[2][2])


"""
l2 =[] 
for i in range(3):  # 0 1 2 
    l3=[] 
    for j in range(3):
        l3.append(l1[j][i])
    l2.append(l3)

print("original matrix : ")
for i in l1 : 
    print(i)

print("transpose matrix : ")
for i in l2 :
    print(i)
"""
# c : 

"""
for (i=0; i<3; i++)
{
    for (j=0; j<3; j++)
    {
        printf("%d ", a[i][j]);
    }
}

for (i=0; i<3; i++)
{
    for (j=0; j<3; j++)
    {
        printf("%d ", a[j][i]);
    }
}
"""

"""
l1= [[1,2,3],
     [4,5,6],
     [7,8,9]]

n= len(l1) 

for i in range(n):  # 0 1 2  
    for  j in range(i+1,n):  # 1,3   #                     4       2        =    4          2   
        l1[i][j] ,l1[j][i]  =  l1[j][i] , l1[i][j]  # l1[0][1] , l1[1][0] = l1[1][0], l1[0][1]
for i in l1:
    print(i)
"""

l1= [[1,2,3],
     [4,5,6],
     [7,8,9]]

# sum of  row and col  : 

"""
for i in range(len(l1)):
    print(f"row {i+1} sum ={sum(l1[i])}")  

for i in range(3):  # 1
    colsum=0   # colsum =0 
    for j in range(3):   # j= 0
        colsum +=l1[j][i]   # colsum =12
    print(f"col {j+1} sum ={colsum}")  # col 1 sum =12
"""

#task  : 2 
"""
input  : l1 = [[1,2] , [3,0] , [2,1]]  second value sort and print the list. 
ouput : l1= [[3,0], [2,1] , [1,2]]
"""

     
