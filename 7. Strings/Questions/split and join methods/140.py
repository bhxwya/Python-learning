my_string = "Hello World"
my_list = my_string.split()
my_string = " ".join(i[::-1] for i in my_list)
print(my_string)
