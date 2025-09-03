import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time
'''
HW:
Cycle through cookie images as score increases
Ask them to figure it out :)




'''
def update_display():
    scoreLabel.config(text=f"Score: {score}")

def clicked(event):
    print("Clicked!!")
    increment() 
    update_display()

def buyClicker(events):
    global score, multiplier
    if score >= clickerCost:
        score -= clickerCost
        multiplier+=1
        update_display()
        updateStats()
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
window.title("Cookie Clicker") # added this Practice7, should have been added a long time ago
window.geometry(f"{WIDTH}x{HEIGHT}")

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
score = 100000
scoreLabel = tk.Label(window, text=f"Score: {score}", font=FONT)
scoreLabel.grid(row=1, column=2)

#??
def increment():
    global score, multiplier
    critChance = random.randint(0,100)
    if critChance <= luck:
        score+= multiplier * criticalMultiplier
    else:
        score+= multiplier  # + 100 for testing game
    scoreLabel.config(text=f"Score: {score}")

# The meat of this file is to flesh out the functions for the upgrade buttons.
def buyPassive(events):
    global score, startPassive, passive
    if score >= passiveCost:
        score -= passiveCost
        passive+=1
        update_display()
        updateStats()
        if not startPassive:
            startPassive = True
            procPassive()
    else:
        print("You need more money!")

def procPassive():
    global score
    score += passive
    update_display()
    updateStats()
    window.after(5000//tickSpeed, procPassive) # Only takes integers for tick, so double divide // to convert to integer


def buyTickSpeed(events):
    global score, tickSpeed, tickCost
    if score >= tickCost:
        score -= tickCost
        tickSpeed += 1
        update_display()
        updateStats()
    else:
        print("You don't have enough money")
    
def buyLuck(events):
    global score, luckCost, luck
    if score >= luckCost:
        if luck <= 50:
            score -= luckCost
            luck += 2
            update_display()
            updateStats()
        else:
            print("You have the maximum amount of luck")
        
    
def buyCritMultiplier(events):
    global score, criticalMultiplier
    if score >= criticalCost:
        score -= criticalCost
        criticalMultiplier += 10
        update_display()
        updateStats()
    else:
        print("You don't have enough money")

clickerCost = 20
global multiplier
multiplier = 1
global passive
passive = 0
global startPassive
startPassive = False

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
tickSpeedUpgrade.bind("<Button-1>", buyTickSpeed)
tickSpeedUpgrade.pack()

luckCost = 10000
luckUpgrade = tk.Button(upgradeFrame, text=f"Buy 2% of luck for {luckCost}", font=FONT)
luckUpgrade.bind("<Button-1>", buyLuck)
luckUpgrade.pack()

criticalCost = 20000
critClickMulti = tk.Button(upgradeFrame, text=f"Buy critical click multiplier {criticalCost}", font=FONT)
critClickMulti.bind("<Button-1>", buyCritMultiplier)
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
passiveMultiplier = tk.Label(statsFrame, text=f"Cookies per Tick: {passive}")
passiveMultiplier.pack()

tickSpeed = 1

tickSpeedUpgrade = tk.Label(statsFrame, text=f"Tick Speed: 5000 / {tickSpeed}")
tickSpeedUpgrade.pack()

global luck
luck = 0
luckUpgrade = tk.Label(statsFrame, text=f"Luck: {luck}%")
luckUpgrade.pack()

criticalMultiplier = 50
criticalUpgrade = tk.Label(statsFrame, text=f"Critical Multiplier: x{criticalMultiplier}")
criticalUpgrade.pack()

saveBtn = tk.Button(window, text="Save Game")
saveBtn.grid(row=1,column=5)

loadBtn = tk.Button(window, text="Load Game")
loadBtn.grid(row=1,column=6)

def updateStats():
    multiplierLabel["text"] = f"Multiplier: {multiplier}"
    passiveMultiplier["text"] = f"Cookies per Tick: {passive}"
    tickSpeedUpgrade["text"] = f"Tick Speed: 5000 / {tickSpeed}"
    luckUpgrade["text"] = f"Luck: {luck}%" 
    criticalUpgrade["text"] = f"Critical Multiplier: x{criticalMultiplier}"

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
