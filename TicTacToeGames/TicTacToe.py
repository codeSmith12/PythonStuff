import math
board = [
    ['-', '-', '-'],
    ['-', '-', '-'],
    ['-', '-', '-']
]

def displayBoard(board):
    print(board[0][0], '|', board[0][1], '|', board[0][2])
    print(board[1][0], '|', board[1][0], '|', board[1][0])
    print(board[2][0], '|', board[2][0], '|', board[2][0])
# Make changes here... Then Ctrl + s to save,
def checkRows(board):
    print("Checking rows...")
    if board[0][0] != '-' and board[0][0] == board[0][1] and board[0][0] == board[0][2]:
        if board[0][0] == 'X':
            print("X Wins!")
            xWins = True
        else:
            print("O Wins!")
            oWins = True
    elif board[1][0] != '-' and board[1][0] == board[1][1] and board[1][0] == board[1][2]:
        if board[1][0] == 'X':
            print("X Wins!")
            xWins = True
        else:
            print("O Wins!")
            oWins = True
    elif board[2][0] != '-' and board[2][0] == board[2][1] and board[2][0] == board[2][2]:
        if board[2][0] == 'X':
            print("X Wins!")
            xWins = True
        else:
            print("O Wins!")
            oWins = True

def checkWin(board):
    checkRows(board)
# Check Cols
# Check Diagonal

# 0 | 0 1 2
# 1 | 0 1 2
# 2 | 0 1 2
# 7 / 3 = 2
# 7 % 3 = 0

displayBoard(board)

xWins = False
oWins = False
numMarkers = 0
xTurn = True

while xWins != True and oWins != True and numMarkers != 9:
    marker = int(input("Place a marker by entering a number (1-9) "))
    y = math.floor(marker / 3)
    x = (marker % 3) - 1
    print (y)
    if xTurn and board[y][x] == '-': # if it's x's turn
        board[y][x] = 'X'
        xTurn = False
    elif xTurn == False and board[y][x] == '-':
        board[y][x] = 'O'
        xTurn = True
    checkWin(board)
    displayBoard(board)
