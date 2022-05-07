from tkinter import *


def drawGrid():
    colWidth = WIDTH/8
    # Draw the lines...
    for i in range(1, 9):
        canvas.create_line(colWidth*i, 0, colWidth*i, HEIGHT, fill="black")

    for i in range(8):
        canvas.create_oval(PADX + colWidth*i, PADY, PADX + CIRCLE_SIZE + colWidth*i, PADY+CIRCLE_SIZE, fill="white")

# Game Constants
WIDTH = 800
HEIGHT = 800
PADX = WIDTH//65 # <---
PADY = HEIGHT//65 # <---
CIRCLE_SIZE = WIDTH//10 # <---

tk = Tk()
tk.title("Connect 4")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background="lightblue")
canvas.pack()

drawGrid()

tk.mainloop()
