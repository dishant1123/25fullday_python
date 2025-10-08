# task :1 
"""
ask user to enter the  string and  remove  the  duplicate  vowel in string. 

input  :  my name is meet. 
output  : my name is met. 
  
"""

s1="my name is mete."

vowels ="aeiou"
result=""
r_vowels =set() 

for i in s1 :  # my name is meet. ==>16 
    if i  in vowels:
        if i not in r_vowels:
            result +=i  # result = m
            r_vowels.add(i) 
    else :
        result +=i
print(result)