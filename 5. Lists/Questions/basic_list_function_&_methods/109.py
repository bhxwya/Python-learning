list1 = [12, 13, 14, 18]
list2 = [8, 10, 19, 21]

merged_list = []

# merged_list = list1 + list2

for i in list1:
    merged_list.append(i)
    
for i in list2:
    merged_list.append(i)
    
print(f"Merged list = {merged_list}")