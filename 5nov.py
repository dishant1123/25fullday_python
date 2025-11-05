# task :1 

# disarium number  : 

for i in range(1,101):
    temp =i    # 1
    digits = str(temp)  # str 
    length = len(digits)  # len ==> int  
    sum =0 
    while temp >0 :
        r = temp %10 
        sum = sum + r ** length  
        temp = temp //10 
        length = length -1 
        
    if sum == i :
        print(i,end=" ")