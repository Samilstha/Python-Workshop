Q. Program to print a specified list after removing the 0th, 4th and 5th elements. 
Solution:
    
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
list = [x for (i,x) in enumerate(list) if i not in (0,4,5)]
print(list)
