my_list = [23, 60, 35, 67, 80, 92, 90, 20, 55, 10, 200]
count = 0

# for i in my_list:
#     if i % 2 == 0 and i % 5 == 0:

for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0 and my_list[i] % 5 == 0:
        count += 1
print(f"{count} numbers are divisible by 2 and 5")
