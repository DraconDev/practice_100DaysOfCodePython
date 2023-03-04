import json
import os
import random
from tkinter import *

import requests

# get 50 quiz questions
response = requests.get(
    'https://opentdb.com/api.php?amount=10&category=20&type=boolean')
response.raise_for_status

data = response.json()
score = 0

colors = ['#F7C8E0', '#DFFFD8', '#B4E4FF', '#95BDFF']


# response to file check if it exists
if not os.path.exists('./data/'):
    os.mkdir('./data')
with open('./data/questions.json', 'w') as f:
    f.write(json.dumps(data, indent=4))


quiz = random.choice(data['results'])
ask = random.choice(data['results'])['question'].replace('&quot;', '"')


print(quiz)


def random_question():
    global quiz
    global ask
    quiz = random.choice(data['results'])
    ask = random.choice(data['results'])['question'].replace('&quot;', '"')


def correct_answer():
    global score
    if quiz['correct_answer'] == 'True':
        score += 1
    random_question()
    score_label['text'] = f'Score:{score}'
    lbl['text'] = ask


def wrong_answer():
    global score
    if quiz['correct_answer'] == 'False':
        score += 1
    random_question()
    score_label['text'] = f'Score:{score}'
    lbl['text'] = ask


root = Tk()
root.title("My Window")
root.minsize(300, 0)

frame1 = Frame(root)
frame1.pack(side=TOP, fill=BOTH, expand=True)


label_left = Label(frame1, )
label_left.pack(side=LEFT, fill=X, expand=True)
score_label = Label(frame1, text=f'Score:{score}',  font=('Arial', 15))
score_label.pack(side=LEFT, fill=X, expand=True, )

# create a label
lbl = Label(root, text=ask, height=10,
            bg=colors[2], wraplength=300, font=('Arial', 15))

lbl.pack(fill=X, expand=True, )
# create two buttons
btn1 = Button(root, text="True", command=correct_answer, font=('Arial', 15))

btn1.pack(side=RIGHT, fill=X, expand=True)
btn2 = Button(root, text="False",  command=wrong_answer, font=('Arial', 15))
btn2.pack(side=LEFT, fill=X, expand=True)

mainloop()
