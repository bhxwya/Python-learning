import requests
from tqdm import tqdm


# URL of the file to download
url = "https://sample-files.com/downloads/audio/wav/ambient-sounds-96000hz-24bit.wav"

# stream=True → download the response gradually instead of loading
# the entire file into memory at once.
r = requests.get(url, stream=True)


# Content-Length → total size of the file in bytes.
totalExpectedBytes = int(r.headers["Content-Length"])


# Keeps track of how many bytes we have received.
bytesReceived = 0


# tqdm → creates a progress bar for the download.
progress_bar = tqdm(
    total=totalExpectedBytes,
    unit="iB",
    unit_scale=True
)


# Open/create the file in binary write mode.
with open("winrar.wav", "wb") as f:

    # Download the file piece by piece.
    for chunk in r.iter_content(chunk_size=128):

        # Update the progress bar by the size of the chunk received.
        progress_bar.update(128)

        # Write the downloaded chunk to the file.
        f.write(chunk)

        # Keep track of downloaded bytes.
        bytesReceived += 128


# Close the progress bar.
progress_bar.close()


# NOTES:
# stream=True → allows the response to be downloaded in chunks.
# r.iter_content() → gives the response data piece by piece.
# chunk_size=128 → each chunk is approximately 128 bytes.
# Content-Length → tells us the expected total file size.
# tqdm → displays a download progress bar.
# Streaming is useful for large files because the entire file
# does not need to be stored in memory at once.