Q. Write a definition for a class named Circle with attributes center and radius ,
where center is a Point object (tuple) and radius is a number.
Solution:
    
class Circle:
    def __init__(self, center,radius):
        self.center = center
        self.radius = radius
a = int(input("Enter x coordinate of center: "))
b = int(input("Enter y coordinate of center: "))
c = int(input("Enter radius: "))
_circle = Circle((a,b),c)
print(_circle.center)
print(_circle.radius)
