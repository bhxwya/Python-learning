"""
Ask a string from user, remove all the duplicates from that string and
print that string again (order does'nt matter)
"""

my_string = "aerrrooooplllaane"
my_set = set(my_string)

joined_string = "|".join(my_set)
print(joined_string)