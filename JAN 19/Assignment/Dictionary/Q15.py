Q. Program to print all unique values in a dictionary
Solution:
    
x = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
print("Original List: ",x)
unique_value = set( val for dic in x for val in dic.values())
print("Unique Values: ",unique_value)
