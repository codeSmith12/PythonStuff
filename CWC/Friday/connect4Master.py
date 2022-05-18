from tkinter import *

"""
TODO:

Need to stop player from interacting with the board
once a winner has been detected.

^^^ Can deal with out of bounds by using try and except IndexError

Replay menu

"""

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
    global board, playerTurn, gameOver
    # Dont place marker if game is over
    if gameOver:
        return
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
    displayBoard(board)
    checkWinner(board)

# ROW IS NOT WORKING 100%
def checkRows(board):
    for row in board:
        P1Score = 0
        P2Score = 0
        for col in row:
            if P1Score == 4:
                print("Player 1 has won! Row")
                return True
            elif P2Score == 4:
                print("Player 2 has won! Row")
                return True

            if col == 1:
                P2Score = 0
                P1Score += 1
            elif col == 2:
                P1Score = 0
                P2Score += 1
            elif col == 0:
                P1Score = 0
                P2Score = 0


def checkCols(board):
    # displayBoard(board)
    for col in range(8):
        P1Score = 0
        P2Score = 0
        for row in range(8):
            if P1Score == 3:
                print("Player 1 has won! Col")
                return True
            elif P2Score == 3:
                print("Player 2 has won via! Col")
                return True

            if board[row][col] == 1:
                P2Score = 0
                P1Score += 1
            elif board[row][col] == 2:
                P1Score = 0
                P2Score += 1
            elif board[row][col] == 0:
                P1Score = 0
                P2Score = 0

# JESUSSSSSSSSSS
def checkDiags(marker, board):
    print("GITTEST")
    for i in range(0,4):
        for j in range(0,3):
            if (board[j][i]==board[j+1][i+1]==\
                board[j+2][i+2]==board[j+3][i+3]==marker or
                board[j+3][i]==board[j+2][i+1]==\
                board[j+1][i+2]==board[j][i+3]==marker):
                    gameOver = True
            else:
                continue
    # for x in range(0,4):
    #     for y in range(0,3):
    #         if board[x][y] == board[x+1][y+1] ==\
    #          board[x+2][y+2] == board[x+3][y+3] == marker or\
    #          board[y+3][x] == board[y+2][x+1] ==\
    #          board[y+1][x+2] == marker:
    #             print(f"Player {marker} wins diagonally")


def checkWinner(board):
    global gameOver

    gameOver = checkRows(board)
    gameOver = checkCols(board)
    gameOver = checkDiags(1, board)
    # Make sure to end the function so gameOver doesnt get overridden
    if gameOver:
        return
    gameOver = checkDiags(2, board)
    if gameOver:
        return


# Print the grid / board for testing purposes
def displayBoard(board):
    print("---------------")
    for row in board:
        for col in row:
            print(f"{col}", end=" ")
        print("\n")
    print("---------------")

# Game Constants
WIDTH = 800
HEIGHT = 800
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

global gameOver
gameOver=False

# Board is a matrix of integers representing if the slot is taken or not.
# 0 on board means clear, 1 is player1 and 2 is player2
global board
board = []
for i in range(8):
    board.append([0,0,0,0,0,0,0,0])

# GUI Stuff
tk = Tk()
tk.title("Connect 4")
tk.geometry(f"{WIDTH}x{HEIGHT}")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, background=BACKGROUND_COLOR)

# Assign placeMarker function to the left keypress
canvas.bind("<Button-1>", placeMarker)
canvas.pack()

drawGrid()

tk.mainloop()
