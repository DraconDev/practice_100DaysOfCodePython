import json

import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get("https://news.ycombinator.com/front?day=2022-02-13")

soup = BeautifulSoup(r.content, "html.parser")
container = soup.find("table")

news = container.find_all("span", class_="titleline")
news = [item.a.get_text() for item in news]
subtext = container.find_all("td", class_="subtext")
subtext = [item.get_text().replace("\n", "").replace("\xa0", " ") for item in subtext]
headlines = dict(zip(news, subtext))

highest_score = max(
    [
        int(item.get_text().split(" ")[0])
        for item in container.find_all("span", class_="score")
    ]
)

file = json.dumps({"news": headlines, "highest_score": highest_score}, indent=4)
with open("hackernews_data.json", "w") as f:
    f.write(file)

pass
