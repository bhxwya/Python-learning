import requests

# PROXY SERVER

# Proxy = middleman between our program and the website.
# Normal: Python → Website
# Proxy:  Python → Proxy → Website

http_proxy = "http://USERNAME:PASSWORD@HOST:PORT"
https_proxy = "http://USERNAME:PASSWORD@HOST:PORT"

proxies = {
    "http": http_proxy,
    "https": https_proxy
}

r = requests.get(
    "https://httpbin.org/get",
    proxies=proxies
)

print(r.text)

# proxies=proxies → tells Requests to send the request through the proxy.
# "http"/"https" → specify which protocol uses each proxy.
# Proxy can be used to route requests through another server/IP.