#string :
 
# join : 

"""s1=["my","name","is" ,"ketan"]
s2="".join(s1)
print(s2)
"""
# isalpha : 

"""s1="happyDiwali"
print(s1.isalpha())  # only  alphabet  a to z 

s2="1234happyDiwali" 
print(s2.isalnum())  # alphabet + number

s3="1234"
print(s3.isdigit())  # 0-9  only digit : 

s4="happy diwali"
print(s4.islower())  # only lower case 
"""
"""s5="HAPPY DIWALI"
print(s5.isupper())  # only upper case
"""

s1="Happy Diwali"
# print(s1.istitle())  # first letter of each word is capital

s2="my name is  om."
"""print(s2.startswith("my"))
print(s2.startswith("my "))
print(s2.startswith("myn"))

print(s2.endswith("."))
print(s2.endswith("om"))
"""

# prefix , suffix :
"""s2="my name is  om."

print(s2.removeprefix("my"))
print(s2.removeprefix("name"))

print(s2.removesuffix("m."))
print(s2.removesuffix(" om."))
print(s2.removesuffix("s om."))
"""

"""
result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60]}
Expected Output: [{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, {'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]

"""

"""result = {'Science': [88, 89, 62, 95, 50], 'Language': [77, 78, 84, 80, 60], 'Maths': [70, 65, 75, 80, 90]}
subjects=[]
marks_lists=[]
for  subject,marks_list in result.items() : 
    subjects.append(subject)   # sci  lan 
    marks_lists.append(marks_list)    # [[88, 89, 62, 95, 50] , [77, 78, 84, 80, 60]]
                                        # 0                       1                  marks_lists[0]
l1=[]
for i in range(len(marks_lists[0])) :  #[88, 89, 62, 95, 50]
    d2={}
    for  j in  range(len(subjects)) :  # 0 
        d2[subjects[j]] =marks_lists[j][i]   # d2[sci]=marks_lists[0]  
    l1.append(d2)
print(l1)


l2=[[88, 89, 62, 95, 50] ,
    [77, 78, 84, 80, 60]]
"""
"""
(0,0) ==>88  (0,1) ==>89 

"""

"""
[88, 89, 62, 95, 50]  ==> index ==>0 0,0  ==>88  0,1 ==>89 
"""


"""
A Python Dictionary contains List as a value. Write a Python program to update the list values 
 in the said dictionary.
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}
"""

d1={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}

"""for i,j in d1.items():
    if i=="Math":
        j[0]=89
        j[1]=90
        j[2]=91
    elif i=="Physics":
        j[0]=90
        j[1]=92
        j[2]=87
    elif i=="Chemistry":
        j[0]=90
        j[1]=87
        j[2]=93
print(d1)
"""
"""l1=[] 
for i in d1["Math"]:
    l1.append(i+1)
d1["Math"]=l1
d1["Physics"]=[90,92,87]
print(d1)
"""
