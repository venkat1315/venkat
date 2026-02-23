import re

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

num = input("Enter a number: ")

if re.match(r'^\d+$', num):
    num = int(num)
    print("Factorial of", num, "is:", factorial(num))
else:
    print("Invalid input! Please enter a positive integer.")
