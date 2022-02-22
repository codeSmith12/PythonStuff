board = {
  1: ' ', 2: ' ', 3: ' ',
  4: ' ', 5: ' ', 6: ' ',
  7: ' ', 8: ' ', 9: ' '
}


def displayBoard(board):
    print(board[1], '|', board[2], '|', board[3])
    print("---------")
    print(board[4], '|', board[5],  '|',board[6])
    print("---------")
    print(board[7],  '|', board[8], '|', board[9])

global xTurn
xTurn = True

global numMarkers
numMarkers = 0

global gameOver
gameOver = False


def checkRows(board):
    if board[1] != ' ' and board[1] == board[2] and board[1] == board[3]:
        if board[1] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")
    elif board[1] != ' ' and board[1] == board[2] and board[1] == board[3]:
        if board[1] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")
    elif board[1] != ' ' and board[1] == board[2] and board[1] == board[3]:
        if board[1] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")

def checkCols(board):
    if board[1] != ' ' and board[1] == board[4] and board[1] == board[7]:
        if board[1] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")
    elif board[2] != ' ' and board[2] == board[5] and board[2] == board[8]:
        if board[2] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")
    elif board[3] != ' ' and board[3] == board[6] and board[3] == board[9]:
        if board[3] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")

def checkDiags(board):
    if board[1] != ' ' and board[1] == board[5] and board[1] == board[9]:
        if board[1] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")
    elif board[3] != ' ' and board[3] == board[5] and board[3] == board[7]:
        if board[3] == 'X':
            print("X wins!")
        else: # if board[1] == 'O'
            print("O wins!")

def checkWin(board):
    checkRows(board)
    checkCols(board)
    checkDiags(board)






def placeMarker(board):
    global xTurn, numMarkers
    pos = int( input("Please enter a number 1-9 to place a marker: ") )
    if board[pos] == ' ':
        if xTurn == True:
            board[pos] = 'X'
            xTurn = False
        else:
            board[pos] = 'O'
            xTurn = True
        numMarkers += 1
        checkWin(board)

while gameOver == False:
    placeMarker(board)
    displayBoard(board)
