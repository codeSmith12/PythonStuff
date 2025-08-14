import tkinter as tk
from tkinter import ttk
from pathlib import Path # This was added to get the containing folder of our script




'''
Homework:

HW after this assignment: Take a given file and create an object that can store each variable separately
(self.name = name, self.age = age, ect but with diff data), 
Extra credit is to read in the file and create many objects?


I think we should provide 1-3 files. Students will write Python code that will read in each line of a file
and create 1 object per line in the file.

Each object should be added to a list upon being instanciated
After reading in each object, students should loop through each object and call their toStr function, or print their information
to verify that each item was correctly read in.

'''




'''
Instead of making each Person manually, lets read from a file to get everyone created



'''

class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def toStr(self):
        return f"Name:{self.name}\nAge:{self.age}"


class Entry:
    def __init__(self, person):
        self.person = person
        self.label = tk.Label(window, text=person.toStr(), bg="black", fg="white",height=5, width=WIDTH-2)

        # Create empty label for spacer...?
        tk.Label(window, text="").pack()
        self.label.pack()
        tk.Label(window, text="").pack()

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
    person = Person(stripped[0], stripped[1])
    people.append(person)
    

# Constants
WIDTH = 200
HEIGHT = 600

# Build Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

entries = []

# Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
for person in people:
    entries.append(Entry(person))

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
