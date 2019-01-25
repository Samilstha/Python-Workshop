Q.Program to check the validity of password input by users.

import re
x= input("Input your password")
a= True
while a:  
    if (len(x)<6 or len(x)>12):
        break
    elif not re.search("[a-z]",x):
        break
    elif not re.search("[0-9]",x):
        break
    elif not re.search("[A-Z]",x):
        break
    elif not re.search("[$#@]",x):
        break
    elif re.search("\s",x):
        break
    else:
        print("Valid Password")
        a=False
        break

if a:
    print("Not a Valid Password")
