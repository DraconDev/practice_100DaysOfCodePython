import json
import os

import openai


def analyze_input(text: str, instruction: str, save=True):

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
                "content": instruction,
            },
        ],
    )
    analyzed_text = analyzed_text["choices"][0]["message"]["content"]
    save_response(analyzed_text)
    return analyzed_text


def save_response(text):
    if not os.path.dirname("/data"):
        os.makedirs("/data")

    # with open("./data/analyzed_input.json", "w") as f:
    #     json.dump(text, f)
    pass
