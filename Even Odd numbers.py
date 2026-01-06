n = int(input("Enter a number: "))

i = 1
print("Even numbers:")
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1

i = 1
print("Odd numbers:")
while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1