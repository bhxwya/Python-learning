# split() splits a string wherever the given regex pattern is found.
# The result is returned as a list of separate parts.

import re

text = "How r you\nI am fine\nThank u"

reg = re.compile(r"\n")
result = reg.split(text)

print(result)

#Example - 2
text = "Python is easy to learn"

result = re.split(r"\s", text)

print(result)