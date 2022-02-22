from tkinter import *
import tkinter.font as font

tk = Tk()
tk.geometry("380x375")
tk.title("Tic Tac Toe")

myFont = font.Font(size=30)

global xTurn # Deleted at the end of the entire program
xTurn = True
global gameOver
gameOver = False

def playerMove(btn, btns):
    global xTurn
    if xTurn == True and btns[btn - 1]['text'] == ' ':
        btns[btn-1]['text'] = 'X'
        xTurn = False
    elif xTurn == False and btns[btn - 1]['text'] == ' ':
        btns[btn-1]['text'] = 'O'
        xTurn = True
    checkWin(btns)





# list (btns) == 0-8
# 0, 1, 2
# 3, 4, 5,
# 6, 7, 8
def checkRows(btns):
    global gameOver
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[1]['text'] and btns[0]['text'] == btns[2]['text']:
        if btns[0]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[4]['text'] and btns[3]['text'] == btns[5]['text']:
        if btns[3]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True

    elif btns[6]['text'] != ' ' and btns[6]['text'] == btns[7]['text'] and btns[6]['text'] == btns[8]['text']:
        if btns[6]['text'] == 'X':
            gameOver = True
            print("X Wins!")
        else:
            gameOver = True
            print("O Wins!")

def checkCols(btns):
    global gameOver
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[3]['text'] and btns[0]['text'] == btns[6]['text']:
        if btns[0]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True

    elif btns[1]['text'] != ' ' and btns[1]['text'] == btns[4]['text'] and btns[1]['text'] == btns[7]['text']:
        if btns[1]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True

    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[5]['text'] and btns[2]['text'] == btns[8]['text']:
        if btns[2]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True


def checkDiags(btns):
    global gameOver
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[4]['text'] and btns[0]['text'] == btns[8]['text']:
        if btns[0]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True

    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[4]['text'] and btns[2]['text'] == btns[6]['text']:
        if btns[2]['text'] == 'X':
            print("X Wins!")
            gameOver = True
        else:
            print("O Wins!")
            gameOver = True


def checkWin(btns):
    checkRows(btns)
    checkCols(btns)
    checkDiags(btns)






btn1 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(1,btns))
btn2 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(2,btns))
btn3 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(3,btns))
btn4 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(4,btns))
btn5 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(5,btns))
btn6 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(6,btns))
btn7 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(7,btns))
btn8 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(8,btns))
btn9 = Button(tk, text=' ', width=5, height=2, command=lambda:playerMove(9,btns))

global btns
btns = []
btns.append(btn1)
btns.append(btn2)
btns.append(btn3)
btns.append(btn4)
btns.append(btn5)
btns.append(btn6)
btns.append(btn7)
btns.append(btn8)
btns.append(btn9)

for btn in btns:
    btn['font'] = myFont

# 0,0 0,1 0,2
# 1,0

# ^^^^^ Look here for example...

btn1.grid(row=0, column = 0)
btn2.grid(row=0, column = 1)
btn3.grid(row=0, column = 2)
btn4.grid(row=1, column = 0)
btn5.grid(row=1, column = 1)
btn6.grid(row=1, column = 2)
btn7.grid(row=2, column = 0)
btn8.grid(row=2, column = 1)
btn9.grid(row=2, column = 2)

def clearBoard():
    global btns
    print("clearing buttons")
    for btn in btns:
        btn['text'] = ' '

def playGame():
    # Run the main game
    global gameOver, xTurn
    while not gameOver:
        tk.update()

    # After game is over, ask if they want to play again
    playAgain = input("Would you like to play again? (y/n)")
    if playAgain == 'y': # If y, reset variables and board
        gameOver = False
        xTurn = True
        clearBoard()
        playGame() # Begin next game
    else:
        return
playGame()
