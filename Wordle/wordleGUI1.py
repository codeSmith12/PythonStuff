from tkinter import *
from random import choice

with open("answers.txt", "r") as answersFile:
    answers = [line.rstrip() for line in answersFile]

with open("allowedWords.txt", "r") as wordFile:
    words = [line.rstrip() for line in wordFile]

global turn
turn = 0
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
    if len(value) > 5: entryStr.set(value[:5])

def checkAnswer(guess, matrix):
    global turn, answer
    for i in range(5):
        if guess[i] == answer[i]:
            matrix[turn][i].configure(bg=_from_rgb(green))
        elif guess[i] in answer:
            matrix[turn][i].configure(bg=_from_rgb(yellow))

    if guess == answer:
        turn = 6
        print("You win!")
        inputBox.configure(state="disabled")
        submitBtn.configure(state="disabled")
        winLabel = Label(window, text="You win!", bg=_from_rgb(black), fg="white", font=winFont).grid(column=3, row=9)

def submitAnswer(entryStr, matrix):
    global turn, words, answers
    guess = entryStr.get()
    if guess not in words and guess not in answers:
        print("Guess not found in word list.")
        return
    if turn < 6:
        if len(guess) != 5:
            print("Please enter a word that's 5 letters long.")
        else:
            for i in range(5):
                if matrix[turn][i]['text'] == " ":
                    matrix[turn][i]['text'] = guess[i].upper()
            entryStr.set("")
            checkAnswer(guess, matrix)
            turn += 1
    else:
        print("You've run out of turns :(")


myFont = ("Helvetica", 20, "bold")
winFont = ("Helvetica", 12, "bold")
submitFnt = ("Helvetica", 12)
darkGrey = (59,56,56)
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
window.columnconfigure(6,weight=1)
# Necessary to limit the string length
entryStr = StringVar()
entryStr.trace('w', limitEntry)

# Create the grid of buttons
matrix = []
for i in range(0,6):
    temp = []
    for j in range(0,5):
        temp.append(Button(window, text=" ", font = myFont, width=4,height=2, bg=_from_rgb(darkGrey), borderwidth=.5,fg="white", state="disabled", disabledforeground="white"))
        temp[j].grid(row=i, column=j+1) # +1 for the left margin

    matrix.append(temp)

# Allows enter key to call submit function, nice!
window.bind("<Return>", (lambda event: submitAnswer(entryStr, matrix) ))

inputBox = Entry(window, width=12, textvariable=entryStr)
inputBox.grid(row=7, column=3)
submitBtn = Button(window, text="Enter", font = submitFnt, width=6,height=1, bg=_from_rgb(darkGrey), fg="white", command=lambda: submitAnswer(entryStr, matrix))
submitBtn.grid(column = 3, row = 8)
# warningLabel = Label(window, text=" ", bg=_from_rgb(darkGrey))
# warningLabel.grid(column=3, row=9)


window.mainloop()
