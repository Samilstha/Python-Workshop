#Classroom works:

def function (x,y=0, *args, **kwargs):
    print (x)
    print (y)
    print(args)
    print(kwargs)
function(1,2,3,4,5)


def function (x,y=0, *args, **kwargs):
    print (x)
    print (y)
    print(args)
    print(kwargs)
function(1,2,3,4,5, name="nishesh")


x=list (range(0,10))
y=[]
for each in x:
    y.append(each**2)
    
print (y)


z=[each**2 for each in range(0,10)]
print(z)


programming_lang = ["C","Python","Java"]
creator=["Dennis", "Guido", "James"]

d={}
for key, val in zip (programming_lang, creator):
    d[key]= val

print (d)

programming_lang = ["C","Python","Java"]
creator=["Dennis", "Guido", "James"]

x= {}
x= {key: val for key, val in zip (programming_lang, creator)}
print(x)


def sum (a,b):
    return a+b
print(sum(1,2))

a= lambda a, b:a+b
print (a(5,6))



def sum (a,b):
    yield a+b
    yield a-b
print(next(sum(1,2)))


def sum (a,b):
    yield a+b
    yield a-b
gen_sum=sum(1,2)
print(next(gen_sum))
print(next(gen_sum))
print(next(gen_sum))


for each in gen_sum:
    print (each)


def sum ():
    i=0
    yield i
    i+=1
    yield i
    i+=100
    yield i


    l = [x for x in range(1, 10000)]
g = (x for x in range(1, 10000))

print("Memory consumed by list l: ", l.__sizeof__())
print("Memory consumed by generator g: ", g.__sizeof__())


l = [x for x in range(1, 10000)]
g = (x for x in range(1, 10000))
print(type(g))
print("Memory consumed by list l: ", l.__sizeof__())
print("Memory consumed by generator g: ", g.__sizeof__())


def sum(a,b):
    return a+b

a = sum
print (type(a))

def accept_func(a):
    print (a(1,2))

accept_func(a)



def outer():
    def inner(a,b):
        return a+b
    return inner
x = outer()
print (x.__name__)


def outer():
    def inner(a,b):
        return a+b
    return inner
x = outer()(4,5)
print (x)

class Car:

    def __init__(self,name, wheels, engine):
         self.name = name
         self.wheels = wheels
         self.engine = engine

    def drift(self):
        print(f"{self.name} is drifting")

    def __str__ (self):
        return self.name
    
    def __repr__ (self):
        return f"Car({self.name},{self.wheels},{self.engine})"
    
        
kia = Car("kia", 4, "diesel")
print (isinstance(kia, Car))


    
class Animal:

    def __init__(self,type):
        self.type = type


class Dog(Animal):
    def __init__(self,name,type):
        super().__init__(self)
        self.name = name
        self.type = type
d= Dog("tom", "carni")
print(d.__dict__)
print(isintance(d,Animal))
print(isintance(d,Dog))
print(isintance(d,type))

        




