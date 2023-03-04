import tkinter as tk


class Window(tk.Tk):
    """docstring for Window."""

    def __init__(self, ):
        super(Window, self).__init__()
        self.title('')
        self.minsize(300, 300)
        # window.columnconfigure(0, weight=)
        # window.columnconfigure(1, weight=300)
        # window.resizable(0, 0)
        # self.turn_on = self.on

    # def on(self):
    #     self.mainloop()
