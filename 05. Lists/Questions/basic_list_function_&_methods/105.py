my_list = [5, 10, 15, 20, 15]

old_num = int(input("Enter the old number = "))
new_num = int(input("Enter the new number = "))

for i in range (0, len(my_list)):
    if my_list[i] == old_num:
        # x = my_list.index(old_num)
        # my_list.remove(old_num)
        # my_list.insert(x, new_num)
        my_list[i] = new_num

print(my_list)