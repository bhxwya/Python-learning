list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]

# list3 = []
# list4 = []
# for i in list1:
#     if i not in list3:
#         list3.append(i)
        
# for i in list2:
#     if i not in list3:
#         list3.append(i)
#     elif i not in list4:
#         list4.append(i)

# print(list4)

result = []

for i in list1:
    if i in list2 and i not in result:
        result.append(i)

print(result)