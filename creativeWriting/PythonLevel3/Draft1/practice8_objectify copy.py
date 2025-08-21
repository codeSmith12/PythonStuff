import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time

'''
This part focuses on refactoring the code. For a while, we've had a lot of loose code. This isn't ideal and is not the OOP way of doing things.
For the class, we will be shuffling things around and encapsulating all of our data into a big game class

____________________

Another note, do we want playerData file to hold only 1 players data or do we want to have multiple?

If we have multiple, we'd have to add some kind of login system. It would also allow us to continue the idea of having a high score panel
If we have 1, there's a lot less work but it also makes the high score part not important... Maybe they use it for their own game.



'''
# Create the skeleton of your new game object
class ClickerGame:
    def __init__(self):
        # Make all game variables
        self.score = 100000
        self.clickMultiplier = 1
        self.clickerCost = 20
        self.passiveMultiplier = 0
        self.passiveCost = 100
        self.passiveActive = False # Game will not start calling passive function until it's purchased once
        self.tickSpeed = 1
        self.tickSpeedCost = 1000
        self.luck = 0
        self.luck_increment = 2
        self.luckCost = 10000
        self.criticalMultiplier = 20
        self.critical_increment = 10
        self.criticalCost = 20000
        
        # Call member function to build game GUI
        self.buildGUI()

    def buildGUI(self):
        # GUI Constants
        WIDTH = 1200
        HEIGHT = 800
        # Build Window
        self.window = tk.Tk()
        self.window.title("Cookie Clicker") # added this Practice7, should have been added a long time ago
        self.window.geometry(f"{WIDTH}x{HEIGHT}")
        PROJ_DIR = Path(__file__).parent
        # Using this variable allows us to easily change the file we want to read from
        FILE_NAME = "persons2.txt"

        # Create person objects
        # f = open(f"{PROJ_DIR}/{FILE_NAME}", "r")

        # Build cookie stuff, not using self.X because these member variables don't need to be referenced after they've been built
        cookieImg = Image.open(PROJ_DIR / "cookie.jpg")
        cookieImg = cookieImg.resize((WIDTH//5,WIDTH//5))
        img = ImageTk.PhotoImage(cookieImg)
        cookieLabel = tk.Label(self.window, image=img)
        cookieLabel.bind("<Button-1>", self.clicked)
        cookieLabel.grid(row=2, column=2)

        # Create font object for the text in our program
        FONT = ("FixedSys", 20)
        
        # Displays the score above the cookie
        self.scoreLabel = tk.Label(self.window, text=f"Score: {self.score}", font=FONT)
        self.scoreLabel.grid(row=1, column=2)

        # Holds all of the upgrade buttons, not referenced outside of this, so not a member variable (no .self)
        upgradeFrame = tk.Frame(self.window)
        upgradeFrame.grid(row=2,column=3)

        self.clickerUpgrade = tk.Button(upgradeFrame, text=f"Buy Multiplier for {self.clickerCost}", font=FONT)
        self.clickerUpgrade.bind("<Button-1>", self.buyClicker)
        self.clickerUpgrade.pack()

        self.passiveUpgrade = tk.Button(upgradeFrame, text=f"Buy Passive Cookies for {self.passiveCost}", font=FONT)
        self.passiveUpgrade.bind("<Button-1>", self.buyPassive)
        self.passiveUpgrade.pack()

        self.tickSpeedUpgrade = tk.Button(upgradeFrame, text=f"Buy Tick Speed for {self.tickSpeedCost}", font=FONT)
        self.tickSpeedUpgrade.bind("<Button-1>", self.buyTickSpeed)
        self.tickSpeedUpgrade.pack()

        self.luckUpgrade = tk.Button(upgradeFrame, text=f"Buy 2% of luck for {self.luckCost}", font=FONT)
        self.luckUpgrade.bind("<Button-1>", self.buyLuck)
        self.luckUpgrade.pack()

        self.critClickMulti = tk.Button(upgradeFrame, text=f"Buy critical click multiplier {self.criticalCost}", font=FONT)
        self.critClickMulti.bind("<Button-1>", self.buyCritMultiplier)
        self.critClickMulti.pack()
        
        # Container for all of our stat labels
        statsFrame = tk.Frame(self.window)
        statsFrame.grid(row=2, column=4)

        self.multiplierLabel = tk.Label(statsFrame, text=f"Multiplier: {self.clickMultiplier}")
        self.multiplierLabel.pack()

        self.passiveMultiplierLabel = tk.Label(statsFrame, text=f"Cookies per Tick: {self.passiveMultiplier}")
        self.passiveMultiplierLabel.pack()

        self.tickSpeedUpgrade = tk.Label(statsFrame, text=f"Tick Speed: 5000 / {self.tickSpeed}")
        self.tickSpeedUpgrade.pack()

        self.luckUpgrade = tk.Label(statsFrame, text=f"Luck: {self.luck}%")
        self.luckUpgrade.pack()

        self.criticalUpgrade = tk.Label(statsFrame, text=f"Critical Multiplier: x{self.criticalMultiplier}")
        self.criticalUpgrade.pack()        

        # Add save and load button
        self.saveBtn = tk.Button(self.window, text="Save Game")
        self.saveBtn.grid(row=1,column=5)

        self.loadBtn = tk.Button(self.window, text="Load Game")
        self.loadBtn.grid(row=1,column=6)

        self.window.mainloop()

    def clicked(self, event):
        self.increment()
        self.update_display()

    def increment(self):
        critChance = random.randint(0,100)
        if critChance < self.luck:
            self.score += self.clickMultiplier * self.criticalMultiplier
        else:
            self.score += self.clickMultiplier  # + 100 for testing game
        self.update_display()

    def update_display(self):
        self.scoreLabel['text'] = f"Score: {self.score}"

    def update_stats(self):
        self.multiplierLabel["text"] = f"Multiplier: {self.clickMultiplier}"
        self.passiveMultiplierLabel["text"] = f"Cookies per Tick: {self.passiveMultiplier}"
        self.tickSpeedUpgrade["text"] = f"Tick Speed: 5000 / {self.tickSpeed}"
        self.luckUpgrade["text"] = f"Luck: {self.luck}%" 
        self.criticalUpgrade["text"] = f"Critical Multiplier: x{self.criticalMultiplier}"

    def buyClicker(self, events):
        if self.score >= self.clickerCost:
            self.score -= self.clickerCost
            self.clickMultiplier += 1
            self.update_display()
            self.update_stats()
        else:
            print("You need more money!")

    def buyPassive(self, events):
        if self.score >= self.passiveCost:
            self.score -= self.passiveCost
            self.passiveMultiplier += 1
            self.update_display()
            self.update_stats()
            if not self.passiveActive:
                self.passiveActive = True
                self.procPassive()
        else:
            print("You need more money!")

    def procPassive(self):
        self.score += self.passiveMultiplier
        self.update_display()
        self.update_stats()
        self.window.after(5000//self.tickSpeed, self.procPassive) 

    def buyTickSpeed(self, events):
        if self.score >= self.tickSpeedCost:
            self.score -= self.tickSpeedCost
            self.tickSpeed += 1
            self.update_display()
            self.update_stats()
        else:
            print("You need more money!")

    def buyLuck(self, events):
        if self.score >= self.luckCost:
            self.score -= self.luckCost
            self.luck += self.luck_increment
            self.update_display()
            self.update_stats()
        else:
            print("You need more money!")

    def buyCritMultiplier(self,events):
        if self.score >= self.criticalCost:
            self.score -= self.criticalCost
            self.criticalMultiplier += self.critical_increment
            self.update_display()
            self.update_stats()
        else:
            print("You need more money!")

    def save_data(self, events):
        pass

    def load_data(self, events):
        pass





clickerGame = ClickerGame()