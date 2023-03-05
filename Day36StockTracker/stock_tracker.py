import json
import os

import requests

from get_news import get_news
from send_sms import send_sms

api_key = os.environ.get('API_KEY_ALPHA_VANTAGE')
url = "https://www.alphavantage.co/query"

params = {
    'apikey': api_key,
    'function': 'TIME_SERIES_DAILY_ADJUSTED',
    'datatype': 'json',
    'symbol': 'TSLA',
}

try:
    # api call to alpha vantage api with headers

    response = requests.get(url, params=params)
    response.raise_for_status()  # Check if there is an error or not
    data = response.json()

    data_daily = list(data['Time Series (Daily)'].values())[:10]
    stock_volume = 0
    stock_price_current = data_daily[0]['1. open']
    stock_price_10_day_old = data_daily[-1]['1. open']
    stock_price_yesterday_close = data_daily[-1]['4. close']

    for item in data_daily:
        stock_volume += int(item['6. volume'])
        pass

    print(
        f'In the last 10 days trading vomune was {stock_volume} and prince changed to {stock_price_current} from {stock_price_10_day_old}')

    news = get_news()

    def check_stock_rise():
        # If price dropped
        if stock_price_current < stock_price_yesterday_close:
            send_sms(news)
            pass

    check_stock_rise()

    if not os.path.exists("data"):  # Checking for existence of directory
        os.mkdir("data")

    with open('data/data.json', 'w') as f:
        json.dump(data, f)

finally:
    response.close()  # Release the system resources
