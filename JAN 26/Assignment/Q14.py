Q. Write recursive function to calculate fibonacci number.
Solution:
    
def gen_seq(length):
    if(length <= 1):
        return length
    else:
        return (gen_seq(length-1) + gen_seq(length-2))

length = int(input("Enter number of terms:"))

print("Fibonacci sequence:")
for iter in range(length):
    print(gen_seq(iter))
