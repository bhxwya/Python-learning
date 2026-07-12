original_list = [5, "Code and Debug", "Bhawya", "Bhawya", 23, 67, 89, 98.8, 23, 5, 67, 5]
new_list = []

for i in original_list:
    if i not in new_list:
        new_list.append(i)

print(new_list)