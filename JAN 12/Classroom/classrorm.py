
print("Hello World!")
print("Hello"*10)

name = input("enter your name")
age = input("enter your age")
print("your name is" + name + "and age is" + age)
print ("your name is {} and age is {}" .format(name,age))
#print ("your name is {} and age is {},{}" .format(name,age)}
print("your name is {} and age is {}" .format(name,age,"hello"))
print("your name is {0} and age is {1} . happy bithday{0}" .format(name,age))
print(f"your name is {name} and age is {age}")

import keyword
print(keyword.kwlist)

a= input("enter the age")
int (a)
print ("your age is", a)

x = True
print(bool(x)) 

x = False
print(bool(x)) 

x = 4
y = 5
print(x/y) 
print(x//y)
print(x%y)
print(x**y)
print(pow(x,y))

x = input("Enter a string: ") 
repeat_num = int(input("Enter the number of repetition: "))
print(x * repeat_num) 
print((x+' ') * repeat_num)
print(x*10)
