Q. Program to get the maximum and minimum value in a dictionary.
Solution:
    
dictionary = {'x':50, 'y':74, 'z': 60}

value_max = max(dictionary.keys(), key=(lambda k: dictionary[k]))
value_min = min(dictionary.keys(), key=(lambda k: dictionary[k]))

print('Maximum Value: ',dictionary[value_max])
print('Minimum Value: ',dictionary[value_min])
