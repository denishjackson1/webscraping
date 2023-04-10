import requests
from bs4 import BeautifulSoup

URL = "http://olympus.realpython.org/profiles/aphrodite"

page = requests.get(URL)
html = page.text

# Create a BeautifulSoup Object
soup = BeautifulSoup(html, 'html.parser')

#Extract text from title
title = soup.find_all('title')
for t in title:
    print(t.get_text())

# Extract text from body.
body = soup.find_all('center')
for c in body:
    print(c.get_text())

print("Hello World")
