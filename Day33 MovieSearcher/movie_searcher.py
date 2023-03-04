import json
import os
import tkinter as tk

import requests


# search for a movie
def fetch_search_results(search_term):
    try:
        with open('e:/_Drive/_Dev/_Login/_API/IMDBAPI.json', 'r') as f:
            api_login = json.load(f)

        url = "https://imdb8.p.rapidapi.com/auto-complete"
        querystring = {"q": search_term}

        headers = {
            "X-RapidAPI-Key": api_login['key'],
            "X-RapidAPI-Host": api_login['host']
        }

        response = requests.request(
            "GET", url, headers=headers, params=querystring)

        # write response to result file
        if not os.path.exists('./data'):
            os.mkdir('data')
        with open('./data/result.json', 'w') as f:
            f.write(response.text)

        print(response.json()['d'][0])

        list_search_results(response.json()['d'])

    except FileNotFoundError:
        print("Login file not found")

# read search box and return it's value


def search():
    search_term = search_box.get()
    if len(search_term) > 1:
        fetch_search_results(str(search_term))
    return


# Give all elements 5px padding
root = tk.Tk()
root.minsize(500, 350)


# 5 px padding to be passed to all the elements
padding = {'padx': '5', 'pady': '5'}

# creating a label
label1 = tk.Label(root, text="Search for a movie:")
label1.pack(**padding)

search_bar = tk.Frame(root)
search_bar.pack(**padding, fill=tk.X, expand=False)

# creating a text entry box
search_box = tk.Entry(search_bar, width=30)
search_box.pack(**padding, fill=tk.BOTH, expand=True, side=tk.LEFT)

# creating a button widget
button1 = tk.Button(search_bar, text="Search", command=search, )
button1.pack(side=tk.RIGHT, **padding)

search_results = tk.Frame(root)
search_results.pack(**padding, fill=tk.BOTH, expand=True)


def list_search_results(results):
    print(results)

    # for item in results:
    #     tk.Label(root, text=item['l']).pack(**padding)
    # results = [i for i in range(1, 9)]
    # for item in results:
    #     tk.Label(search_results, text='hey').pack(**padding)

    for item in results:
        tk.Label(search_results, text=item['l']).pack(**padding)


# list_search_results(range(1, 9))


# run infinitely
root.mainloop()
