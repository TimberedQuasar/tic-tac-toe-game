from tkinter import *
from tkinter import ttk

class myGui:

    def __init__(self):

        self.root = Tk()
        self.root.title("Tic tac toe")

        self.content = ttk.Frame(self.root)
        self.label = ttk.Label(self.content, text="Tic tac toe\nThe game" )
        
        self.buttonOne = ttk.Button(self.content, text="Play\nvs\nplayer")
        self.buttonTwo = ttk.Button(self.content, text="Play\nvs\ncomputer")

        self.content.grid(column=0, row=0)
        self.label.grid(column=0, row=0, columnspan=2)
        self.buttonOne.grid(column=0, row=1)
        self.buttonTwo.grid(column=1, row=1)


        self.root.mainloop()

myGui()