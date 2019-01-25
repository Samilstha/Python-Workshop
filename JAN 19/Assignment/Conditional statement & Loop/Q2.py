Q.Create a for loop that prompts the user for a hobby 3 times, then appends each one to
hobbies.
Solution:
    
hobbies = []
for i in range(3):
    hobby = input("Enter a hobby:")
    hobbies.append(hobby)
print (hobbies)
