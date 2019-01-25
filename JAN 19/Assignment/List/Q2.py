Q. Program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
Solution:
  
def numberof_strings(word):
  x = 0
  for w in word:
    if len(w) > 1 and w[0] == w[-1]:
      x += 1
  return x
print(numberof_strings(['abc', 'xyz', 'aba', '1221']))
