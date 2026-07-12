original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_list = []

for i in range (0, len(original_list)):
    if original_list[i] % 2 != 0:
        odd_list.append(original_list[i])

print(odd_list)