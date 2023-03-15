# make a user on pixela

import datetime
import json
import time

import requests


def get_login(name, extension="json", path="../../../_Login/_API"):
    try:
        with open(f"{path}/{name}.{extension}") as f:
            data = json.load(f)
        return data
    except FileNotFoundError:
        raise Exception("File not found")


user_data = get_login("pixela")
token = user_data["token"]
username = user_data["username"]


def make_user(username, token):
    url = "https://pixe.la/v1/users"

    payload = {
        "notMinor": "yes",
        "agreeTermsOfService": "yes",
        "token": token,
        "username": username,
    }

    # make a user on pixela
    response = requests.post(url=url, json=payload)
    print(response.text, response.status_code)

    print(payload)


# make_user(username, token)


def make_graph(token, username, id):
    url = f"https://pixe.la/v1/users/{username}/graphs"
    payload = {
        "id": id,
        "name": "DailyDevTracker",
        "unit": "Days",
        "type": "float",
        "color": "ajisai",
    }

    headers = {"X-USER-TOKEN": token}

    response = requests.post(url=url, json=payload, headers=headers)
    return response


# make_graph(token, username, id="graph2")


def post_pixel(token, username, id):
    date = time.strftime("%Y%m%d", time.localtime())
    url = f"https://pixe.la/v1/users/{username}/graphs/{id}"
    payload = {
        "date": str(date),
        "quantity": "2",
    }
    response = requests.post(url=url, json=payload, headers={"X-USER-TOKEN": token})
    return response


# post_pixel(token, username, id="graph2")


def update_pixel(token, username, id):
    date = time.strftime("%Y%m%d", time.localtime())
    url = f"https://pixe.la/v1/users/{username}/graphs/{id}/{date}"
    data = {
        # "date": str(date),
        "quantity": "3",
    }
    response = requests.put(url=url, json=data, headers={"X-USER-TOKEN": token})
    return response


# update_pixel(token, username, id="graph2")


def delete_pixel(token, username, id):
    date = time.strftime("%Y%m%d", time.localtime())
    url = f"https://pixe.la/v1/users/{username}/graphs/{id}/{date}"
    response = requests.delete(url=url, headers={"X-USER-TOKEN": token})
    return response


delete_pixel(token, username, id="graph2")
