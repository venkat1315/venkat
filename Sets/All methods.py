s1={1,2,3,4,5,6,7,8}
s2={1,2,3,9,10,11}
print(s1.union(s2)) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(s1|s2) #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print(s1.intersection(s2)) #{1, 2, 3}
print(s1&s2) #{1, 2, 3}
print(s1.difference(s2)) #{4, 5, 6, 7, 8}
print(s1-s2) #{4, 5, 6, 7, 8}
print(s2.difference(s1)) #{9, 10, 11}
print(s2-s1) #{9, 10, 11}
print(s1.symmetric_difference(s2)) #{4, 5, 6, 7, 8, 9, 10, 11}
print(s1^s2) #{4, 5, 6, 7, 8, 9, 10, 11}
s1.add(20)
print(s1) #{1, 2, 3, 4, 5, 6, 7, 8, 20}
s2.update([30,40])
print(s2) #{1, 2, 3, 40, 9, 10, 11, 30}
s1.remove(7)
print(s1) #{1, 2, 3, 4, 5, 6, 8, 20}
s2.discard(40)
print(s2) #{1, 2, 3, 9, 10, 11, 30}
s1.pop()
print(s1)#{2, 3, 4, 5, 6, 8, 20}