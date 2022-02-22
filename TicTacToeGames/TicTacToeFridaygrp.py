from tkinter import *
import tkinter.font as font

tk = Tk()
tk.geometry("400x400")
tk.title("Tic Tac Toe")
myFont = font.Font(size=30)

global xTurn
xTurn = True

global numMarkers
numMarkers = 0

global gameOver
gameOver = False

def playerMove(btn):
    global xTurn
    if xTurn and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text'] = 'X'
        xTurn = False

    elif not xTurn and btns[btn-1]['text'] == ' ':
        btns[btn-1]['text'] = 'O'
        xTurn = True
    checkWin(btns)

        # 0, 1, 2,
        # 3, 4, 5,
        # 6, 7, 8
def checkRows(btns):
    global gameOver
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[1]['text'] and btns[0]['text'] == btns[2]['text']:
        if btns[0]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[4]['text'] and btns[3]['text'] == btns[5]['text']:
        if btns[3]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

    elif btns[6]['text'] != ' ' and btns[6]['text'] == btns[7]['text'] and btns[6]['text'] == btns[8]['text']:
        if btns[6]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

        # 0, 1, 2,
        # 3, 4, 5,
        # 6, 7, 8
def checkCols(btns):
    global gameOver
    if btns[0]['text'] != ' ' and btns[0]['text'] == btns[3]['text'] and btns[0]['text'] == btns[6]['text']:
        if btns[0]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

    elif btns[3]['text'] != ' ' and btns[3]['text'] == btns[4]['text'] and btns[3]['text'] == btns[5]['text']:
        if btns[3]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

    elif btns[6]['text'] != ' ' and btns[6]['text'] == btns[7]['text'] and btns[6]['text'] == btns[8]['text']:
        if btns[6]['text'] == 'X':
            print("X Wins!")
        else:
            print("O Wins!")
        gameOver = True

def checkDiags(btns):
    pass

def checkWin(btns):
    checkRows(btns)
    checkCols(btns)
    checkDiags(btns)


btn1 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(1))
btn2 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(2))
btn3 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(3))
btn4 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(4))
btn5 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(5))
btn6 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(6))
btn7 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(7))
btn8 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(8))
btn9 = Button(tk, text=' ', width=5, height=2, command=lambda: playerMove(9))

# row 1
btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
# row 2

btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)

# row 3
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)

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
    btn['font']=myFont



while not gameOver and numMarkers < 9:
    tk.update()
