import requests

# Send a PUT request to update/replace data on the server
r = requests.put(
    "https://httpbin.org/put",
    data={"a": 1, "b": 3}
)

# Response body as text
print(r.text)


# NOTES:
# requests.put() sends a PUT request, generally used to update/replace data.
# data={} contains the data sent in the request body.
# Requests also supports other HTTP methods such as GET, POST, PUT, DELETE, etc.