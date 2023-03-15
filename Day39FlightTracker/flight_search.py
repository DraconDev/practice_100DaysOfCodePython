import os

import requests


class FlightSearch:
    """docstring for FlightSearch."""

    def __init__(
        self,
    ):
        super(FlightSearch, self).__init__()

        # Set the request parameters
        self.url = "https://api.kiwi.com/v2/search"
        self.key = os.getenv("KIWI_API_KEY")
        # self.headers = {"Authorization": f"Bearer {self.key}"}
        self.headers = {
            "accept": "application/json",
            "apikey": self.key,
        }
        # self.params = {
        #     "fly_from": "DUB",
        #     "fly_to": "LON",
        #     "date_from": "20/5/2023",
        #     "date_to": "30/12/2025",
        #     # "apikey": self.key
        #     # "typeFlight": "oneway",
        # }

        self.params = {
            "flyFrom": "DUB",
            "to": "LON",
            "dateFrom": "20/5/2023",
            "dateTo": "30/12/2023",
            "partner":
        }

    def get_flight(
        self,
    ):
        # response = requests.get(self.url, headers=self.headers, params=self.params)
        response = requests.get(self.url, params=self.params)
        print(response.json())
        return response.json()


# kiwi api call of a flight
