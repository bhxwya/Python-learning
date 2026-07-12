my_list = [51, 85 , 1748, 52 , 44 ,100, 200]
total = 0

for i in range (0, len(my_list)):
    if my_list[i] % 2 == 0 or my_list[i] % 3 == 0:
        total = total + my_list[i]
print(total)