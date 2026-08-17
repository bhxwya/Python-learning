# loads() converts a JSON string into a Python object.
# "s" in loads means string.

import json

data = '{"var1": "harry", "var2": 56}'

parsed = json.loads(data)

print(parsed)
print(parsed["var1"])