# load() reads JSON data from a file and converts it into a Python object.
# It is the file version of loads().

import json

with open("data.json", "r") as file:
    data = json.load(file)

print(data)