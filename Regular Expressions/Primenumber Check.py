import re

def is_prime(n):
    if n <= 1:
        return False
    i = 2
    while i <= n // 2:
        if n % i == 0:
            return False
        i += 1
    return True

# Input
num = input("Enter a number: ")

# Regex to check if input is a positive integer
if re.match(r'^\d+$', num):
    num = int(num)
    if is_prime(num):
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
else:
    print("Invalid input! Please enter a positive integer.")
