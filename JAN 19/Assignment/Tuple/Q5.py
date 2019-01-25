Q. Program to remove an item from a tuple.
Solution:
    
tup = ("a","e", "i", "o", "u", 1, 2)
print(tup)
tup = tup[:2] + tup[3:]
print(tup)
