Q. Write a function called cumulative_sum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
original list.
Solution:

def cummulative_sum(n):
    new_list = []
    sum_1ist = 0
    for each in n:
        sum_1ist += each
        new_list.append(sum_1ist)
    return new_list


t = [1, 2, 3]
print(f"original list: {t}")
print(f"Cummulative sum list: {cummulative_sum(t)}")
