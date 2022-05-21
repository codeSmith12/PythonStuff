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

def displayBoard(board):
    for row in board:
        for col in row:
            print(f"{col}", end=" ")
        print("\n")


def placeMarker(event):
    global player1Turn
    colWidth = WIDTH/8
    colClicked = int(event.x // colWidth)
    # Search bottom up for an empty slot.
    for i in range(7, -1, -1):
        # If the slot we are currently on is empty?
        if board[i][colClicked] == 0:
            # Place a marker for whoever's turn it is
            if player1Turn:
                board[i][colClicked] = 1
                canvas.create_oval(PADX + colWidth*colClicked, PADY+colWidth*i, PADX + CIRCLE_SIZE + colWidth*colClicked, PADY+CIRCLE_SIZE + colWidth*i, fill="blue")
            else:
                board[i][colClicked] = 2
                canvas.create_oval(PADX + colWidth*colClicked, PADY+colWidth*i, PADX + CIRCLE_SIZE + colWidth*colClicked, PADY+CIRCLE_SIZE + colWidth*i, fill="red")
            # Flip the turn boolean variable
            player1Turn = not player1Turn
            break
    displayBoard(board)
# Created the canvas, write this below it \/

# Game Constants
WIDTH = 800
HEIGHT = 800
PADX = WIDTH//65
PADY = HEIGHT//65
CIRCLE_SIZE = WIDTH//10

global player1Turn
player1Turn = True

# 1 in the board means player one's marker is there
# 2 in the board means player two's marker is there

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
