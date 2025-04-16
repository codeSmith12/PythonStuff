import tkinter as tk
from tkinter import ttk




'''

What does this build on?

Initially, I think that we should beautify the entries. 
Learn more about setting geometry of GUI,
use lines to deliniate each entry. 

Could probably develop the entry class in this project, not the first one.
This will reinforce Classes but also GUI
'''
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def toStr(self):
        return f"Name:{self.name}\nAge:{self.age}"

'''
'''
class Entry:
    def __init__(self, person):
        self.person = person
        self.label = tk.Label(window, text=person.toStr(), bg="black", fg="white",height=5, width=WIDTH-2)

        # Create empty label for spacer...?
        tk.Label(window, text="").pack()
        self.label.pack()
        tk.Label(window, text="").pack()



# Create person objects
person1 = Person("Brian", 32)
person2 = Person("Jake", 29)
person3 = Person("Dylan", 33)
person4 = Person("Ian", 34)

# Group objects together
people = [person1, person2, person3, person4]

# Constants
WIDTH = 400
HEIGHT = 600

# Build Window
window = tk.Tk()
window.title("Practice Project")
window.geometry(f"{WIDTH}x{HEIGHT}")

entries = []

# Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
for person in people:
    entries.append(Entry(person))
    

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
