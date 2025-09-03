import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time, json

'''

This file will focus on the saving and loading of data.

'''
# Create the skeleton of your new game object
class ClickerGame:
    def __init__(self):
        # Make all game variables, set to default values
        self.name = ""
        self.score = 0
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
        # FILE_NAME = "persons2.txt"

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

        loadSaveFrame = tk.Frame(self.window)
        loadSaveFrame.grid(row=1, column=5)

        self.accountEntry = tk.Entry(loadSaveFrame, text="User Name")
        self.accountEntry.pack()

        # Add save and load button
        self.saveBtn = tk.Button(loadSaveFrame, text="Save Game")
        self.saveBtn.bind("<Button-1>", self.save_data)
        self.saveBtn.pack()

        self.loadBtn = tk.Button(loadSaveFrame, text="Load Game")
        self.loadBtn.bind("<Button-1>", self.load_data)
        self.loadBtn.pack()

        self.window.mainloop()

    def clicked(self, event):
        self.increment()
        self.update_display()

    def increment(self):
        critChance = random.randint(0,100)
        if critChance < self.luck: # The higher luck the player has, the greater chance that the crit will "proc"
            self.score += self.clickMultiplier * self.criticalMultiplier
        else:
            self.score += self.clickMultiplier 
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
        '''
        When saving, we want to find an entry if it exists and update it.
        If it's not found, then we want to add it to the end
        '''
        
        
        print("Saving Player Data...")
        playerData = {
            "Name": self.accountEntry.get(),
            "Score": self.score,
            "Click Multiplier": self.clickMultiplier,
            "Passive Multiplier": self.passiveMultiplier,
            "Passive Active": self.passiveActive,
            "Tick Speed": self.tickSpeed,
            "Luck": self.luck,
            "Critical Multiplier": self.criticalMultiplier
        }
        # Get the directory the file is in to avoid "not found"
        PROJ_DIR = Path(__file__).parent
        # Using this variable allows us to easily change the file we want to read from
        FILE_NAME = "playerData.txt"
        # List that contains every dictionary read in, so we can update and output to the file, overwriting the current data
        listOfData = []
        playerFound = False
        # Create person objects

        with open(f"{PROJ_DIR}/{FILE_NAME}", "r") as outputFile: # Open in read mode so we can use readlines function
            # Read through each entry in the text file
            for line in outputFile.readlines():
                # Convert the line (str) into a dictionary
                if line != "\n": # Make sure the line isn't empty
                    curEntry = json.loads(line) # Converts a string into a dictionary
                    # Check if the name of the entry matches the user name that was entered
                    if curEntry["Name"] == self.accountEntry.get():
                        playerFound = True
                        # Update the players data
                        listOfData.append(playerData)
                    else:
                        # Else, place data back into list for re-writing to file
                        listOfData.append(curEntry)
        outputFile.close() # Closing so we can open in write, not read
        # Now that we've read everything in the list and updated the players data if it existed, write it all back to the file
        with open(f"{PROJ_DIR}/{FILE_NAME}", "w") as outputFile:
            for item in listOfData:
                json.dump(item, outputFile)
                outputFile.write("\n")

        outputFile.close() # Closing so we can open in append, not write
        # If we havent' returned by this time, that means we didn't find the user in our list, and we can just append the result to the end
        if not playerFound:
            with open(f"{PROJ_DIR}/{FILE_NAME}", "a") as outputFile:
                outputFile.write("\n")
                json.dump(playerData, outputFile)
            outputFile.close()

    def load_data(self, events):
        PROJ_DIR = Path(__file__).parent
        # Using this variable allows us to easily change the file we want to read from
        FILE_NAME = "playerData.txt"
        playerData = {}
        with open(f"{PROJ_DIR}/{FILE_NAME}", "r") as inputFile: #Open in read mode so we can use readlines function
            # Read through each entry in the text file
            for line in inputFile.readlines():
                # Convert the line (str) into a dictionary
                if line != "\n": # Make sure the line isn't empty
                    curEntry = json.loads(line)
                    # Check if the name of the entry matches the user name that was entered (Need input field for this)
                    if curEntry["Name"] == self.accountEntry.get():
                        print("Found")
                        playerFound = True
                        # Update the players data
                        playerData = curEntry
                    else:
                        print(f"{self.accountEntry.get()} not found")
        inputFile.close()        
        # If we found the player, store values found in file in our main objects variables
        if playerFound:
            self.name = playerData["Name"]
            self.score = playerData["Score"]
            self.clickMultiplier = playerData["Click Multiplier"]
            self.passiveMultiplier = playerData["Passive Multiplier"]
            self.passiveActive = playerData["Passive Active"]
            self.tickSpeed = playerData["Tick Speed"]
            self.luck = playerData["Luck"]
            self.criticalMultiplier = playerData["Critical Multiplier"]
            # Update all of the display with the newly entered stats
            self.update_display()
            self.update_stats()
            # Start the passive counting function if the player has purchased already
            if self.passiveActive:
                self.procPassive()
        else:
            print("Player not found...")




clickerGame = ClickerGame()