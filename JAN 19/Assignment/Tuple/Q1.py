Q.Program to add an item in a tuple.
Solution:
    
tup = (4, 6, 2, 8, 3, 1) 
print(tup)
tup = tup + (9,)
print(tup)
tup = tup[:5] + (15, 20, 25) + tup[:5]
print(tup)
