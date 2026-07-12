my_list = [23, 45, 67, 89, 24, 56, 89, 45 , 22]

count = 0


# for i in my_list:
#     if i % 2 == 0:
#         count += 1

# print(count)


for i in range(0, len(my_list)):
    if my_list[i] % 2 == 0:
        count += 1
        
print(count)