#join

# my_list = ["Bhawya", "ANSH", "Abhishek", "Shivam"]
# my_string = "  |  ".join(my_list)
# my_string = "  |  ".join(i for i in my_list)
# print(type(my_string))
# print(my_string)

my_list = ["Bhawya", "ANSH", "Abhishek", "Shivam" , 96]
# my_string = " ".join(i for i in my_list) #gives error (int not allowed)

my_string = " ".join(str(i)[::-1] for i in my_list)
print(my_string)
