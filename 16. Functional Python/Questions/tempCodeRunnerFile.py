from functools import reduce

numbers = [1, 2, 3, 4, 5]
add_number = []

add_number = reduce(lambda x, y: x + y, numbers)
print(add_number)