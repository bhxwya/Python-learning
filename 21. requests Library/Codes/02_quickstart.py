import requests

# Send a GET request
r = requests.get(
    "https://api.github.com/user",
    auth=("user", "pass")
)

# HTTP status code returned by the server
print(r.status_code)

# Response metadata
print(r.headers["content-type"])

# Character encoding of the response
print(r.encoding)

# Response body as text
print(r.text)

# Convert JSON response into a Python object
print(r.json())


# NOTES:
# r.status_code → HTTP status code of the response.
# r.headers → metadata about the response.
# r.encoding → character encoding used for response text.
# r.text → response body as a string.
# r.text → JSON response as a string (even if it looks like a dictionary)
# r.json() → converts a JSON response into a Python object.
# r.json() → parses JSON response into a Python object, usually dict/list