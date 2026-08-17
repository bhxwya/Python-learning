# search() looks anywhere in the string and returns a match object if found.
# It can be used in an if condition to check whether a pattern exists.

import re

text = "Her name is Tamanna and Tamanna is a good girl"

if re.search("Tamanna", text):
    print("Item found")
    
    
#Example - 2
text1 = "My phone number is 404-4000-8789"

if re.search(r"\d{3}-\d{4}-\d{4}", text1):
    print("Phone number found")