from tkinter import *


def drawGrid():
    colWidth = WIDTH/8
    # Draw the lines...
    for i in range(1, 9):
        canvas.create_line(colWidth*i, 0, colWidth*i, HEIGHT, fill="black")

    # Makes each row further down from the last...
    for j in range(8):
        # Draws a row of circles
        for i in range(8): # i = 0,1,2,3,4,5,6,7
            canvas.create_oval(PADX + colWidth*i, PADY+colWidth*j, PADX + CIRCLE_SIZE + colWidth*i, PADY+CIRCLE_SIZE + colWidth*j, fill="white")

def placeMarker(event):
    # print(event.x,event.y)
    colWidth = WIDTH/8 # == 100
    rowClicked = event.x // colWidth # 99 // 100
    print(rowClicked)


def displayBoard(board):
    for row in board:
        for col in row:
            print(f"{col}", end=" ")
        print("\n")


# Game Constants
WIDTH = 800
HEIGHT = 800
PADX = WIDTH//65 # <---
PADY = HEIGHT//65 # <---
CIRCLE_SIZE = WIDTH//10 # <---


global board
board = []
for i in range(8):
    board.append([0,0,0,0,0,0,0,0])

displayBoard(board)


tk = Tk()
tk.title("Connect 4")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background="lightblue")
canvas.bind("<Button-1>", placeMarker)
canvas.pack()

drawGrid()

tk.mainloop()
