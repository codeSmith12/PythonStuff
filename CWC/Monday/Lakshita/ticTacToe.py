from tkinter import *
import tkinter.font as font
window = Tk()

# GUI = Graphic User Interface

window.geometry("380x500")
window.title("Tic Tac Toe")

myFont = font.Font(size=30)

global xTurn
xTurn = True # Game begins with Xs turn
global hasWon
hasWon = False


def playerMove(btn, btns): # Takes the number of the button pressed,
    global xTurn, hasWon    # and the list of btns

    if hasWon == False:
        if btns[btn-1]['text'] == " ":
            if xTurn == True:
                btns[btn-1]['text'] = 'X'
                xTurn = False
            else:
                btns[btn-1]['text'] = 'O'
                xTurn = True
            checkWin(btns)

# 0 1 2
# 3 4 5
# 6 7 8

def checkRows(btns): # If the first button is taken, and the first button is == to the second and 3rd Button
    global xWins, oWins, hasWon
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[1]['text'] and btns[0]['text'] == btns[2]['text']:
        hasWon = True
        if btns[0]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[4]['text'] and btns[3]['text'] == btns[5]['text']:
        hasWon = True
        if btns[3]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"
    elif btns[6]['text'] != ' ' and btns[6]['text'] == btns[7]['text'] and btns[6]['text'] == btns[8]['text']:
        hasWon = True
        if btns[6]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"



# 0 1 2
# 3 4 5
# 6 7 8
def checkCols(btns):
    global xWins, oWins, hasWon
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[3]['text'] and btns[0]['text'] == btns[6]['text']:
        hasWon = True
        if btns[0]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"
    elif btns[1]['text'] != ' ' and btns[1]['text'] == btns[4]['text'] and btns[1]['text'] == btns[7]['text']:
        hasWon = True
        if btns[1]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"
    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[5]['text'] and btns[2]['text'] == btns[8]['text']:
        hasWon = True
        if btns[2]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"

# 0 1 2
# 3 4 5
# 6 7 8
def checkDiags(btns):
    global xWins, oWins, hasWon
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[4]['text'] and btns[0]['text'] == btns[8]['text']:
        hasWon = True
        if btns[0]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"
    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[4]['text'] and btns[2]['text'] == btns[6]['text']:
        hasWon = True
        if btns[2]['text'] == 'X':
            print("X Wins!")
            xWins += 1
            xWinsLabel['text'] = f"X Wins: {xWins}"
        else:
            print("O Wins!")
            oWins += 1
            oWinsLabel['text'] = f"O Wins: {oWins}"

def clearBoard(btns):
    global hasWon, xTurn
    hasWon = False
    xTurn = True
    for btn in btns:
        btn['text'] = " " # data type? String

def checkWin(btns):
    checkRows(btns)
    checkCols(btns)
    checkDiags(btns)




btn1 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(1, btns))
btn2 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(2, btns))
btn3 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(3, btns))
btn4 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(4, btns))
btn5 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(5, btns))
btn6 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(6, btns))
btn7 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(7, btns))
btn8 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(8, btns))
btn9 = Button(window, text=' ', width=5, height=2, font=myFont, command=lambda: playerMove(9, btns))



global btns # global means this variable
            # can be accessed ANYWHERE in the program.
btns = []

btns.append(btn1) # 0
btns.append(btn2) # 1
btns.append(btn3) # 2
btns.append(btn4) # 3
btns.append(btn5)
btns.append(btn6)
btns.append(btn7)
btns.append(btn8)
btns.append(btn9)

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

"""

"""



myFont = font.Font(size=20, family="Comic Sans MS")


resetButton = Button(window, text='Reset', width=5, height=1, font=myFont, command=lambda: clearBoard(btns), bg="red", activebackground="red")
resetButton.grid(row=3, column=0,sticky=W)

global xWins, oWins
xWins = 0 # Keep track of how many wins each player has.
oWins = 0

# Set the font for the labels <----
myFont = font.Font(size=15, family="Comic Sans MS")

# Add the X wins label to the grid
xWinsLabel = Label(window,text=f"X Wins: {xWins}", font = myFont, fg="blue")
xWinsLabel.grid(row=3, column=1,sticky=W)

# Add the O wins label to the grid
oWinsLabel = Label(window,text=f"O Wins: {oWins}", font = myFont, fg="red")
oWinsLabel.grid(row=3, column=2,sticky=W)

window.mainloop()
