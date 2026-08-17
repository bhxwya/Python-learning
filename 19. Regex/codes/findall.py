# findall() returns a list containing all matches found in the string.
# It can extract names, numbers, or other patterns.

import re

crick_score = "Sachin scores 76 and Dravin scores 40 and Rohit scores 88 and Dhoni scores 99"

name = re.findall(r"[A-Z][a-z]*", crick_score)
age = re.findall(r"\d{2}", crick_score)

print(name)
print(age)

#Example - 2
text = "Rat Cat Pat Mat Sat Qat"

print(re.findall(r"[RPSQ]at", text))
print(re.findall(r"[^RPSQ]at", text))