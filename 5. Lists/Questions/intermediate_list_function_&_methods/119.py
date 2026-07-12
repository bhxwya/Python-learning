my_list = [10, 20, 30, 40, 50]
list1 = []
list2 = []

for i in range(0, len(my_list)//2):
    list1.append(my_list[i])

for i in range(len(my_list)//2, len(my_list)):
    list2.append(my_list[i])
    
print(list1)
print(list2)