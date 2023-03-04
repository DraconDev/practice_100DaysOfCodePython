import random
import tkinter as tk

import pandas
from window_class import Window

colors = ['#222831', '#393E46', '#00ADB5', '#EEEEEE']

window = Window()
window.title('Flashcard')


data = pandas.read_csv('./translate most common 100 french words - Sheet1.csv')
data.to_dict()
data = {row.French: row.English for i, row in data.iterrows()}


card_list = list(data.keys())
card_to_review_later = []


def go_again():
    global rand_card
    rand_card = random_card()
    print(rand_card)
    canvas.itemconfig(
        canvas_text, text=rand_card,)
    canvas.itemconfig(
        canvas_image, image=flash_front,)
    return


def random_card():
    return random.choice(card_list)


def correct_answer():
    card_to_review_later.append(rand_card)
    card_list.remove(rand_card)
    review_label['text'] = f"Review:{len(card_to_review_later)}"
    go_again()


rand_card = random_card()


padding = {'padx': 5, 'pady': 5, 'ipadx':  10, 'ipady': 10}
padding_button = {'padx': 10, 'pady': 10, 'ipadx':  10, 'ipady': 10}


canvas = tk.Canvas(width="300", height='300',
                   bg=colors[1], highlightthickness=0)
# print(canvas.i)
flash_front = tk.PhotoImage(file='./images/card_front.png')
flash_back = tk.PhotoImage(file='./images/card_back.png')
canvas_image = canvas.create_image(150, 150, image=flash_front)
canvas_text = canvas.create_text(150, 150, text=rand_card, fill="black",
                                 font=('Ariel', 16, 'bold'))
canvas.pack(fill=tk.BOTH, expand=True, ** padding, )


def show_card():
    if canvas.itemcget(canvas_text, 'text') == data[rand_card]:
        canvas.itemconfig(
            canvas_text, text=rand_card,)
        canvas.itemconfig(
            canvas_image, image=flash_front,)
    else:
        canvas.itemconfig(
            canvas_text, text=data[rand_card],)
        canvas.itemconfig(
            canvas_image, image=flash_back,)


no_button = tk.Button(window, text="Again",
                      bg=colors[0], fg=colors[2], font=('Ariel', 14, 'bold'), command=go_again)
no_button.pack(**padding_button, fill=tk.BOTH, expand=True, side=tk.LEFT)

show_button = tk.Button(window, text="Show",
                        bg=colors[0], fg=colors[2], font=('Ariel', 14, 'bold'), command=show_card)
show_button.pack(**padding_button, fill=tk.BOTH, expand=True, side=tk.LEFT)

yes_button = tk.Button(window, text="Good",
                       bg=colors[0], fg=colors[2], font=('Ariel', 14, 'bold'), command=correct_answer, )
yes_button.pack(**padding_button, fill=tk.BOTH, expand=True, side=tk.LEFT)

review_label = tk.Label(window, text=f"Review:{len(card_to_review_later)}",
                        fg=colors[1], font=('Ariel', 14, 'bold'), )
review_label.place(x=0, y=0)


window.mainloop()
