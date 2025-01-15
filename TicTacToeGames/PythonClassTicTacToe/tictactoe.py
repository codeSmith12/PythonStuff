
def displayBoard():
    for row in range(3):
        for col in range(3):
            print(board[row][col], end=" ")
        print("")

def placeMarker():
    if xTurn:
        

board = [["-", "-", "-"],["-", "-", "-"],["-", "-", "-"]]

displayBoard()

xTurn = True
xWins = 0
oWins = 0
numMarkers = 0

# Create board
# Display board
# Place marker on board
# Check if a player has won
# If so, print results