Q. Python script to merge two Python dictionaries.
Solution:
    
first_dict = {'a': 10, 'b': 20}
second_dict = {'x': 30, 'y': 20}
d = first_dict.copy()
d.update(second_dict)
print(d)
