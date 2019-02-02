Q. Program that accepts a sentence and calculate the number of upper case letters and lower
case letters.
Solution:
    
def string_test(s):
    d={"UPPER_CASE":0, "LOWER_CASE":0}
    for c in s:
        if c.isupper():
           d["UPPER_CASE"]+=1
        elif c.islower():
           d["LOWER_CASE"]+=1
        else:
           pass
    print ("Original String : ", s)
    print ("UPPER CASE : ", d["UPPER_CASE"])
    print ("LOWER CASE : ", d["LOWER_CASE"])

string_1 =input('Enter a string:')
string_test(string_1)
