Write a function called disect that takes a list, modifies it by removing the first and
last elements
For example:
>>> l = [1, 2, 3, 4]
>>> disect(t)
>>> t
[2, 3]

Solution:

def disect(t):
    del t[0]
    if(len(t)-1>0):
        del t[len(t)-1]
    return t
