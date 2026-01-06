s = input("Enter a string: ")
vowels = "aeiouAEIOU"   # include both lowercase and uppercase
count = 0
i = 0

while i < len(s):
    if s[i] in vowels:
        count += 1
    i += 1

print("Number of vowels:", count)