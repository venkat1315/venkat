file = open("data.txt", "w")   # Open file in write mode
file.write("Hello Python\n")
file.write("This is file writing example.")
file.close()

file = open("data.txt", "r")   
data=file.read()
print(data)
file.close()

file = open("data.txt", "r")   
data=file.readline()
print(data)
file.close()

file = open("data.txt", "r")   
data=file.readlines()
print(data)
file.close()

with open("data.txt", "r") as file:
    line_count = 0
    for line in file:
        line_count += 1

print("Total lines:", line_count)

def ch_count(a):
    with open (a,"r") as f:
        data = f.read()
        count=len(data)
        return count
print(ch_count("data.txt"))  

def word_count(a):
    with open (a,"r") as f:
        data=f.read()
        words=data.split()
        count=len(words)
        return count
print(word_count("data.txt"))


