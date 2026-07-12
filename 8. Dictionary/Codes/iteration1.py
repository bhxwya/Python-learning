my_dict = {"name": "Anubhav",
           "Age": "34",
           "Gender": "Non-binary",
           }

# for i in my_dict.keys():
#     print(f"{i} -> {my_dict[i]}")
    
    
for key,value in my_dict.items():
    print(f"{key} -> {value}")
    
print(my_dict.items())