numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

squared_even_num = list(filter(lambda x : x % 2 == 0, numbers))
squared_even_num = list(map(lambda x: x*x, squared_even_num))
print(squared_even_num)