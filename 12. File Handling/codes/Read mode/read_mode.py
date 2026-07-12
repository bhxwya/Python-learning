# my_file = open("hello.txt", "r")

# my_file = open(
    # "C:\\Users\\Ansh\\OneDrive\\Desktop\\MY CODES\\Python-learning\\12. File Handling\\codes\\Read mode\\hello.txt", "r")

my_file = open(
    r"C:\Users\Ansh\OneDrive\Desktop\MY CODES\Python-learning\12. File Handling\codes\Read mode\hello.txt", "r")

# print(my_file.read())

# print(my_file.read(5))
# print(my_file.read(5))

# print(my_file.readline())
# print(my_file.readline())

print(my_file.readlines())

my_file.close()
