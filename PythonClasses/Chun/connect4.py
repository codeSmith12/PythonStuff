board = [
    ["_", "_", "_", "_", "_", "_", "_"], # 0 
    ["_", "_", "_", "_", "_", "_", "_"], # 1 
    ["_", "_", "_", "_", "_", "_", "_"], # 2
    ["_", "_", "_", "_", "_", "_", "_"], # 3
    ["_", "_", "_", "_", "_", "_", "_"], # 4
    ["_", "_", "_", "_", "_", "_", "_"], # 5
        ]
"""

ask player what column they want (Done)
see if column is valid 
put item in correct column and row

"""
print("1 2 3 4 5 6 7")

redPlayerTurn = True

def showboard(board):
    print("\n")
    for i in range(6):
        for j in range(7):
            print (board [i][j], end = " ")
        print()
    print("\n")
    
def checkWin(board):
    # 1. Check Vertical
    for i in range(5,-1,-1):
        pass
    # 2. Check Horizontal
    # 3. Diagonal Right
    # 4. Diagonal Left
    return False


def placeitem(board, player): # player == "R"
    while(True):
        Col_choice = int(input("Enter your column number: "))-1
        if Col_choice > 6 or Col_choice < 0:
            print ("Invalid number")
        else:
            break
    print("Add to board")
    for i in range(5,-1, -1):
        if board[i][Col_choice] == "_":
            board[i][Col_choice] = player
            break

while not checkWin(board):
    showboard(board)
    if redPlayerTurn: # If redPlayerTurn == True:
        placeitem(board, "R")
        redPlayerTurn = not redPlayerTurn
    else:
        placeitem(board, "Y")
        redPlayerTurn = not redPlayerTurn
        


















