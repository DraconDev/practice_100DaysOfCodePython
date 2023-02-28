import math
import tkinter as tk

# window = tkinter.Tk()
window = tk.Tk()
window.title('Miles to km')
# window.minsize(500, 300)
window.config(padx=10, pady=10)

# configure the grid
# window.columnconfigure(0, weight=1)
# window.columnconfigure(1, weight=3)

# Click event


def button_clicked():
    label_miles_in_km['text'] = math.trunc(int(input.get()) * 1.609344)
    # my_label.config(text='button click')
    print('click')

# Label


input = tk.Entry(width=10, )
input.grid(row=0, column=1)

label_miles = tk.Label(text='Miles', font=('Arial', 14))
label_miles.grid(row=0, column=2)

label_is_equal = tk.Label(text='is equal to', font=('Arial', 14))
label_is_equal.grid(row=1, column=0)

label_miles_in_km = tk.Label(text='0', font=('Arial', 14))
label_miles_in_km.grid(row=1, column=1)

label_km = tk.Label(text='Km', font=('Arial', 14))
label_km.grid(row=1, column=2)

button = tk.Button(text='Click me', command=button_clicked)
button.grid(row=2, column=1)


window.mainloop()
