from tkinter import *
import tkinter.font as font
from random import *
from math import inf as infinity
tk = Tk()
tk.geometry("380x375")
tk.title("Tic Tac Toe")
myFont = font.Font(size=30)


# If we dont use xTurn as a global the placemarker function has trouble changing it's value
global xTurn
xTurn = True

global numMarkers
numMarkers = 0

global btns
btns = []

global AI
AI = True

global gameOver
gameOver = False

global MAX
MAX = 1
global MIN
MIN = -1




def compMove(btns):
    global xTurn, numMarkers, gameOver
    for btn in btns:
        if btn['text'] == ' ':
            if xTurn == True:
                btn['text'] = 'X'
                xTurn = False
                numMarkers += 1
                break
            else:
                btn['text'] = 'O'
                xTurn = True
                numMarkers += 1
                break
    if checkWin(btns):
        gameOver = True
        return

def playerMove(btn, btns):
    global xTurn, AI, gameOver, numMarkers
    if xTurn and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text']='X'
        xTurn = False
        numMarkers += 1
    elif xTurn == False and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text']='O'
        xTurn = True
        numMarkers += 1
    if checkWin(btns):
        gameOver = True
        return


    if AI == True:
        return compMove(btns)

def checkRows(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[1]['text'] and btns[0]['text'] == btns[2]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[4]['text'] and btns[3]['text'] == btns[5]['text']:
        if btns[3]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[3]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[6]['text'] != ' ' and btns[6]['text'] == btns[7]['text'] and btns[6]['text'] == btns[8]['text']:
        if btns[6]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[6]['text'] == 'O':
            print("O wins!")
            return True
    return False

def checkCols(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[3]['text'] and btns[0]['text'] == btns[6]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[1]['text'] != ' ' and btns[1]['text'] == btns[4]['text'] and btns[1]['text'] == btns[7]['text']:
        if btns[1]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[1]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[5]['text'] and btns[2]['text'] == btns[8]['text']:
        if btns[2]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[2]['text'] == 'O':
            print("O wins!")
            return True
    return False

def checkDiags(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[4]['text'] and btns[0]['text'] == btns[8]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[4]['text'] and btns[2]['text'] == btns[6]['text']:
        if btns[2]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[2]['text'] == 'O':
            print("O wins!")
            return True
    return False

def checkWin(btns):
    if checkRows(btns):
        print("Game over")
        return True
    elif checkCols(btns):
        print("Game over")
        return True
    elif checkDiags(btns):
        print("Game over")
        return True
    return False

# Create all of the buttons with blank text, size them
# Make sure to call function placeMarker when clicked and pass in btn# and btn array
btn1 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(1,btns))
btn2 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(2,btns))
btn3 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(3,btns))
btn4 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(4,btns))
btn5 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(5,btns))
btn6 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(6,btns))
btn7 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(7,btns))
btn8 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(8,btns))
btn9 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(9,btns))

btn1.grid(row=0, column = 0)
btn2.grid(row=0, column = 1)
btn3.grid(row=0, column = 2)
btn4.grid(row=1, column = 0)
btn5.grid(row=1, column = 1)
btn6.grid(row=1, column = 2)
btn7.grid(row=2, column = 0)
btn8.grid(row=2, column = 1)
btn9.grid(row=2, column = 2)

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
    btn['font']=myFont

while not gameOver and numMarkers < 9:
    tk.update()
if not gameOver and numMarkers == 9:
    print("Tie game!")
