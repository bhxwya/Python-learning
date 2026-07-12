my_list = [23, 60, 35, 67, 80, 92, 90, 20, 55, 10, 200]
total = 0

# for i in my_list:
#     if i % 2 == 0:
        # total = total + i

for i in range (0, len(my_list)):
    if my_list[i] % 2 == 0:
        total = total + my_list[i]
print(total)
