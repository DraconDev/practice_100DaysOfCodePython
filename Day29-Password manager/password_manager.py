import json
import random
import re
import string
import tkinter as tk
from tkinter import messagebox

import pandas as pd

colors = ['#181823', '#537FE7', '#C0EEF2', '#E9F8F9']

window = tk.Tk()
window.title('Password Manager')
# window['bg'] = 'black'

image_password = tk.PhotoImage(file='./logo.png')

canvas = tk.Canvas(width='220', height='220',)
canvas_image = canvas.create_image(110, 110, image=image_password)
canvas.pack()


# validate email format


def validate_email(email):
    if len(email) > 7:
        if re.match("^.+@(\[?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True

    return False

# def save_entries():
#     if is_valid_email(input_email.get()) is False:
#         messagebox.showinfo("Error", "Invalid email")
#         return
#     if len(input_password.get()) < 7:
#         messagebox.showinfo("Error", "Password needs to be at least 8 chars")
#         return
#     login_info= {"Website": input_website.get(), "Email": input_email.get(),
#                   "Password": input_password.get()}
#     confirm = messagebox.askyesno(
#         login_info['Website'], f"Save login information for {login_info['Website']}?")
#     if confirm:
#         try:
#             df = pd.read_csv('./data/saved_passwords.csv')
#             new_df = pd.DataFrame(login_info, index=[len(df)])
#             # new_df = new_df.reset_index(drop=True)
#             df = pd.concat([df, new_df], ignore_index=True)
#         except FileNotFoundError:
#             df = pd.DataFrame(login_info, index=[0])
#         df.to_csv('./data/saved_passwords.csv', index=False)
#         input_email.delete(0, tk.END)
#         input_password.delete(0, tk.END)
#         input_website.delete(0, tk.END)


# append to user_info.json new login information
def save_user_info():
    email = input_email.get()
    password = input_password.get()
    website = input_website.get()

    if not validate_email(email):
        messagebox.showinfo("Error", "Invalid email")
        return

    if len(password) < 8:
        messagebox.showinfo("Error", "Password needs to be at least 8 chars")
        return

    login_info = {
        website: {
            "Email": email,
            "Password": password
        }
    }

    confirm = messagebox.askyesno(
        website, f"Save login information for {website}?")
    if confirm:
        try:
            with open('./data/user_info.json', 'r') as f:
                existing_data = json.load(f)
        except FileNotFoundError:
            existing_data = {}

        existing_data.update(login_info)

        with open('./data/user_info.json', 'w') as f:
            json.dump(existing_data, f, indent=4)

    input_email.delete(0, tk.END)
    input_password.delete(0, tk.END)
    input_website.delete(0, tk.END)


# search for website in user_info.json
def search_user_info():
    website = input_website.get()
    try:
        with open('./data/user_info.json', 'r') as f:
            existing_data = json.load(f)
    except FileNotFoundError:
        existing_data = {}

    if website in existing_data:
        email = existing_data[website]['Email']
        password = existing_data[website]['Password']
        input_email.delete(0, tk.END)
        input_email.insert(0, email)
        input_password.delete(0, tk.END)
        input_password.insert(0, password)
    else:
        messagebox.showinfo("Error", f"Website {website} not found")


def generate_password():
    password = "".join([random.choice(string.ascii_letters)
                        for i in range(16)])
    input_password.delete(0, tk.END)
    input_password.insert(0, password)


# *input field
padding = {'padx': 5, 'pady': 5, 'ipadx':  0, 'ipady': 0}

div_first_row = tk.Frame(window,)
div_first_row.pack(fill='both', expand=True)

label_website = tk.Label(div_first_row, text='Website:', width=8,
                         fg=colors[0], )
label_website.pack(**padding, side=tk.LEFT, fill='both', expand=False, )

input_website = tk.Entry(div_first_row, text='Website',
                         fg=colors[0], )
input_website.pack(**padding, side=tk.LEFT, fill='both', expand=True)

# button that searches for website in user_info.json
button_search = tk.Button(div_first_row, text='Search',
                          fg=colors[0], command=search_user_info, width=14)
button_search.pack(**padding, side=tk.LEFT, fill='none', expand=False)

div_second_row = tk.Frame(window)
div_second_row.pack(fill='both', expand=True)

div_second_row = tk.Frame(window)
div_second_row.pack(fill='both', expand=True)

label_email = tk.Label(div_second_row, text='Email:', width=8,
                       fg=colors[0], justify=tk.RIGHT)
label_email.pack(**padding, side=tk.LEFT, fill='none', expand=False)

input_email = tk.Entry(div_second_row, text='email',  fg=colors[0], )
input_email.pack(**padding, side=tk.LEFT, fill='both', expand=True)

div_third_row = tk.Frame(window)
div_third_row.pack(fill='both', expand=True)

label_password = tk.Label(div_third_row, text='Password:',  width=8,
                          fg=colors[0], justify=tk.RIGHT)
label_password.pack(**padding, side=tk.LEFT, fill='none',)

input_password = tk.Entry(div_third_row, text='password',  fg=colors[0], )
input_password.pack(**padding, side=tk.LEFT, fill='both', expand=True)

button_generate_password = tk.Button(
    div_third_row, text='Generate password',  fg=colors[0], command=generate_password, width=14)
button_generate_password.pack(
    **padding, side=tk.LEFT, fill='none', expand=False)

div_forth_row = tk.Frame(window)
div_forth_row.pack(fill='both', expand=True)

button_store_input = tk.Button(
    div_forth_row, text='Store password',  fg=colors[0], command=save_user_info, width=14)
button_store_input.pack(**padding, side=tk.RIGHT, fill='none', expand=False)


window.mainloop()

window.mainloop()
window.mainloop()
window.mainloop()
window.mainloop()
