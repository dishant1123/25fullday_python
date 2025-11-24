# file handling  : txt open  , csv open  
"""
file open  : 
mode  : 

1. read mode  : exiting  file open ,  no new file  create in read mode. 
2. write  mode  : create  new file  , write  data in file , exiting  file  open  ==> overwrite
3.append mode : create  new file  , write  data in file , exiting  file  open  ==> last add . 

fopen () ==>  open file ("name.txt","mode") , with  open(), 
fclose() 
f.read() , f.readline() , f.readlines() 
f.write(), f.writelines() 

"""

# write  : 
"""
with open("vidhi.txt","w") as f : 
    f.write("my name is vidhi.\n")
    f.write("my age is 22.\n")
    f.write("study in sliver oak university.\n")
    f.write("dream to meet sharukh khan.\n")
    f.close()
"""
    
# exiting file  opne  in write  mode  : 

"""with open("vidhi.txt","w") as f :
    f.write("my best friend name is purva.\n")
    f.write("study in ROYAL.\n")
    f.write("recently vidhi drop i-phone.\n")
    f.close()
"""

# read: exiting  file  . 
"""
with  open("harshil.txt") as f :
    # context = f.read()  # read all file  
    # context =f.readline()  # read one line
    context = f.readlines()  # read all line ==> in list 
    print(context)
"""
 
# append : 

"""with open("om.txt","a") as f : 
    f.write("my name is om.\n")
    f.write("my age is 21.\n")
    f.write("study in GROWMORE  university.\n")
    f.write("dream to meet salman khan.\n")
    f.close()
"""
# exiting : 
"""with open("om.txt","a") as f : 
    f.write("my best friend name is saumya.\n")
    f.write("study in ROYAL.\n")
    f.write("made in nagpur.\n")
    f.close()
"""

# task  : 1 list   ==>  odd even  ==> txt file   ==> 

"""
1. r+ : read + write  
2. w+ : read + write 
3. a+ : append + write  + read 
"""
"""
with  open("vidhi.txt","r+") as f :
    f.write("shalin patel.")
    f.seek(0)    # using seek  to  move  cursor  to  start  of  file
    context = f.read()
    print(context)
    f.close()
    
#my best friend name is purva.   ==> saumya  patel    saumya
"""

# w+ : 

"""
with  open("vidhi.txt","w+") as f :
    f.write("shalin patel.")
    f.seek(0)    # using seek  to  move  cursor  to  start  of  file
    context = f.read()
    print(context)
    f.close()
"""

# a+:

with  open("harshil.txt","a+") as f :
    
    f.write("shalin patel.")
    f.seek(0)    # using seek  to  move  cursor  to  start  of  file
    
    context = f.read()
    print(context)
    f.close()
 

