"""
file handling  : 

file  3 mode  : 

1.read  == >  file  exiting  open   ==>r 
2.write ==> new file  create  +  write  + exiting  open   ==> overwrite 
3.append ==> new file  create  +  write  + exiting  open   ==> append

open  ==>  with open 
close ==> close 

"""

# w  mode:

"""
with  open("harshil.txt","w") as file: 
    file.write("my name is harshil.\n") 
    file.write("live in gandhinagar.\n")
    file.write("TABLE TENNIS  LOVER.\n")
    file.write("food  lover.\n")
    file.close()
     
"""
# w : exiting open  

"""
with open("harshil.txt","w") as file: 
    file.write("huge property.\n") 
    file.write("study  in GROWMORE.")
    file.close()
"""

# append  mode : 
"""
with  open("het.txt","a") as file: 
    file.write("my name is het.\n") 
    file.write("live in gandhinagar.\n")
    file.write("CRICKET  LOVER.\n")
    file.write("PHOTOGRAPHY  lover.\n")
    file.close()
"""
# exiting file open in append mode : 
"""with  open("het.txt","a") as file: 
    file.write("study in ROYAL.\n")
    file.write("BIKE lover.")
    file.close()
"""

# read mode:

"""with  open("het.txt","r") as file:
    # context =file.read() # read all the file
    # context=file.readline()  # only first line  read 
    context=file.readlines()
    print(context)
"""

# task :1 
"""
ask user to enter the string  and  print  vowel  and  consonant in seprate  txt  file. 

input :  my name is ketan. 

consonant.txt :my nm s ktn. 
vowel.txt :  ae i e a 
"""

# with open("consonant.txt","w") as file:
    # with  open("vowel.txt","w") as file1:
"""n=input("enter the string : ")
print(n)
for i in n : 
    if i in "aeiouAEIOU":
        with open("vowel2.txt","a") as file:
            file.write(i)
    else :
        with open("consonant2.txt","a") as file:
            file.write(i)
        
"""
# task  :2 
"""
bal =25000 
1. deposit   ==>10000 
2. withdraw  ==> 15000 
3. check _balance

passbook.txt 
                        STATE BANK OF INDIA 
                                                ACC.NO :729212390003
DATE : 24-9-2025                                ACC.NAME :HARSHIL THAKKAR 
BRANCH : AHMEDABAD                              PAN :AWKPS3297A 

DATE/TIME            AMOUNT           DR          CR          BALANCE 

24-9-2025                                                     25000 
24-9-2025            10000                       10000        35000 
24-9-2025            15000           15000                    20000
"""

