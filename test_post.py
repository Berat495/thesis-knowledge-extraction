import requests
from bs4 import BeautifulSoup

url = "https://artanddance.art.blog/2026/02/25/david-teniers-the-bride-who-never-dances/"

soup = BeautifulSoup(requests.get(url).text, "html.parser")

for h1 in soup.find_all("h1"):
    print("H1:", h1.get_text(strip=True))