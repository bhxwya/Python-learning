import requests

# Send a GET request to the website
r = requests.get("https://www.codewithharry.com")

# Get the response body as text (HTML)
print(r.text)

# Save the HTML response into a local file
with open("index.html", "w") as f:
    f.write(r.text)


# NOTES:
# requests.get(url) sends a GET request and returns a Response object.
# r.text gives the response body as text, usually HTML for a webpage.
# HTML can be saved to a file using open() and write().