my_list = []

for i in range(0, 10):
    num = int(input(f"Enter a number at index {i}= "))
    my_list.append(num)
print(my_list)

result = []
for i in range(len(my_list)-1, -1, -1):
    result.append(my_list[i])
print(result)
