Q. Program to create a list by concatenating a given list which range goes from 1 to n. 
Solution:
    
my_list = ['p', 'q']
n = 5
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]
print(new_list)
