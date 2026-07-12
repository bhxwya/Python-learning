my_list = [ 1, 2, 3, 74, -1 , -10, -90, -3, -5]
positive_count = 0
negative_count = 0

for i in range(0, len(my_list)):
    if my_list[i] > 0 :
        positive_count +=1
    else:
        negative_count +=1

print(f"Your positive number count is {positive_count}")
print(f"Your negative number count is {negative_count}")
        