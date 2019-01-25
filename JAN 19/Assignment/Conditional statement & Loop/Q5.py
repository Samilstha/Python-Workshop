Q.Program that prints all the numbers from 0 to 6 except 3 and 6.
Solution:

for a in range(6):
    if (a == 3 or a==6):
        continue
    print(a,end=' ')
print("\n")
