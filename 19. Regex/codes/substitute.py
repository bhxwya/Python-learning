# sub() replaces text that matches a regex pattern.
# It can be used to replace characters, words, spaces, or patterns.

import re

text = "Rat Cat Pat Mat Sat rat"

reg = re.compile(r"[Rr]at")
result = reg.sub("LION", text)

print(result)

#Example - 2
text = "How   are    you?"

result = re.sub(r"\s+", " ", text)

print(result)