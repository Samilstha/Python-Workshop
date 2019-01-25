Q.Program to construct the following pattern, using a nested loop number.
Expected Output:
    1
    22
    333
    4444
    55555
    666666
    7777777
    88888888
    999999999

Solution:
    
for a in range(10):
    for n in range(a):
        print(a, end='')
    print()
