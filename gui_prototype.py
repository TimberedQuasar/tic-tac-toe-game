import tkinter as tk
from tkinter import *

class myGui:

    def __init__(self):
        self.root = tk.Tk()

        self.root.title("Tic tac toe")

        self.root.geometry("500x500")
        
        #home window
        """
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
        """

        #game window

        #word charackter is placeholder
        #character should change to O or X 
        #depending on which player has a turn
        self.game_header = tk.Label(self.root, text="It's charackter turn", font=('Arial', 18))
        self.game_header.pack(padx=20, pady=20)

        self.board = tk.Frame(self.root)
        self.board.columnconfigure(0, weight=1)
        self.board.columnconfigure(1, weight=1)
        self.board.columnconfigure(2, weight=1)

        #button should update their text
        #depending on which player use it
        #if someone used button
        #on top of the board (game_header)
        #should be information for a player
        #that he can't make that move
        self.btn1 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn1.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.btn2 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn2.grid(row=0, column=1, sticky=tk.W + tk.E)
        self.btn3 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn3.grid(row=0, column=2, sticky=tk.W + tk.E)
        self.btn4 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn4.grid(row=1, column=0, sticky=tk.W + tk.E)
        self.btn5 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn5.grid(row=1, column=1, sticky=tk.W + tk.E)
        self.btn6 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn6.grid(row=1, column=2, sticky=tk.W + tk.E)
        self.btn7 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn7.grid(row=2, column=0, sticky=tk.W + tk.E)
        self.btn8 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn8.grid(row=2, column=1, sticky=tk.W + tk.E)
        self.btn9 = tk.Button(self.board, text=" ", font=('Arial', 14))
        self.btn9.grid(row=2, column=2, sticky=tk.W + tk.E)

        self.board.pack(fill='x')


        self.root.mainloop()

myGui()