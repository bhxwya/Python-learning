original_list = [3, 8, 12, 17, 22, 30, 35, 41, 48, 50]
even_list = []
odd_list = []

for i in original_list:
    if i % 2 == 0:
        even_list.append(i)
    else:
        odd_list.append(i)

print(f"Odd List = {odd_list}")
print(f"Even List = {even_list}")
