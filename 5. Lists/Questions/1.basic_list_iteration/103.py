my_list = [52, 85 , 1748, 51 , 44 ,100, 200, -3 , -1748 , -1749]

smallest = my_list[0]

for i in range(0 , len(my_list)):
    if my_list[i] < smallest:
        smallest = my_list[i]

print(smallest)