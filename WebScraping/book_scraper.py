import json
import re

import requests
from bs4 import BeautifulSoup


class BookRatings:
    """docstring for BookRatings."""

    regex = f"[0-9,.]+"

    def __init__(self, section="psychology"):
        super(BookRatings, self).__init__()
        self.base_link = "https://goodreads.com/shelf/show/"
        self.section = section
        self.link = f"{self.base_link}{self.section}"

    def book_list(self, pages: int) -> dict:
        params = {
            "page": pages,
        }
        # r = requests.get(self.link, params=params)
        r = requests.get("https://www.goodreads.com/shelf/show/psychology?page=2")
        soup = BeautifulSoup(r.content, "lxml")
        # with open("test.html", "w", encoding="utf-8") as file:
        #     file.write(str(soup))
        container = soup.find("div", "leftContainer")
        rows = container.find_all("div", class_="left")

        book_ratings_raw = {
            item.a.get("title"): item.find("span", class_="smallText").get_text()
            for item in rows
        }

        book_ratings_formatted = {}
        for k, v in book_ratings_raw.items():
            rating, num_ratings, year = re.findall(self.regex, v)[:3]
            book_ratings_formatted[k] = {
                "rating": float(rating),
                "number_of_ratings": int(num_ratings.replace(",", "")),
                "year_of_release": int(year),
            }

        return book_ratings_formatted

    def book_lists(
        self,
        pages=1,
    ):
        result = {}
        for i in range(1, pages + 1):
            result.update(self.book_list(i))
        return result
