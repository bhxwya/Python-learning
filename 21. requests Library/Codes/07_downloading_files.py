import requests

url = "https://cdn.pixabay.com/download/audio/2023/08/26/audio_a6ee15a317.mp3?filename=kamhunt-sunflower-street-drumloop-85bpm-163900.mp3"

r = requests.get(url)

print(r.status_code)
print(r.headers.get("Content-Type"))
print(len(r.content))

fp = open("random.mp3", "wb")

fp.write(r.content)

fp.close()

