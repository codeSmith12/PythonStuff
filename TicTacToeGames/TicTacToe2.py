board = {
  1: ' ', 2: ' ', 3: ' ',
  4: ' ', 5: ' ', 6: ' ',
  7: ' ', 8: ' ', 9: ' '
}

def displayBoard(board):
  print('---------')
  print(board[1], '|', board[2], '|',board[3] )
  print('---------')
  print(board[4], '|', board[5], '|',board[6])
  print('---------')
  print(board[7], '|', board[8], '|',board[9])
  print('---------')


def spaceIsFree(position):
    if board[position] == ' ':
        return True
    else:
        return False

def placeMarker(letter, position):
    if spaceIsFree(position):
        board[position] = letter
        displayBoard(board)
        if checkDraw():
            print("Draw")
            exit()
        if checkWin():
            if letter == 'X':
                print("Bot wins!")
                exit()
            else:
                print("Player wins!")
                exit()
    else:
        print("Can't place marker there.")
        position = int(input("Enter new position: "))
        placeMarker(letter, position)
        return


def checkDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False
    return True

def checkWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def checkWhoWon(mark):
    if (board[1] == board[2] and board[1] == board[3] and board[1] == mark):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] == mark):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] == mark):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] == mark):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] == mark):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] == mark):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] == mark):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] == mark):
        return True
    else:
        return False

player = 'O'
bot = 'X'
def playerMove():
    position = int(input("Enter the position for your marker. "))
    placeMarker(player, position)
    return
def botMove():
    bestScore = -1000
    bestMove = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = bot
            score = minimax(board,0,False)
            board[key] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = key
    placeMarker(bot, bestMove)
    return

def minimax(board, depth, isMaximizing):
    if checkWhoWon(bot):
        return 100
    elif checkWhoWon(player):
        return -100
    elif checkDraw():
        return 0
    if isMaximizing:
        bestScore = -1000
        for key in board.keys():
            if board[key] == ' ':
                board[key]= bot
                score = minimax(board, 0 , False)
                board[key] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else: # isMinimizing, place markers for the player in worst spots possible
        bestScore = 1000
        for key in board.keys():
            if board[key] == ' ':
                board[key]= player
                score = minimax(board, 0 , True)
                board[key] = ' '
                if score < bestScore:
                    bestScore = score
        return bestScore


while not checkWin():
    playerMove()
    botMove()
