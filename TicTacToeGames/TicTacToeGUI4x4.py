from tkinter import *
import tkinter.font as font
from random import *

tk = Tk()
tk.geometry("600x600")
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

player = 'X'
bot = 'O'
# def miniMax(btn, depth, player):
def checkDraw(btns):
    for btn in btns:
        if btn['text'] == ' ':
            return False
    return True
def checkWhoWon(btns, mark):
    # Rows
    print("checkking")
    if (btns[0]['text'] == btns[1]['text'] and btns[0]['text']== btns[2]['text'] and btns[0]['text']== btns[3]['text']and btns[0]['text']== mark):
        return True
    elif (btns[4]['text']== btns[5]['text']and btns[4]['text']== btns[6]['text']and btns[4]['text']== btns[7]['text'] and btns[4]['text']== mark):
        return True
    elif (btns[8]['text']== btns[9]['text']and btns[8]['text']== btns[10]['text'] and btns[8]['text']== btns[11]['text'] and btns[8]['text']== mark):
        return True
    elif (btns[12]['text']== btns[13]['text']and btns[12]['text']== btns[14]['text']and btns[12]['text']== btns[15]['text']and btns[12]['text']== mark):
        return True
        # checkCols
    elif (btns[0]['text']== btns[4]['text']and btns[0]['text']== btns[8]['text']and btns[0]['text']== btns[12]['text']and btns[0]['text']== mark):
        return True
    elif (btns[1]['text']== btns[5]['text']and btns[1]['text']== btns[9]['text']and btns[1]['text']== btns[13]['text']and btns[1]['text']== mark):
        return True
    elif (btns[2]['text']== btns[6]['text']and btns[2]['text']== btns[10]['text']and btns[2]['text']== btns[14]['text']and btns[2]['text']== mark):
        return True
    elif (btns[3]['text']== btns[7]['text']and btns[3]['text']== btns[11]['text']and btns[3]['text']== btns[15]['text']and btns[3]['text']== mark):
        return True
        # Diags
    elif (btns[0]['text']== btns[5]['text']and btns[0]['text']== btns[10]['text']and btns[0]['text']== btns[15]['text']and btns[0]['text']== mark):
        return True
    elif (btns[3]['text']== btns[6]['text']and btns[3]['text']== btns[10]['text']and btns[3]['text']== btns[13]['text']and btns[3]['text']== mark):
        return True
    else:
        print("No winner")
        return

def minimax(btns, depth, isMaximizing):
    if depth <= 0:
        return 0
    if checkWhoWon(btns, bot):
        print("Botwon")
        return 100
    elif checkWhoWon(btns, player):
        print("Human won")
        return -100
    elif checkDraw(btns):
        print("Draw")
        return 0
    if isMaximizing:
        bestScore = -1000
        for btn in btns:
            if btn['text'] == ' ':
                btn['text']= 'O'
                score = minimax(btns, depth-1 , False)
                btn['text'] = ' '
                if score > bestScore:
                    bestScore = score
        return bestScore
    else: # isMinimizing, place markers for the player in worst spots possible
        bestScore = 1000
        for btn in btns:
            if btn['text'] == ' ':
                btn['text']= player
                score = minimax(btns, depth-1, True)
                btn['text']= ' '
                if score < bestScore:
                    bestScore = score
        return bestScore

def botMove(btns):
    global xTurn, numMarkers, gameOver
    bestScore = -1000
    bestMove = 0
    for btn in btns:
        if btn['text'] == ' ':
            if xTurn == True:
                btn['text'] = 'X'
                xTurn = False
                score = minimax(btns,3,False)
                btn['text'] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = btn
                    print("Found bestScore")
            else:
                btn['text'] = 'O'
                xTurn = True
                score = minimax(btns,3,False)
                btn['text'] = ' '
                if score > bestScore:
                    bestScore = score
                    bestMove = btn
                    print("Found bestScore")

    print("Best move is btn ", bestMove)
    bestMove['text'] = bot
    if checkWin(btns):
        gameOver = True
        return

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
    print(btn)
    if xTurn and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text']='X'
        xTurn = False
        numMarkers += 1
        if checkWin(btns):
            gameOver = True
            return
        if AI == True:
            return botMove(btns)
    elif xTurn == False and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text']='O'
        xTurn = True
        numMarkers += 1
        if checkWin(btns):
            gameOver = True
            return
        if AI == True:
            return botMove(btns)





