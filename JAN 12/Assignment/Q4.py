 Get the first name and last name from a user and use different string formatting techniques that we
learnt in class to get a formatted string.
For example: If user’s first name is Ram and last name is Bahadur, the output should be:
Hello! Ram Bahadur.

Soultion:

firstname = input("Enter first name: ")
lastname = input("Enter last name: ")
print("Hello! "+firstname+" "+lastname+".")
print(f"Hello! {firstname} {lastname}.")
print("Hello! {} {}.".format(firstname,lastname))
print("Hello! {0} {1}.".format(firstname,lastname))
print("{} {} {}.".format("Hello!",firstname,lastname))
print("Hello! {first_key} {last_key}.".format(first_key=firstname,last_key=lastname))
#print ("your firstname is {} and lastname is {},{}" .format(firstname,lastname)}
print("Hello! {1} {0}.".format(lastname,firstname))
