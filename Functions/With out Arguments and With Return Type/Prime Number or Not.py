def is_prime():
    n = 9
    c = 0
    for i in range(1, n + 1):
        if n % i == 0:
            c += 1
    return c == 2

if is_prime():
    print("Prime")
else:
    print("Not Prime")