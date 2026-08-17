# dump() converts a Python object into JSON and writes it to a file.
# It is the file version of dumps().

import json

data = {
    "name": "Ansh",
    "age": 22,
    "skills": ["Python", "C++"]
}

with open("data.json", "w") as file:
    json.dump(data, file)