"""
Count, Startswith, Endswith
Index, Find, Replace, Strip

"""

my_string = "@hello_world@@@@@"

c = my_string.count("ll")
print(c)

c = my_string.startswith("@hello")
print(c)

c = my_string.endswith("world")
print(c)

c = my_string.strip("@")
print(my_string)
print(c)

c = my_string.replace("@h", "H")
print(c)

c = my_string.index("@")
print(c)

c = my_string.find("@")  # same as index
print(c)

c = my_string.find("z")  # Returns -1 on not found
print(c)

c = my_string.index("z")  # gives error
print(c)
