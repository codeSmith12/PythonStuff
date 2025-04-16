import tkinter as tk
from tkinter import ttk
from pathlib import Path # This was added to get the containing folder of our script





'''
So we can read into files, we can build objects and can build simple guis. Now what?
Start building towards something?

Maybe take 2 files, heroes and enemies, and read them in,
or build with canvas ?

What kind of game can I make with this?
Castles and Creatures, but with GUI?

Some kind of puzzle game ? The matching game ?

THIS COULD BE THAT WE READ IN NAMES AND HIGH SCORES,
THEN WE BUILD AN ENTRY FOR EACH OF THE TOP X !!!!!!

This gives purpose to everything we've made so far
Can maybe spend more time beautifying our gui, as this is more permanent.

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



Show kids different attributes to change, like font colors, families
Give them time to find things they like



'''
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
people = []

# Get one line of the document
# line1 = f.readline()
# print(line1)

# Loop through each line of the file, 

# creating a person object with the data


# f.readlines returns a list of strings
# Loop through each item in the list, 
# and separate into individual data bits (name, age) using .split
# Create a person object with the array with 2 items, using indexes
# Add object into list so our window can build each entry, as it has in the past
for line in f.readlines():
    stripped = line.split(",")
    playerScore = PlayerScore(stripped[0], stripped[1])
    people.append(playerScore)
    
# Sort list of PlayerScore objects by their scores so we can easily grab the top few
people.sort(key=lambda x: x.score, reverse=True)# Reverse for decending values
# for person in people:
#     print(person.toStr())


# Constants
WIDTH = 400
HEIGHT = 600

# How many player scores will we list on our board
NUM_TOP_SCORES = 9 # chose 9 because thats how many fit on the window..

FONT = ("FixedSys", 20)

# Build Window
window = tk.Tk()
window.title("High Scores!")
window.geometry(f"{WIDTH}x{HEIGHT}")

header = tk.Label(window, text="High Scores:")
header.pack()

entries = []

# Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
for i in range(NUM_TOP_SCORES):
    entries.append(Entry(people[i]))
    

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
