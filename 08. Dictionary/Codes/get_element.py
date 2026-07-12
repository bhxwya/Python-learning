my_dict = {"name": "Bhawya Kumar",
           "age": 23, 
           "sex": "No Experience"}

#to get a value
# print(my_dict["name"])
# print(my_dict["sexx"])
# print(type(my_dict["name"]))


#get method
# r = my_dict.get("sex")
# r = my_dict.get("namee")
# print(r)
# print(type(r))


k = input("Enter a key: ")
result = my_dict.get(k)

if result != None:
    print(result)
else:
    print("Key doesn't Exist")