def checkRows(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[1]['text'] and btns[0]['text'] == btns[2]['text'] and btns[0]['text'] == btns[3]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[4]['text'] != ' ' and btns[4]['text'] == btns[5]['text'] and btns[4]['text'] == btns[6]['text'] and btns[4]['text'] == btns[7]['text']:
        if btns[4]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[4]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[8]['text'] != ' ' and btns[8]['text'] == btns[9]['text'] and btns[8]['text'] == btns[10]['text'] and btns[8]['text'] == btns[11]['text']:
        if btns[8]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[8]['text'] == 'O':
            print("O wins!")
            return True
    elif btns[12]['text'] != ' ' and btns[12]['text'] == btns[13]['text'] and btns[12]['text'] == btns[14]['text'] and btns[12]['text'] == btns[15]['text']:
        if btns[12]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[12]['text'] == 'O':
            print("O wins!")
            return True
    return False

def checkCols(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[4]['text'] and btns[0]['text'] == btns[8]['text'] and btns[0]['text'] == btns[12]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[1]['text'] != ' ' and btns[1]['text'] == btns[5]['text'] and btns[1]['text'] == btns[9]['text'] and btns[1]['text'] == btns[13]['text']:
        if btns[1]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[1]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[2]['text'] != ' ' and btns[2]['text'] == btns[6]['text'] and btns[2]['text'] == btns[10]['text'] and btns[2]['text'] == btns[14]['text']:
        if btns[2]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[2]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[7]['text'] and btns[3]['text'] == btns[11]['text'] and btns[3]['text'] == btns[15]['text']:
        if btns[3]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[3]['text'] == 'O':
            print("O wins!")
            return True
    return False

def checkDiags(btns):
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[5]['text'] and btns[0]['text'] == btns[10]['text'] and btns[0]['text'] == btns[15]['text']:
        if btns[0]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[0]['text'] == 'O':
            print("O wins!")
            return True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[6]['text'] and btns[3]['text'] == btns[9]['text'] and btns[3]['text'] == btns[12]['text']:
        if btns[3]['text'] == 'X':
            print("X wins!")
            return True
        elif btns[3]['text'] == 'O':
            print("O wins!")
            return True


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
btn10 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(10,btns))
btn11 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(11,btns))
btn12 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(12,btns))
btn13 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(13,btns))
btn14 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(14,btns))
btn15 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(15,btns))
btn16 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(16,btns))


# Add each button to it's respective location
btn1.grid(row=0, column = 0)
btn2.grid(row=0, column = 1)
btn3.grid(row=0, column = 2)
btn4.grid(row=0, column = 3)
btn5.grid(row=1, column = 0)
btn6.grid(row=1, column = 1)
btn7.grid(row=1, column = 2)
btn8.grid(row=1, column = 3)
btn9.grid(row=2, column = 0)
btn10.grid(row=2, column = 1)
btn11.grid(row=2, column = 2)
btn12.grid(row=2, column = 3)
btn13.grid(row=3, column = 0)
btn14.grid(row=3, column = 1)
btn15.grid(row=3, column = 2)
btn16.grid(row=3, column = 3)

btns.append(btn1)
btns.append(btn2)
btns.append(btn3)
btns.append(btn4)
btns.append(btn5)
btns.append(btn6)
btns.append(btn7)
btns.append(btn8)
btns.append(btn9)
btns.append(btn10)
btns.append(btn11)
btns.append(btn12)
btns.append(btn13)
btns.append(btn14)
btns.append(btn15)
btns.append(btn16)

for btn in btns:
    btn['font']=myFont

while not gameOver and numMarkers < 16:
    tk.update()
if not gameOver and numMarkers == 16:
    print("Tie game!")
