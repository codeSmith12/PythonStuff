from tkinter import *


def drawGrid():
    colWidth = WIDTH/8
    # Draw the lines...
    for i in range(1, 9):
        canvas.create_line(colWidth*i, 0, colWidth*i, HEIGHT, fill=LINE_COLOR)

    # Draw circles
    for i in range(8):
        for j in range(8):
            canvas.create_oval(PADX + colWidth*j, PADY+colWidth*i, PADX + CIRCLE_SIZE + colWidth*j, PADY+CIRCLE_SIZE+colWidth*i, fill=CIRCLE_COLOR)

def placeMarker(event):
    global board, playerTurn
    colWidth = WIDTH/8
    # Calculate which row was clicked on using event X, convert to int for indexing later
    rowClicked = int(event.x // colWidth)
    # Fill in the board from the bottom up, alternating turns.
    for i in range(7,-1,-1):
        # Iterate from bottom up, find the first open slot.
        if board[i][rowClicked] == 0:
            if playerTurn:
                board[i][rowClicked] = 1
                canvas.create_oval(PADX + colWidth*rowClicked, PADY+colWidth*i, PADX + CIRCLE_SIZE + colWidth * rowClicked, PADY+CIRCLE_SIZE+colWidth*i, fill=PLAYER1_COLOR)
            else:
                board[i][rowClicked] = 2
                canvas.create_oval(PADX + colWidth*rowClicked, PADY+colWidth*i, PADX + CIRCLE_SIZE + colWidth * rowClicked, PADY+CIRCLE_SIZE+colWidth*i, fill=PLAYER2_COLOR)
            # Flip players turn, break so only one marker is placed.
            playerTurn = not playerTurn
            break

    checkWinner(board)

def checkRows(board):
    P1Score = 0
    P2Score = 0
    for row in board:
        for col in row:
            if P1Score == 4:
                print("Player 1 has won! Row")
                return
            elif P2Score == 4:
                print("Player 2 has won! Row")
                return

            if col == 1:
                P2Score = 0
                P1Score += 1
            elif col == 2:
                P1Score = 0
                P2Score += 1

def checkCols(board):
    displayBoard(board)
    P1Score = 0
    P2Score = 0
    for col in range(8):
        for row in range(8):
            if P1Score == 3:
                print("Player 1 has won! Col")
            elif P2Score == 3:
                print("Player 2 has won via! Col")

            if board[row][col] == 1:
                P2Score = 0
                P1Score += 1
            elif board[row][col] == 2:
                P1Score = 0
                P2Score += 1
        # Reset the counters between cols
        P1Score=0
        P2Score=0


def checkDiags(board):
    pass

def checkWinner(board):
    checkRows(board)
    checkCols(board)
    checkDiags(board)


def displayBoard(board):
    for row in board:
        for col in row:
            print(f"{col}", end=" ")
        print("\n")

# Game Constants
WIDTH = 1200
HEIGHT = 1200
PADX = WIDTH//65
PADY = HEIGHT//65
CIRCLE_SIZE = WIDTH//10
BACKGROUND_COLOR = "black"
CIRCLE_COLOR = "grey"
LINE_COLOR = "white"
PLAYER1_COLOR = "blue"
PLAYER2_COLOR = "red"

# Player Variables
global playerTurn
playerTurn = True



# Board variables, 0 on board means clear, 1 is player1 and 2 is player2
global board
board = []
for i in range(8):
    board.append([0,0,0,0,0,0,0,0])



tk = Tk()
tk.title("Connect 4")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background=BACKGROUND_COLOR)
canvas.bind("<Button-1>", placeMarker)
canvas.pack()

drawGrid()

tk.mainloop()
