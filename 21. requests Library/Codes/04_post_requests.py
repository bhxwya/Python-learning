import requests

# Send data to the server using a POST request
r = requests.post(
    "https://httpbin.org/post?a=b",
    data={"harry": "value"}
)

# Response body as text
print(r.text)


# NOTES:
# requests.post() sends data to a server using a POST request.
# data={} contains the data sent in the request body.
# Query parameters can still be included in the URL using ?key=value.

# GET  → usually used to request/get data
# POST → usually used to send/submit data