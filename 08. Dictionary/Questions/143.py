lst1 = ['Ten', 'Twenty', 'Thirty']
lst2 = [10, 20, 30]
my_dict = {}

for i in range(0, len(lst1)):
    my_dict[lst1[i]] = lst2[i]
print(my_dict)
