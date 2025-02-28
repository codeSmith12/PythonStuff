
# board = [                                # i:
#     ["_", "_", "_", "_", "_", "_", "_"], # 0 
#     ["_", "_", "_", "_", "_", "_", "_"], # 1 
#     ["_", "_", "_", "_", "_", "_", "_"], # 2
#     ["_", "_", "_", "_", "_", "_", "_"], # 3
#     ["_", "_", "_", "_", "_", "_", "_"], # 4
#     ["_", "_", "_", "_", "_", "_", "_"], # 5
#     ]
# # j:  0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 

# redPlayerTurn = True

# def showboard(board):
#     print("\n")
#     for i in range(6):
#         for j in range(7):
#             print (board [i][j], end = " ")
#         print()
#     print("\n")
    
# def checkWin(board):
#     # 1. Check Vertical
#     for i in range(5,-1,-1):
#         pass
#     # 2. Check Horizontal
#     # 3. Diagonal Right
#     # 4. Diagonal Left
#     return False


# def placeitem(board, player): # player == "R"
#     while(True):
#         Col_choice = int(input("Enter your column number: "))-1
#         if Col_choice > 6 or Col_choice < 0:
#             print ("Invalid number")
#         else:
#             break
#     print("Add to board")
#     for i in range(5,-1, -1):
#         if board[i][Col_choice] == "_":
#             board[i][Col_choice] = player
#             break

# while not checkWin(board):
#     showboard(board)
#     if redPlayerTurn: # If redPlayerTurn == True:
#         placeitem(board, "R")
#         redPlayerTurn = not redPlayerTurn
#     else:
#         placeitem(board, "Y")
#         redPlayerTurn = not redPlayerTurn
        


















board = [                               # i
    ["_", "_", "_", "_", "_", "_", "_"],# 0
    ["_", "_", "_", "_", "_", "_", "_"],# 1
    ["_", "_", "_", "_", "_", "_", "_"],# 2
    ["_", "_", "_", "_", "_", "_", "_"],# 3 
    ["_", "_", "_", "_", "_", "_", "_"],# 4
    ["_", "_", "_", "_", "_", "_", "_"],# 5
    ]
# j:  0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 

redplayerturn = True

def showboard(board):
    print("\n")
    for i in range(6):
        for j in range(7):
            print (board [i][j], end = " ")
        print()
    print("\n")

def checkHorizontal(board):
    for i in range(5,-1,-1):
        for j in range(0,4,1):
            if board[i][j] == "R" and board[i][j+1] =="R" and board[i][j+2] =="R" and board[i][j+3] =="R":
                showboard(board)
                print("red Wins!!! Congrats")
                return True
            if board[i][j] == "Y" and board[i][j+1] =="Y" and board[i][j+2] =="Y" and board[i][j+3] =="Y":
                showboard(board)
                print("Yellow Wins!!! Congrats")
                return True

def checkvertical(board):
    for j in range(7):
        for i in range(3):
            if board [i][j] == "R" and board[i+1][j] == "R" and board [i+2][j] == "R" and board[i+3][j] == "R":
                showboard(board)
                print("red Wins!!! Congrats")
                return True
            if board [i][j] == "Y" and board[i+1][j] == "Y" and board [i+2][j] == "Y" and board[i+3][j] == "Y":
                showboard(board)
                print("Yellow Wins!!! Congrats")
                return True

def checkDiag(board):
    rcount = 0
    ycount= 0
    for i in range(6):
        rcount = 0
        ycount = 0
        for j in range (5, -1, -1):
            if board[i][j] == "R":
                rcount += 1
                ycount =0
            elif board[i][j] == "Y":
                rcount = 0
                ycount += 1
            if rcount == 4:
                print("red Wins!!! Congrats")
                return True
            elif ycount == 4:
                print("Yellow Wins!!! Congrats")
                return True
            
    
    
    
def checkwin(board):
    return checkDiag(board)
    return checkvertical(board)
    return checkHorizontal(board)
    
            
    return False


def placeitem(board, player):
    while(True):
        Col_choice = int(input("Enter your column number: "))-1
        if Col_choice > 6 or Col_choice < 0:
            print ("Invalid number")
        else:
            break
    print("Add to board")
    for i in range(5,-1,-1):
        if board [i][Col_choice]=="_":
            board[i][Col_choice] = player
            break
            


while not checkwin(board):
    showboard(board)
    if redplayerturn:
        placeitem(board, "R")
        redplayerturn = not redplayerturn
    else:
        placeitem(board, "Y")
        redplayerturn = not redplayerturn