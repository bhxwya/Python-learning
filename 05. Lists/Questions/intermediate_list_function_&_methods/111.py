my_list = [5, 10, 15, 20 ,1 ,1, 5]
num = int(input("Enter a number = "))
    
if num in my_list:
    print(my_list.index(num))

else:
    print(-1)
        