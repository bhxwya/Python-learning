my_dict = {"name": "Bhawya Kumar",
           "age": 23,
           "sex": "No Experience"}
print(my_dict)

# you can use delete keyword everywhere example,
# del my_dict["age"]
# del my_dict

# now the pop method
# my_dict.pop("sex")
# my_dict.pop()
# print(my_dict)


# What is .popitem()?
# It removed the last inserted key-value pair.It returned it as a tuple.
# Each call removes the last inserted item
pi = my_dict.popitem()
print(pi)
print(my_dict)
