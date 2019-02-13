def countvowel(str1): 
   c = 0
   
   s="aeiouAEIOU"
   v = set(s) 

   for alpha in str1: 
      if alpha in v: 
         c = c + 1
   print("No. of vowels ::>", c) 
  
str1 = input("Enter the string ::>") 
countvowel(str1) 
