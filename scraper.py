import json
import requests
from bs4 import BeautifulSoup

BASE_URL = "https://artanddance.art.blog/"

post_links = set()

response = requests.get(BASE_URL)
soup = BeautifulSoup(response.text, "html.parser")

for link in soup.find_all("a", href=True):
    href = link["href"]

    if "artanddance.art.blog/2026/" in href:
        post_links.add(href)

all_posts = []

for url in sorted(post_links):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    h1_tags = soup.find_all("h1")

    if len(h1_tags) > 1:
        title = h1_tags[1].get_text(strip=True)
    else:
        title = "No title"

    date = soup.find("time").get_text(strip=True) if soup.find("time") else "No date"

    paragraphs = soup.find_all("p")
    content = "\n".join(
        p.get_text(" ", strip=True)
        for p in paragraphs
        if p.get_text(strip=True)
    )

    tags = []
    for link in soup.find_all("a", href=True):
        if "/tag/" in link["href"]:
            tags.append(link.get_text(strip=True))

    post_data = {
        "url": url,
        "title": title,
        "date": date,
        "content": content,
        "tags": list(set(tags))
    }

    all_posts.append(post_data)

with open("data/posts.json", "w", encoding="utf-8") as file:
    json.dump(all_posts, file, indent=4, ensure_ascii=False)

print(f"{len(all_posts)} posts opgeslagen in data/posts.json")