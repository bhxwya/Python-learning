my_list = [23, 45, 67, 89, 24, 56, 89]

#by iterating index
for i in range(0, len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i], end=" ")
print()

#by iterating values
for i in my_list:
    if i % 2 != 0:
        print(i, end=" ")
