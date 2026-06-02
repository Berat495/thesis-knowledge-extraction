import requests
from bs4 import BeautifulSoup

url = "https://artanddance.art.blog/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

post_links = set()

for link in soup.find_all("a", href=True):
    href = link["href"]

    if "/2026/" in href:
        post_links.add(href)

print(f"Gevonden posts: {len(post_links)}")

for post in sorted(post_links):
    print(post)