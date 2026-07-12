list1 = [56, 25, 14, 78, 19, 62]
largest_num = float("-inf")
second_largest_num = float("-inf")

for i in list1:
    if largest_num < i:
        second_largest_num = largest_num
        largest_num = i
    elif largest_num > i and second_largest_num < i:
        second_largest_num = i
        
print(f"Second Largest Number = {second_largest_num}")