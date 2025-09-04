"""
task  :4 take list from user append all element in list and print pelindorme word in list  
         input : ["java", "python", "php","cpp","flutter","maam"]
         output :  ['php','maam']
"""
# n=int(input("enter the  number  of ele to store  in list : "))
# l1=[] 
# for i in range(n):
#     a=input("enter the  string  / word :")
#     l1.append(a)
# print(l1)
# ["php","maam","ketan"]
# l2=[]
# for i in l1 :
#     if str(i) ==i[ : : -1]:
#         l2.append(i)
# print(l2)

""" 
task  :2 take list from user append all element in list and print longest word in list  
         input : ["java", "python", "php","cpp","flutter"]
         output :  flutter
"""

# n=int(input("enter the  number  of ele to store  in list : "))
# l1=[] 
# for i in range(n):
#     a=input("enter the  string  / word :")
#     l1.append(a)
# print(l1)

# # ["java", "python", "php","cpp","flutter"] 
# s2=""
# for  i in l1 :
#     if len(i) > len(s2) :     # 7 >6
#         s2=i    # flutter  ==> 7 
# print(s2)


"""
task :3
Write a Python program to find the length of a given list of non-empty strings.
	Input:
	['cat', 'car', 'fear', 'center']
	Output:
	[3, 3, 4, 6]
	Input:
	['cat', 'dog', 'shatter', 'donut', 'at', 'todo', '']
	Output:
	[3, 3, 7, 5, 2, 4, 0]

"""

"""
task  :6 
Write a Python program to count the number of strings from a given list of strings. 
	The string length is 2 or more and the first and last characters are the same.
	
	Sample List : ['abc', 'xyz', 'aba', '1221']
	Expected Result : 2

"""
"""
task:7 
Write a Python program to find strings in a given list containing a given substring.
Input:
[(('cat', 'car', 'fear', 'center'))]
Output:
['cat', 'car']
Input:
[(('cat', 'dog', 'shatter', 'donut', 'at', 'todo', ''))]
Output:
['dog', 'donut', 'todo']


"""

"""l1 =[(('cat', 'car', 'fear', 'center'))]
n=input("enter the  word : ")
l2 =[]
for i in l1[0] : 
    if n in i:
        l2.append(i)
print(l2)
"""
n=int(input("enter the  number  : "))
sum =0 

for i in str(n):
    sum = sum + int(i)
print(sum) 
