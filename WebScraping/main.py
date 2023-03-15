import json

from book_scraper import BookRatings


def main():
    book_rate = BookRatings()
    book_ratings = book_rate.book_lists(4)

    with open("book_ratings.json", "w") as f:
        json.dump(book_ratings, f)

    pass


if __name__ == "__main__":
    main()
