import json
import os

import openai


def input_analyzer(text: str):

    openai.api_key = os.getenv("API_KEY_OpenAI")

    analyzed_text = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": text,
            },
            {
                "role": "user",
                "content": "Identify the type of exercise and approximate time spent doing it. Send the reply in a json format. No new lines or spaces",
            },
        ],
    )
    analyzed_text = analyzed_text["choices"][0]["message"]["content"]
    save_response(analyzed_text)
    return analyzed_text


def save_response(text):
    if not os.path.dirname("/data"):
        os.makedirs("/data")
    text = input_analyzer("I ran 20kms today")
    with open("./data/data.json", "w") as f:
        json.dump(text, f)
    pass


save_response()
