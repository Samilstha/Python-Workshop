l =[1,2,3]
a=l*5
print(a)

s = "Hello world"
print(s.split(" "))


x = (1,2,3)
print(x[0])
print(x[-1])
print(x[:2])


w = 1, 2, 3
print(x)
x, y, z = w
print(x)
print(y)
print(z)


a = 4
b = 5
b,a =a,b
print(b)
print(a)


s = {"Hello",1,1.15,("OK",None)} 
s.update(("Helloo",2))
print(s)
print(type(s))
print(len(s))


def print_happy(name):
    print(f"Happy Birthday to you! \n"*2+"Happy Bithday to you {name}!!")
yourname=input("enter your name: ")
print_happy(yourname)



def sum_num(*args):
    print(args)
sum_num()
sum_num(1,2,3)
sum_num(1,2,3,4,5)


def sum_vals(**kwargs):
    print(kwargs)
sum_vals(a=10,b=50)
