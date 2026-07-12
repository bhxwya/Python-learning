original_list = [3, 6, 9, 12, 15, 21, 24, 27, 30]
new_list = []
x = int(input("Enter a number = "))

for i in original_list:
    if i % x != 0:
        new_list.append(i)

print(new_list)
