import json

import requests
from bs4 import BeautifulSoup

response = requests.get(f"https://www.empireonline.com/movies/features/best-movies-2/")
soup = BeautifulSoup(response.content, "html.parser")

with open("test.html", "w", encoding="utf-8") as file:
    file.write(str(soup))

titles_raw = soup.find_all("div", class_="listicle-item")

title_formatted = {
    str(100 - count): item.get_text().split("of")[-1].strip()
    for count, item in enumerate(titles_raw)
}

pass

with open("movies.json", "w") as file:
    json.dump(title_formatted, file)
