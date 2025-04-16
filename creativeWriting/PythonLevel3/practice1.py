import tkinter as tk

# Define what a person is in our program

'''
I think lesson 1 SHOULD have toStr command, 
because if I let them create more than a person class
Each object will need to know how to return a string for GUI 2.1 or so
But we can start by just printing variables (person1.name)

'''
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    def toStr(self):
        return f"Name:{self.name}\nAge:{self.age}"

'''
By the time we make Entry, we are on second session (GUI2.1)
but it feels like over kill. Will probably add to confusion of GUI.
We could leave Entry out, and just loosely add each person to the window
'''
class Entry:
    def __init__(self, person):
        self.person = person
        self.label = tk.Label(window, text=person.toStr())
        self.label.pack()


# Create person objects
person1 = Person("Brian", 32)
person2 = Person("Jake", 29)
person3 = Person("Dylan", 33)
person4 = Person("Ian", 34)

# Group objects together
people = [person1, person2, person3, person4]

# Build Window
window = tk.Tk()

entries = []

# Simultaneously creates entries on window, and stores them in a list. Not necessary for now, but maybe later?
for person in people:
    entries.append(Entry(person))
    

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
