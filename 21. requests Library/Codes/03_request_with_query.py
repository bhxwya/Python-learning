import requests

# Query parameters to send with the GET request
payload = {
    "key1": "value1",
    "key2": "value2"
}

# Send GET request with query parameters
r = requests.get(
    "https://httpbin.org/get",
    params=payload
)

# Convert JSON response into a Python dictionary
print(r.json())


# NOTES:
# params={} sends query parameters with a GET request. (keyword argument of requests.get())
# Query parameters are added to the URL after '?' and separated by '&'.
# httpbin.org echoes the parameters received from our request. example : 
# https://httpbin.org/get?key1=value1&key2=value2