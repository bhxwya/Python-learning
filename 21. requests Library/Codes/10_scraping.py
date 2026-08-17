import requests

# Data Collection
links = [
    "https://www.codewithharry.com/blog",
    "https://www.codewithharry.com/videos",
    "https://www.codewithharry.com/contact"
]

for link in links:
    r = requests.get(link)

    with open(f"htmls/{link.split('/')[-1]}.html", "w", encoding="utf-8") as f:
        f.write(r.text)
        
        
# NOTES:
# requests.get() → downloads the webpage.
# r.text → HTML source code received from the webpage.
# link.split('/')[-1] → gets the last part of the URL to create the filename.
# This file collects webpages and saves their HTML locally.

# WEB SCRAPING:
# Scraping = automatically collecting useful data from websites using code.
# requests → downloads the webpage; BeautifulSoup → searches/parses its HTML.


# WITHOUT encoding="utf-8":
# Windows may use cp1252 → some Unicode characters cannot be saved → UnicodeEncodeError.

# WITH encoding="utf-8":
# UTF-8 supports a much wider range of Unicode characters → HTML saves correctly.