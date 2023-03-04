import os

import requests

latitude = 53.692946
longitude = -0.311706


# make a request to the server with 2 arguments

querystring = {"lat": latitude, "lng": longitude, 'date': 'today'}


response = requests.get(
    "https://api.sunrise-sunset.org/json", params=querystring)
response.raise_for_status()

if not os.path.exists('./data'):
    os.mkdir('data')
with open('./data/sunrise.json', 'w') as f:
    f.write(response.text)
