my_list = [12, 3, 4, 8, 7, 2]
result = []

# for num in my_list:
#     prime = True
#     for i in range(2, num):
#         if num % i == 0:
#             prime = False
#             break
#     if prime:
#         result.append(num)


for num in range (0, len(my_list)):
    factor = 0
    for i in range (1, my_list[num] + 1):
        if my_list[num] % i == 0:
            factor += 1
    
    if factor == 2:
        result.append(my_list[num])
        
print(result)
            
            
    