import time
import tkinter as tk

import schedule

WORK_MIN = 25 * 60
REST_MIN = 5 * 60
LONG_BREAK_MIN = 20 * 60

colors = ['#222831', '#393E46', '#00ADB5', '#EEEEEE']
# type_of_hours = 0
window = tk.Tk()
window.title('Pomodoro')
# window.minsize(500, 300)
window.config(padx=10, pady=10, bg=colors[0], )


button_colors = {'bg': colors[0], 'fg': colors[1]}
set = False
type_of_hours = ["WORK_MIN", "REST_MIN", "WORK_MIN", "REST_MIN",
                 "WORK_MIN", "REST_MIN", "WORK_MIN", 'LONG_BREAK_MIN']
clock_type = 0


def update_clock(count,):
    print(type_of_hours[clock_type])
    colors = {"WORK_MIN": 'green',
              "LONG_BREAK_MIN": 'orange', 'REST_MIN': 'black'}
    titles = {"WORK_MIN": 'Work',
              "LONG_BREAK_MIN": 'Long break', 'REST_MIN': 'Short rest'}
    canvas.itemconfig(
        canvas_text, text=f"{int(count/60) : 03d}:{count%60 : 03d}", fill=colors[type_of_hours[clock_type]])
    title['text'] = titles[type_of_hours[clock_type]]
    title['fg'] = colors[type_of_hours[clock_type]]


# schedule.every(1).seconds.do(up_type_of_hours)


timer = 0


def count_down(count,):

    global clock_type
    if count == 0:
        clock_type += 1
    if count >= 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
        update_clock(count,)
        print(count)
    else:
        checkmark['text'] += "✓"
        if clock_type == 7:
            count_down(LONG_BREAK_MIN, )
            clock_type = 0
        else:
            count_down(REST_MIN, )


# count_down(10)

def start_timer():
    global clock_type
    count_down(WORK_MIN, )


def reset_timer():
    window.after_cancel(timer)
    checkmark['text'] = ''
    canvas.itemconfig(
        canvas_text, text="00:00")
    # schedule.cancel_job(up_type_of_hours)


def test_mode():
    global WORK_MIN
    global REST_MIN
    WORK_MIN = 2
    REST_MIN = 2


# button_config = {"padx": 10, "pady": 5}


title = tk.Label(window, text="Timer",
                 bg=colors[0], fg=colors[1], font=('Ariel', 26, 'bold'))
title.grid(row=0, column=0, columnspan=2)

start = tk.Button(window, text="Start",
                  bg=colors[0], fg=colors[1], font=('Ariel', 26, 'bold'), command=start_timer, )
start.grid(row=4, column=0,  sticky=tk.EW,)

reset = tk.Button(window, text="Reset",
                  bg=colors[0], fg=colors[1], font=('Ariel', 26, 'bold'), command=reset_timer)
reset.grid(row=4, column=1, sticky=tk.EW)

title = tk.Label(window, text="Timer",
                 bg=colors[0], fg=colors[1], font=('Ariel', 26, 'bold'))
title.grid(row=0, column=0, columnspan=2)

test = tk.Button(window, text="test",
                 bg=colors[0], fg=colors[1], font=('Ariel', 26, 'bold'), command=test_mode)
test.grid(row=5, column=0,)

checkmark = tk.Label(window, text="",
                     bg=colors[0], fg="green", font=('Ariel', 26, 'bold'))
checkmark.grid(row=6, column=0,)

canvas = tk.Canvas(width="300", height='300',
                   bg=colors[1], highlightthickness=0)
tomato = tk.PhotoImage(file='./tomato.png')
canvas.create_image(150, 150, image=tomato)

canvas_text = canvas.create_text(150, 165, text='00:00', fill="white",
                                 font=('Ariel', 16, 'bold'))
# canvas_text = canvas.create_text(150, 150, text=0, fill="white",
#                                  font=('Ariel', 16, 'bold'))
canvas.grid(row=1, column=0, rowspan=2, columnspan=2)


window.mainloop()
