import tkinter as tk

window = tk.Tk()
window.minsize(500, 300)


# Label
# greeting = tk.Label(text="Hello, Tkinter", fg='white',
#                     bg='black', width='30', height='10')
# greeting.pack()

# box1 = tk.Label(window, text="Box 1", bg="green", fg="white")
# box1.pack(ipadx=20, ipady=20, anchor=tk.N,  expand=True, side=tk.TOP)


# box 1
box1 = tk.Label(window, text="Box 1", bg="green", fg="white")
box1.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.LEFT)

# box 2
box2 = tk.Label(window, text="Box 2", bg="red", fg="white")
box2.pack(ipadx=20, ipady=20, fill=tk.BOTH, expand=True, side=tk.RIGHT)


# # Button
# button = tk.Button(
#     text="Click me!",
#     width=25,
#     height=5,
#     bg="blue",
#     fg="yellow",
# )
# # button.pack(fill=tk.BOTH, expand=True)


window.mainloop()
