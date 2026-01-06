n = int(input("Enter a number: "))

i = 1
print("Factors of", n, ":")
while i <= n:
    if n % i == 0:
        print(i)
    i += 1