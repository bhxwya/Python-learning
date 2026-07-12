my_dict = {"name": "Bhawya Kumar",
           "age": 23,
           "sex": "No Experience"}
print(my_dict)

# by key
# my_dict["age"] = 21
# my_dict["name"] = "Ansh"
# my_dict["City"] = "Ludhiana"  # key doesn't exist so it adds on its own


# by update method(Remember update method needs a dictionary to work)
# you can add/update mutliple keys and values in single line using this method
my_dict.update({"State": "Punjab", "Pin code": 141003,
               "sex": "male", "Age": 89})
print(my_dict)
