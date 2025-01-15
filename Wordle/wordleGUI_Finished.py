from tkinter import *
from random import choice
from functools import partial

with open("Wordle/answers.txt", "r") as answersFile:
    answers = [line.rstrip() for line in answersFile]

with open("Wordle/allowedWords.txt", "r") as wordFile:
    words = [line.rstrip() for line in wordFile]

global turn
turn = 0
global curLetter
curLetter=0
global answer

answer = choice(answers)
# print(answer)
def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    r, g, b = rgb
    return f'#{r:02x}{g:02x}{b:02x}'

def limitEntry(*args):
    value = entryStr.get()
    if len(value) > 5:
        entryStr.set(value[:5])

def checkAnswer(guess, matrix):
    global turn, answer, kb
    for i in range(5):
        if guess[i] == answer[i]:
            matrix[turn][i].configure(bg=_from_rgb(green))
        elif guess[i] in answer:
            matrix[turn][i].configure(bg=_from_rgb(yellow))
        elif guess[i] not in answer:
            for row in kb:
                for btn in row:
                    if guess[i] == btn['text'].lower():
                        btn.configure(fg=_from_rgb(disabledGrey))

    if guess == answer:
        turn = 6
        print("You win!")
        winLabel = Label(window, text="You win!", bg=_from_rgb(black), fg="white", font=winFont).grid(column=3, row=14)

def clearRow(matrix):
    global turn, curLetter
    curLetter = 0
    for i in range(5):
        matrix[turn][i]['text'] = ' '

def submitAnswer(matrix):
    global turn, curLetter
    guess = []
    if turn < 6:
        for i in range(5):
            if matrix[turn][i]['text'] != " ":
                guess.append(matrix[turn][i]['text'].lower())
        guess = "".join(guess)
        print(guess)
        if guess not in words and guess not in answers:
            print(f"{guess} not found in word list.")
            clearRow(matrix)
            return
        else:
            if len(guess) != 5:
                print("Please enter a word that's 5 letters long.")
                clearRow(matrix)
            else:
                checkAnswer(guess, matrix)
                turn += 1
                curLetter = 0
                print(turn)
    else:
        print("You are out of turns :(")
def removeLetter(matrix):
    global turn, curLetter
    if curLetter > 0:
        matrix[turn][curLetter-1]['text'] = ' '
        curLetter -= 1

def enterValue(key, matrix,event=None):
    global turn, curLetter, kb
    # for row in kb:
    #     for btn in row:
    #         if key == btn['text'].lower() and btn["state"] == "disabled":
    #             return
    if curLetter < 5 and turn < 6:
        matrix[turn][curLetter]['text'] = key.upper()
        curLetter += 1

myFont = ("Helvetica", 20, "bold")
kbFont = ("Helvetica", 8, "bold")

winFont = ("Helvetica", 12, "bold")
submitFnt = ("Helvetica", 12)
darkGrey = (59,56,56)
disabledGrey = (70,70,70)
black = (17,17,17)
green = (39,133,32)
yellow = (158,142,22)

window = Tk()
window.title("Wordle")
window.configure(bg=_from_rgb(black))

width = 600
height = 800
window.geometry(f"{width}x{height}")

# Configure margins
window.columnconfigure(0,weight=1)
window.columnconfigure(9,weight=1)
# Necessary to limit the string length
entryStr = StringVar()
entryStr.trace('w', limitEntry)

# Create the grid of buttons
matrix = []
for i in range(0,6):
    temp = []
    for j in range(0,5):
        temp.append(Button(window, text=" ", font = myFont, width=4,height=2, bg=_from_rgb(darkGrey), borderwidth=.5,fg="white", state="disabled", disabledforeground="white"))
        temp[j].grid(row=i, column=j+1, columnspan=1) # +1 for the left margin
        # window.columnconfigure(j,weight=2,uniform="grid")
    matrix.append(temp)

# Allows enter key to call submit function, nice!
window.bind("<Return>", (lambda event: submitAnswer(matrix) ))
window.bind("<BackSpace>", (lambda event: removeLetter(matrix) ))


letterList = [['q','w','e','r','t','y','u','i','o','p'],
              ['a','s','d','f','g','h','j','k','l'],
              ['enter','z','x','c','v','b','n','m','del']]
for row in letterList:
    for letter in row:
        # Closure needed again to avoid the same problem, each bind being set to del instead of respective letter
        closure = partial(enterValue, letter, matrix)
        if letter != 'enter' and letter != 'del':
            window.bind(letter, closure)
global kb
kb = []

for i in range(3):
    temp = []
    for j in range(len(letterList[i])):
        # Added closure with partial to save the current letter we are on in a temporary function for button command
        # This avoids the trouble of having every button set to the last letter in the list(del)
        closure = partial(enterValue,letterList[i][j], matrix)
        temp.append(Button(window, font=kbFont, text=letterList[i][j].upper(), width=4,height=2, bg=_from_rgb(darkGrey),fg="white",command=closure))
        # window.columnconfigure(j,weight=1, uniform="kb")
        temp[j].grid(column=j,row=10+i, sticky="NSEW", padx=2,pady=2, columnspan=1)
        if letterList[i][j] == "enter":
            temp[j].configure(command=lambda:submitAnswer(matrix))
        elif letterList[i][j] == "del":
            temp[j].configure(command=lambda:removeLetter(matrix))
    kb.append(temp)

window.mainloop()
