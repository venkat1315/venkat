
n = int(input("Enter a number: "))
i = 1

print("Even numbers up to", n, ":")
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
