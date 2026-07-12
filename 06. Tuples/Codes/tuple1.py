my_tuple = (23, 4, 45, 67, 89, 23)

print(my_tuple.count(23))
print(my_tuple.index(45))
print(my_tuple[4])
print()

for i in my_tuple:
    print(i, end= " ")

# Immutable Example
my_tuple[0] = 100
print(my_tuple[0])

