# dumps() converts a Python object into a JSON-formatted string.
# "s" in dumps means string.

import json

data = {
    "channel_name": "CodeWithHarry",
    "cars": ["bmw", "audi a8", "ferrari"],
    "fridge": ("roti", 540),
    "isbad": False
}

jscomp = json.dumps(data)

print(jscomp)