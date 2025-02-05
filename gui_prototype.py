import tkinter as tk
from tkinter import *

class myGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Tic tac toe")

        self.root.geometry("500x500")

        self.header = tk.Label(self.root, text="Tic tac toe\nThe game", font=('Arial', 20))
        self.header.pack(padx=20, pady=20)

        self.button_column = tk.Frame(self.root)
        self.button_column.columnconfigure(0, weight=1)
        self.button_column.columnconfigure(1, weight=1)

        self.btn1 = tk.Button(self.button_column, text="Play\nVS\nPlayer", font=('Arial', 16))
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)

        self.btn2 = tk.Button(self.button_column, text="Play\nVS\nComputer", font=('Arial', 16))
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)

        self.button_column.pack(fill='x')

        self.root.mainloop()

myGui()