Q.Program to identify the leap year. 
Solution:

def _leap(x):
    if x % 400 == 0:
        return True
    if x % 100 == 0:
        return False
    if x % 4 == 0:
        return True
    return False

print(_leap(int(input())))
