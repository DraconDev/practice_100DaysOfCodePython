import tkinter as tk

# window = tkinter.Tk()
window = tk.Tk()
window.title('Test tk')
window.minsize(500, 300)
window.config(padx=10, pady=10)

# Label
my_label = tk.Label(text='Hello', font=('Arial', 24, 'bold'))
# my_label.pack(fill='both', expand='true')
my_label.grid(row=0, column=1)


# Button


def button_clicked():
    label_miles_in_km['text'] = input.get() 
    # my_label.config(text='button click')
    print('click')

# Entry


button = tk.Button(text='Click me', command=button_clicked)
button.grid(row=0, column=0)

input = tk.Entry(width=10)
input.grid(row=2, column=2)


button = tk.Button(text='Click me', command=button_clicked)
button.grid(row=3, column=4)

button = tk.Button(text='Click me', command=button_clicked)
button.grid(row=0, column=2)
