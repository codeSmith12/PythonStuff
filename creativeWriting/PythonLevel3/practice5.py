import tkinter as tk
from pathlib import Path
import random







'''
but now we need a reason to have a high score, somehow using tkinter?
Could still be clicker game, could be matching game, seeing as reading and writing to files is 
going to always be handled..

Clicker game would allow for continuation by reading files. 
It's a simple enough game to make / animate using tkinter's widgets

Idea to incorporate progress bar,
click until bar is complete, then you gain something in the game
Maybe that's an extra click per or maybe you just get a fixed amount of cash?
or just when you make purchases a bar pops up ?
Can we figure out how to do extra alert windows?


IDEALLY WE WILL NEED TO BE ABLE TO LOG IN, maybe just take a name, no password stuff, unless we have lots of time...



Components of cookie clicker
Left: image of cookie to click on.... expands / jiggles when hovered
Mid: Cartoonish displays of the upgrades you have...
Right: Upgrades, each entry is greyed out and red text until you click enough,
        now it lights up and text green 
All actions have sounds of course...

Make a hitbox around the dimensions of the label which holds an image...



'''


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

for row in range(3):
    for col in range(3):
        tk.Label(window, bg=random.choice(colors), text="1", font=FONT).grid(row=row, column=col, sticky="EW")

entries = []


'''
Build GUI right here dude...
Need grid(col =1-3

Learn how to get Pillow, it sounds like my computer has multiple python installations...


'''
# cookieImg = tk.PhotoImage(PROJ_DIR / "cookie.jpg")
# cookieLabel = tk.Label(window, image=cookieImg)


def buildHighScore():
    window.title("High Scores!")

    header = tk.Label(window, text="High Scores:")
    header.pack()

    # Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
    for i in range(NUM_TOP_SCORES):
        entries.append(Entry(players[i]))


# buildHighScore()
'''


'''
    

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
