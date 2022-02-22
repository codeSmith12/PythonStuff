from tkinter import *

class Cell:
    def __init(self, tk):
        self.value = " "
        self.Button = Button(tk, text= " ")

class Board:
    def __init__(self):
        tk = Tk()
        tk.geometry("300x400")
        tk.title("Tic Tac Toe")
        self.board = [[],[],[]]
        self.window = tk


board = Board()
board.window.mainloop()
