n = int(input("Enter a number: "))
num = 2

print("Prime numbers up to", n, ":")
while num <= n:
    i = 2
    is_prime = True
    while i <= num // 2:
        if num % i == 0:
            is_prime = False
            break
        i += 1
    if is_prime:
        print(num)
    num += 1