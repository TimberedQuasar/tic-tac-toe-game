from tkinter import *
from tkinter import ttk
#from main import *

class myGui:

    def __init__(self):

        self.root = Tk()
        self.root.title("Tic tac toe")

        self.content = ttk.Frame(self.root, padding=(5,5))
        self.label = ttk.Label(self.content, text="Tic tac toe\nThe game", justify='center')
        
        def next_window():
            self.content.forget()
            
            self.content = ttk.Frame(self.root, padding=(5,5))
            #update this label
            self.label = ttk.Label(self.content, text="It's O turn", justify='center')

            #update this buttons and disable them after activation
            self.one = ttk.Button(self.content, text="1")
            self.two = ttk.Button(self.content, text="2")
            self.three = ttk.Button(self.content, text="3")
            self.four = ttk.Button(self.content, text="4")
            self.five = ttk.Button(self.content, text="5")
            self.six = ttk.Button(self.content, text="6")
            self.seven = ttk.Button(self.content, text="7")
            self.eight = ttk.Button(self.content, text="8")
            self.nine = ttk.Button(self.content, text="9")

            self.content.grid(column=0, row=0, sticky=(N,S,E,W))
            self.label.grid(column=0, row=0, columnspan=3, sticky=(N,S), padx=10, pady=5)
            self.one.grid(column=0, row=1, sticky=(N,S,E,W), padx=5, pady=5)
            self.two.grid(column=1, row=1, sticky=(N,S,E,W), padx=5, pady=5)
            self.three.grid(column=2, row=1, sticky=(N,S,E,W), padx=5, pady=5)
            self.four.grid(column=0, row=2, sticky=(N,S,E,W), padx=5, pady=5)
            self.five.grid(column=1, row=2, sticky=(N,S,E,W), padx=5, pady=5)
            self.six.grid(column=2, row=2, sticky=(N,S,E,W), padx=5, pady=5)
            self.seven.grid(column=0, row=3, sticky=(N,S,E,W), padx=5, pady=5)
            self.eight.grid(column=1, row=3, sticky=(N,S,E,W), padx=5, pady=5)
            self.nine.grid(column=2, row=3, sticky=(N,S,E,W), padx=5, pady=5)

            self.root.columnconfigure(0, weight=1)
            self.root.rowconfigure(0, weight=1)
            self.content.columnconfigure(0, weight=2)
            self.content.columnconfigure(1, weight=2)
            self.content.columnconfigure(2, weight=2)
            self.content.rowconfigure(0, weight=2)
            self.content.rowconfigure(1, weight=2)
            self.content.rowconfigure(2, weight=2)
            self.content.rowconfigure(3, weight=2)

        #!!!ADD JUSTIFYIN TO TEXT IN BUTTON
        self.buttonOne = ttk.Button(self.content, text="Play\nvs\nplayer", command=next_window)
        self.buttonTwo = ttk.Button(self.content, text="Play\nvs\ncomputer", command=next_window)

        self.content.grid(column=0, row=0, sticky=(N,S,E,W))
        self.label.grid(column=0, row=0, columnspan=2, sticky=(N,S), padx=10, pady=5)
        self.buttonOne.grid(column=0, row=1, sticky=(N,S,E,W), padx=5, pady=5)
        self.buttonTwo.grid(column=1, row=1, sticky=(N,S,E,W), padx=5, pady=5)

        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.content.columnconfigure(0, weight=2)
        self.content.columnconfigure(1, weight=2)
        self.content.rowconfigure(1, weight=1)

        self.root.mainloop()

myGui()