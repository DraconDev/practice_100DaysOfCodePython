import json
import os
import random
from tkinter import *

import requests


def get_quiz_data():
    response = requests.get(
        'https://opentdb.com/api.php?amount=10&category=20&type=boolean')
    response.raise_for_status()

    data = response.json()
    return data


def save_questions_to_file(data):
    with open('./data/questions.json', 'w') as f:
        f.write(json.dumps(data, indent=4))


def random_question(data):
    quiz = random.choice(data['results'])
    ask = random.choice(data['results'])['question'].replace('&quot;', '"')

    return (quiz, ask)


def build_ui(score_label, question_label, true_btn, false_btn):
    root = Tk()
    root.title("My Window")
    root.minsize(300, 0)

    frame1 = Frame(root)
    frame1.pack(side=TOP, fill=BOTH, expand=True)

    label_left = Label(frame1,)
    label_left.pack(side=LEFT, fill=X, expand=True)
    score_label.pack(side=LEFT, fill=X, expand=True)

    # create a label
    question_label.pack(fill=X, expand=True, )

    # create two buttons
    true_btn.pack(side=RIGHT, fill=X, expand=True)
    false_btn.pack(side=LEFT, fill=X, expand=True)

    return root


def start_quiz(data):
    quiz, ask = random_question(data)
    score = 0

    colors = ['#F7C8E0', '#DFFFD8', '#B4E4FF', '#95BDFF']

    score_label = Label(text=f'Score:{score}', font=('Arial', 15))
    question_label = Label(text=ask, height=10,
                           bg=colors[2], wraplength=300, font=('Arial', 15))

    def correct_answer():
        nonlocal score
        if quiz['correct_answer'] == 'True':
            score += 1
        quiz, ask = random_question(data)
        score_label['text'] = f'Score:{score}'
        question_label['text'] = ask

    def wrong_answer():
        nonlocal score
        if quiz['correct_answer'] == 'False':
            score += 1
        quiz, ask = random_question(data)
        score_label['text'] = f'Score:{score}'
        question_label['text'] = ask

    true_btn = Button(text="True", command=correct_answer, font=('Arial', 15))
    false_btn = Button(text="False", command=wrong_answer, font=('Arial', 15))

    root = build_ui(score_label, question_label, true_btn, false_btn)
    root.mainloop()


if __name__ == '__main__':
    quiz_data = get_quiz_data()

    save_questions_to_file(quiz_data)
    start_quiz(quiz_data)
    start_quiz(quiz_data)
