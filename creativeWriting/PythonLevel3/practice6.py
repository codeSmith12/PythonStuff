import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time

def update_display():
    scoreLabel.config(text=f"Score: {score}")

def clicked(event):
    print("Clicked!!")
    increment() 
    update_display()

'''

Other ideas for games... 

For the section, we want to create our upgrades.

Different ideas for upgrades:

x clicks per second
1 click per second/X
X clicks per ... click on cookie

critical click - can purchase "luck" stat which if proc'd will add multiplier * 100 or 1000 to click
or "On Fire" every click for a period of 5 seconds is worth 50x, this would probably be quick exciting
Another thing is this could be proc'd when a random button spawns in the grid, if clicked in 1 second then On Fire proc's

Could add sounds - not an upgrade but design feature.. 


'''

def buyClicker(events):
    global score, multiplier
    if score >= clickerCost:
        score -= clickerCost
        multiplier+=1
        update_display()
    else:
        print("You need more money!")

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
    global score, multiplier
    score+= multiplier
    scoreLabel.config(text=f"Score: {score}")

def buyPassive(events):
    print("Passive purchased")
    


# Build buttons for upgrades...
clickerCost = 20
global multiplier
multiplier = 1

# Make a frame to put all upgrade buttons into.
# this allows us to put multiple gui items into 1 grid spot
# this is in response to the cookie png making the grid to be much bigger than the buttons
# This will be the major part of this lesson, probably want them to try using grid with all of the buttons
# first to see why we need to use a frame.

upgradeFrame = tk.Frame(window)
upgradeFrame.grid(row=2,column=3)

clickerUpgrade = tk.Button(upgradeFrame, text=f"Buy Multiplier for {clickerCost}", font=FONT)
clickerUpgrade.bind("<Button-1>", buyClicker)
clickerUpgrade.pack()

passiveCost = 100
passiveUpgrade = tk.Button(upgradeFrame, text=f"Buy Passive Cookies for {passiveCost}", font=FONT)
passiveUpgrade.bind("<Button-1>", buyPassive)
passiveUpgrade.pack()

tickCost = 1000
tickSpeedUpgrade = tk.Button(upgradeFrame, text=f"Buy Tick Speed for {tickCost}", font=FONT)
tickSpeedUpgrade.pack()

luckCost = 10000
luckUpgrade = tk.Button(upgradeFrame, text=f"Buy 2% of luck for {luckCost}", font=FONT)
luckUpgrade.pack()

criticalCost = 20000
critClickMulti = tk.Button(upgradeFrame, text=f"Buy critical click multiplier {criticalCost}", font=FONT)
critClickMulti.pack()


# Might make sense to just use 1 label for this... it's a lot less work.
# can run 1 function to update the big label.... Shoulda done this first.
# It would all fit in the grid too....
# Build List of stats

statsFrame = tk.Frame(window)
statsFrame.grid(row=2, column=4)

multiplierLabel = tk.Label(statsFrame, text=f"Multiplier: {multiplier}")
multiplierLabel.pack()

passiveMulti = 1
passiveMultiplier = tk.Label(statsFrame, text=f"Cookies per Tick: {passiveMulti}")
passiveMultiplier.pack()

tickSpeed = 1
tickSpeedUpgrade = tk.Label(statsFrame, text=f"Tick Speed: 5000 / {tickSpeed}")
tickSpeedUpgrade.pack()

luck = 0
luckUpgrade = tk.Label(statsFrame, text=f"Chance to become 'On Fire': {luck}%")
luckUpgrade.pack()

criticalMultiplier = 50
criticalUpgrade = tk.Label(statsFrame, text=f"Critical Multiplier: x{criticalMultiplier}")
criticalUpgrade.pack()

saveBtn = tk.Button(window, text="Save Game")
saveBtn.grid(row=1,column=5)

loadBtn = tk.Button(window, text="Load Game")
loadBtn.grid(row=1,column=6)


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
