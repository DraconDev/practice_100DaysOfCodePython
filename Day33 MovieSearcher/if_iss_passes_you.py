import json
import os
import time

import requests

latitude = 53.692946
longitude = -0.311706


def iss_location():
    response = requests.get('http://api.open-notify.org/iss-now.json')
    response.raise_for_status()
    if not os.path.exists('./data'):
        os.mkdir('data')
    return response.json()['iss_position']


def check_coordinates():

    position = iss_location()
    while True:
        lat_pos = float(position['latitude'])
        long_pos = float(position['longitude'])
        if latitude - 5 < lat_pos < latitude + 5 and longitude - 5 < long_pos < longitude + 5:
            print('ISS is passing my coordinates!')
            with open('./data/iss.json', 'w') as f:
                f.write(json.dump(position))
        else:
            print('ISS is not passing my coordinates.')

        time.sleep(10)


check_coordinates()
