Q. Write a function called nested_sum that takes a list of lists of integers and adds up
the elements from all of the nested lists.
Solution:

def nested_sum(n):
    sum_list = 0
    for each in n:
        if type(each) == int:
            sum_ist += each
        else:
            sum_1ist += nested_sum(each)
    return sum_list

t = [[1, 2], [3], [4, 5, 6]]
print(f"Sum is {nested_sum(t)}")
