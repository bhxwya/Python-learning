# sort_keys=True sorts dictionary keys alphabetically in the JSON output.
# It does not change the original dictionary.

import json

data = {
    "zebra": 1,
    "apple": 2,
    "mango": 3,
    "banana": 4
}

result = json.dumps(data, sort_keys=True)

print(result)