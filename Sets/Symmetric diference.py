s1={1,2,3,4,5,6,7,8}
s2={1,2,3,9,12,16}
print(s1.symmetric_difference(s2)) #{4, 5, 6, 7, 8, 9, 12, 16}
print(s2.symmetric_difference(s1)) #{4, 5, 6, 7, 8, 9, 12, 16}
print(s1^s2) #{4, 5, 6, 7, 8, 9, 12, 16}