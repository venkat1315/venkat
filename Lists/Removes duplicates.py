list=[1,2,7,4,1,23,7,23]
unique=[]
for item in list:
    if item not in unique:
        print(item)
        unique.append(item)
print(unique)

