Q. Program to check whether a number entered by the user is magic number or not. The user will enter 1729 input number and program will calculate and check if it is magic number or not and print
on the console.
What is the magic number?
Input: 1729

Sum of digits of the given number.(1 + 7 + 2 + 9 => 19)
The reverse of 19 is 91
The product of digit sum and the reverse of digit sum.(19 X 91 = 1729)
If the product value and the given input are same,
then the given number is a magic number.(19 X 91 <=> 1729)
Output: So, 1729 is a magic number. 

Solution:

def isMagic(n):
    sum = 0; 
       
    while (n > 0 or sum > 9): 
        if (n == 0): 
            n = sum; 
            sum = 0; 
        sum = sum + n % 10; 
        n = int(n / 10);  
    return True if (sum == 1) else False; 
  
n = 1729; 
if (isMagic(n)): 
    print("Magic Number"); 
else: 
    print("Not a magic Number"); 
      
