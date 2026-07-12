list1 = [15, 16, 18, 19, 55, 98]

list2 = list1.copy()
# list2 = list1

list1[2] = 0

print(list1)
print(id(list1))

print(list2)
print(id(list2))