Q. Write a function called middle that takes a list and returns a new list that contains
all but the first and last elements.
Solution:
    
def middle(l):
    del l[0]
    if len(l) >= 1:
        del l[-1]
    return l


t = [1, 2, 3, 4]
print(f"New list: {middle(t)}")
