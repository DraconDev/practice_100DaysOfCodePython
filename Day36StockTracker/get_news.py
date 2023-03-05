import json
import os

import requests


def get_news():
    with open('../../../_Login/_API/news.txt') as f:
        apikey = f.read().strip()

    params = {"sources": "bbc-news", "apiKey": apikey}
    url = 'https://newsapi.org/v2/top-headlines'

    response = requests.get(url, params=params)

    with open('news.json', 'w') as news:
        json.dump(response.json(), news)

    data = response.json()['articles'][:3]
    data = [item['title'] for item in data]

    top_news = ''
    for item in data:
        top_news += item + '\n'
    return top_news
