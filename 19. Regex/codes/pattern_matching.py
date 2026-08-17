# Regex patterns define what kind of text we want to find.
# Common patterns: [A-Z], [a-z], \d, \w, {n}, +, *.

import re

text = "Sachin scores 76 and Rohit scores 88"

print(re.findall(r"\d{2}", text))