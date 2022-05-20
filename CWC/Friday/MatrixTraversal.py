from random import randint

k1=0
k2=0

flag=True


# Populate board with random digits
board = []
for i in range(8):
    board.append([])
    for j in range(8):
        board[i].append(randint(0,9))
        print(board[i][j], end=" ")
    print("\n")

def displayBoard(board):
    print("---------------")
    for row in board:
        for col in row:
            print(f"{col}", end=" ")
        print("\n")
    print("---------------")


def traverseBoard(i,j, board):

    global k1
    global k2
    global flag

    if i >= 8 or j >= 8:
        if flag:
            a = k1
            k1 = k2
            k2 = a

            if flag:
                flag = False
            else:
                flag = True
            k1 += 1
        else:
            a = k1
            k1 = k2
            k2 = a
            if flag:
                flag = False
            else:
                flag = True
        print()
        return False

    print(board[i][j], end=" ")

    if (traverseBoard(i+1,j+1,board)):
        return True

    if (traverseBoard(k1, k2, board)):
        return True
    return True






traverseBoard(0,0,board)

# displayBoard(board)
