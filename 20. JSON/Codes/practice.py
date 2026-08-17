import json

data = {
    "zebra": 1,
    "apple": 2,
    "mango": 3,
    "banana": 4
}

result = json.dumps(data, sort_keys= True)
print(result)