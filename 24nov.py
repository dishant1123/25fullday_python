# exception handling  : 
"""try :
    a=int(input("enter the  number   : "))
    b=int(input("enter the  number   : "))

    print(a/b)
except ZeroDivisionError :
    print("error  :  division  by  zero")
    
"""
# value error : 
"""
try :
    l1=[1,2,3,4,5]
    print(l1.index(2))
except ValueError :
    print("value is not in your list try again")
"""

# file  not  found  : 
"""try :
    with open("vidhi.txt","r") as f :
        print(f.read())
except FileNotFoundError :
    print("read mode  not created  a new file always open exiting  file. ")
    
"""

# finally  : 

"""try : 
    with  open("vidhi.txt","r") as f :
        print(f.read())

except FileNotFoundError :
    print("file not found")

finally :
    print("file  closed")
"""

# multiple exception  : 
"""try : 
    list1 =[1,2,3,4,5]
    # print(list1[5])
    print(list1.index(11))

except (IndexError,ValueError):
    print("some error occured")
    
"""
# binary  file : 
"""
binary  ===> 010101 

1. rb ==>  read  binary  file
2. wb ==>  write  binary  file
3. ab ==>  append  binary  file

"""
# import  pickle 

import pickle   

# dump ==>  save  data  in  file , write  to file  
# load ==>  read  data  from  file , read  from  file

# wb : 

"""
data = {"id" :1, "name" : "reagen","age":17,"marks":[90,91,95]}

with  open("reagen.dat","wb") as f :
    pickle.dump(data,f)
"""
# rb :
"""
with  open("reagen.dat","rb") as f :
    result = pickle.load(f)
    
print(result)
"""

# binary  + exception  handling  : 

# wb : 
"""try :
    
    data = {"id" :1, "name" : "om","age":17,"marks":[80,81,85]}
    with  open("om_sarkar.dat","wb") as f :
        pickle.dump(data,f)
    print("data  saved  successfully and  written  to  file. ")
    
except :
    print("error  occured  while  writing  data  to  file. ")
"""

# rb : 

"""try  : 
    with open("om_sarkar.dat","rb") as f :
        result =  pickle.load(f)
        print(result)
    print("data read successfully from file.")
except :
    print("error  occured  while  reading  data  from  file. ")
"""

# ab : append binary  

"""try :
    data2 =[{"id" :2, "name" : "om","age":17,"marks":[80,81,85]},
            {"id":3, "name" : "vidhi","age":19,"marks":[86,87,89]}]
    
    with  open("om_sarkar.dat","ab") as f :
        for i in data2 :
            pickle.dump(i,f)
    print("data  saved  successfully  and  appended  to  file. ")
except :
    print("error  occured  while  writing  data  to  file. ")
    
"""

# all data read to binary file  : 

"""try :
    with open("om_sarkar.dat","rb") as f :
        print("all records read successfully from file.")
        
        while True :
            try  : 
                result   = pickle.load(f)
                print(result)
            except EOFError :
                print("no more data to read")
                break
except  Exception as e :
    print("error  occured  while  reading  data  from  file. ",e)
"""