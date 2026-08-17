# match() checks for a match only at the beginning of the string.
# It returns a match object if the pattern matches the beginning.

import re

text = "Tamanna is a good girl"

if re.match("Tamanna", text):
    print("Match found")