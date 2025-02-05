import tkinter as tk
from tkinter import *

class myGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Tic tac toe")

        self.header = tk.Label(self.root, text="Tic tac toe\nThe game", font=('Arial', 20))
        self.header.pack(padx=20, pady=20)

        self.root.mainloop()

myGui()