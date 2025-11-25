import  csv 

# writing  in csv file  : 

"""with  open("student.csv",mode="w",newline="") as f :
    writer = csv.writer(f)
    
    writer.writerow(["id","name","marks"]) 
    writer.writerow([1,"het",100])
    writer.writerow([2,"om sarkar",92])
    writer.writerow([3,"vidhi",90])
       
"""
# read csv in file  : 

"""with open("student.csv",mode="r") as f :
    # reader =csv.reader(f)
    # for i in reader :
        # print(i)
    
    g =csv.DictReader(f)
    
    for i in g :
        # print(i["id"],i["name"] ,i["marks"])
        print(i)
"""

# append in csv file  :

"""with  open("student.csv","a",newline="") as f :
    writer =csv.writer(f)
    
    writer.writerow(["4","purva",90])
    writer.writerow(["5","shalin",97])

"""    

    
rows=[
        [101,"pratham",56],
        [102,"prashant",56],
        [103,"pradeep",56],
    ]
with  open("student.csv","a",newline="") as f :
    writer =csv.writer(f)
    writer.writerows(rows)
