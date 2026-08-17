# PIL / Pillow:
# Pillow is a Python library used to open, edit, and save images.
# Import it with: from PIL import Image

# BytesIO:
# BytesIO creates a file-like object in memory from raw bytes.
# Useful when we have bytes (like r.content) but a library expects a file.

import requests
from PIL import Image
from io import BytesIO

# Download the image
r = requests.get("https://downloadscdn6.magnific.com/488145/4/3540.jpg?filename=closeup-scarlet-macaw-from-side-view-scarlet-macaw-closeup-head.jpg&token=exp=1786878323~hmac=f1e090ddf2e2dd57700452dd556e283f&filename=3540.jpg")

# Convert downloaded bytes into an image
i = Image.open(BytesIO(r.content))

# Open a file in binary write mode
fp = open("img.jpg", "wb")

# Save the image
i.save(fp)

# Close the file
fp.close()


# NOTES:
# r.content → raw response data returned as bytes; useful for images, files, and binary data.
# BytesIO() lets bytes be treated like a file.
# Pillow (PIL) is used to open and save images.
