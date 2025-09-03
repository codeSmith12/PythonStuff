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
This lesson makes a large jump in the completion of the GUI. I think it's unlikely students will have enough time to finish
Their homework could be to finish the lay out.
If they did end up finishing, I think more practice with frames is a good idea. 


'''

def buyClicker(events):
    global score, multiplier
    if score >= clickerCost:
        score -= clickerCost
        multiplier+=1
        update_display()
    else:
        print("You need more money!")


# Get the directory the file is in to avoid "not found"
PROJ_DIR = Path(__file__).parent

# Constants
WIDTH = 1200
HEIGHT = 800

FONT = ("FixedSys", 20)

# Build Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

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

# Put these in but should have waited for practice 7 file. Maybe remove when cleaning up files.
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
clickerUpgrade.pack()

passiveCost = 100
passiveUpgrade = tk.Button(upgradeFrame, text=f"Buy Passive Cookies for {passiveCost}", font=FONT)
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


# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
