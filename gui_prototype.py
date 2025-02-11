from tkinter import *
from tkinter import ttk

class myGui:

    def __init__(self):

        self.root = Tk()
        self.root.title("Tic tac toe")

        self.content = ttk.Frame(self.root, padding=(5,5))
        self.label = ttk.Label(self.content, text="Tic tac toe\nThe game", justify='center')
        
        #!!!ADD JUSTIFYIN TO TEXT IN BUTTON
        self.buttonOne = ttk.Button(self.content, text="Play\nvs\nplayer")
        self.buttonTwo = ttk.Button(self.content, text="Play\nvs\ncomputer")

        self.content.grid(column=0, row=0, sticky=(N,S,E,W))
        self.label.grid(column=0, row=0, columnspan=2, sticky=N, padx=10, pady=5)
        self.buttonOne.grid(column=0, row=1, sticky=(N,S,E,W), padx=5, pady=5)
        self.buttonTwo.grid(column=1, row=1, sticky=(N,S,E,W), padx=5, pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=2)
        self.content.columnconfigure(1, weight=2)
        self.content.rowconfigure(1, weight=1)


        self.root.mainloop()

myGui()