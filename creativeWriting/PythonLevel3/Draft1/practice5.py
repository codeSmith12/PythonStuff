import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time






'''
Homework idea:
Students have learned how to add images to the window, and were introduced to the grid.
Homework might be to make a collage of a topic of their choice.
They will need to gather 9(?) pictures, and display them in a window.
They will use lots of grid, and will likely need to resize images. Good practice!

'''

def clicked(event):
    print("Clicked!!")
    scoreLabel.config(text=f"Score: {score}")
    increment() 

def buyClicker(events):
    global score
    if score >= clickerCost:
        score -= clickerCost
        # give benefit ...

colors = ["red","green","blue","yellow","purple"]

class PlayerScore:
    def __init__(self, name,score):
        self.name = name
        self.score = score
    def toStr(self):
        return f"{self.name}: {self.score}"


# Would like to make something thats easier to decorate than just the label...
# Like an item in a vbox?
class Entry:
    def __init__(self, playerScore):
        self.playerScore = playerScore
        self.label = tk.Label(window, text=playerScore.toStr(), bg="black", fg="lime",height=1,pady=15, width=WIDTH-2, font=FONT)
        # Create empty label for spacer...?
        self.label.pack()

# Get the directory the file is in to avoid "not found"
PROJ_DIR = Path(__file__).parent
# Using this variable allows us to easily change the file we want to read from
FILE_NAME = "persons2.txt"

# Create person objects
f = open(f"{PROJ_DIR}/{FILE_NAME}", "r")

# Group objects together
players = []

# Parse players and scores from file
for line in f.readlines():
    stripped = line.split(",")
    playerScore = PlayerScore(stripped[0], stripped[1])
    players.append(playerScore)
    
# Sort list of PlayerScore objects by their scores so we can easily grab the top few
players.sort(key=lambda x: x.score, reverse=True) # Reverse for decending values

# Constants
WIDTH = 1200
HEIGHT = 800

# How many player scores will we list on our board
NUM_TOP_SCORES = 9 # chose 9 because thats how many fit on the window..

FONT = ("FixedSys", 20)

# Build Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

# for row in range(3):
#     for col in range(3):
#         tk.Label(window, bg=random.choice(colors), text="1", font=FONT).grid(row=row, column=col, sticky="EW")

entries = []

# Build cookie stuff
global cookieImg, cookieLabel
cookieImg = Image.open(PROJ_DIR / "cookie.jpg")
cookieImg = cookieImg.resize((WIDTH//5,WIDTH//5))
img = ImageTk.PhotoImage(cookieImg)
cookieLabel = tk.Label(window, image=img)
cookieLabel.bind("<Button-1>", clicked)
cookieLabel.grid(row=2, column=2)

# Build Score
global score, scoreLabel
score = 0
scoreLabel = tk.Label(window, text=f"Score: {score}", font=FONT)
scoreLabel.grid(row=1, column=2)

#??
def increment():
    global score
    score+=1
    scoreLabel.config(text=f"Score: {score}")


def buildHighScore():
    window.title("High Scores!")

    header = tk.Label(window, text="High Scores:")
    header.pack()

    # Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
    for i in range(NUM_TOP_SCORES):
        entries.append(Entry(players[i]))


# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
