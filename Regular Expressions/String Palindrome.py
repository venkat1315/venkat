import re

s = input("Enter a string: ")
s = re.sub(r'[^A-Za-z0-9]', '', s.lower()) 
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")
