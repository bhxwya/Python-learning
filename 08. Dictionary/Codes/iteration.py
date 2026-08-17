my_dict = {"name": "Anubhav",
           "Age": "34",
           "Gender": "Non-binary",
           }

"""keys method"""
# print(my_dict.keys()) # Returns a dict_keys object (view)

for k in my_dict.keys():
    print(k)

for k in my_dict.keys():
    print(my_dict[k])

"""values method"""
# print (my_dict.values()) # Returns a dict_values object, not a list

# for v in my_dict.values():
#     print(v)
    
    
#question
# my_dict = {
# "history": 67,
# "comp": 99,
# "science": 78,
# "maths": 11,

# }
# total = 0
# for v in my_dict.values():
#     total = total + v
# print(total)