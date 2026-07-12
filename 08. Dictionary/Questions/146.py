my_string = input("Enter a string: ")
result = {}

# for k in my_string:
#     v = my_string.count(k)
#     result[k]=v
# print(result)

for k in my_string:
    if k not in result:
        result[k] = 1
    else:
        result[k] += 1
print(result)