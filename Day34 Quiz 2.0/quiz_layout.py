import json
import os
import random
from tkinter import *

import requests


class QuizApp:
    def __init__(self):
        self.response = requests.get(
            'https://opentdb.com/api.php?amount=10&category=20&type=boolean')
        self.response.raise_for_status()

        self.data = self.response.json()['results']
        self.score = 0

        self.colors = ['#F7C8E0', '#DFFFD8', '#B4E4FF', '#95BDFF']

    def save_questions_to_file(self):
        if not os.path.exists('./data/'):
            os.mkdir('./data')

        with open('./data/questions.json', 'w') as f:
            f.write(json.dumps(self.data, indent=4))

    def start_quiz(self):
        self.random_question()

        self.root = Tk()
        self.root.title("My Window")
        self.root.minsize(300, 0)

        self.frame1 = Frame(self.root)
        self.frame1.pack(side=TOP, fill=BOTH, expand=True)

        self.label_left = Label(self.frame1)
        self.label_left.pack(side=LEFT, fill=X, expand=True)

        self.score_label = Label(
            self.frame1, text=f'Score:{self.score}', font=('Arial', 15))
        self.score_label.pack(side=LEFT, fill=X, expand=True)

        self.lbl = Label(self.root, text=self.ask, height=10,
                         bg=self.colors[2], wraplength=300, font=('Arial', 15))

        self.lbl.pack(fill=X, expand=True, )

        self.btn1 = Button(self.root, text="True",
                           command=self.correct_answer, font=('Arial', 15))
        self.btn1.pack(side=RIGHT, fill=X, expand=True)

        self.btn2 = Button(self.root, text="False",
                           command=self.wrong_answer, font=('Arial', 15))
        self.btn2.pack(side=LEFT, fill=X, expand=True)

        self.root.mainloop()

    def random_question(self):
        self.quiz = random.choice(self.data)
        self.ask = self.quiz['question'].replace('&quot;', '"')

    def correct_answer(self):
        if self.quiz['correct_answer'] == 'True':
            self.score += 1

        self.random_question()
        self.score_label['text'] = f'Score:{self.score}'
        self.lbl['text'] = self.ask

    def wrong_answer(self):
        if self.quiz['correct_answer'] == 'False':
            self.score += 1

        self.random_question()
        self.score_label['text'] = f'Score:{self.score}'
        self.lbl['text'] = self.ask


if __name__ == '__main__':
    quiz_app = QuizApp()

    quiz_app.save_questions_to_file()
    quiz_app.start_quiz()
