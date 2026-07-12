my_set = {1, 2, 3, 4, 5, 6, 7, 8, 8, 9, 10, 10}
num = int(input("Enter a number: "))

# lets try this by iteration first

# for i in my_set:
#     if i == num:
#         found = True
#         break
#     else:
#         found = False
        
# if found == True:
#     print("Yes")
# else:
#     print("No")


#by membership
if num in my_set:
    print("yes")
else:
    print("no")