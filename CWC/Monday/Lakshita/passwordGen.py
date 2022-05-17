from tkinter import *
from random import choice, randint

nouns = ["phone", "mouse", "screen",
        "pickle", "moose",
        "dog", "cat", "bird","dolphin",
        "stapler", "basket", "light",
        "keyboard", "seal",
        "giraffe", "hotdog", "pasta",
        "sushi", "fish", "donut",
        "icecream", "cookie"]

adjectives = ["red", "colorful", "prickly",
             "blue", "light", "heavy",
             "rough", "sour", "sticky",
             "smelly", "sweet", "pasty",
             "dusty", "clean", "chubby",
             "skinny", "smooth", "slippery",
             "nasty", "fishy", "stale", "snarky",
             "nice", "mean", "angry", "sad", "yummy",
             "yucky", "salty", "cold", "hot", "savory",
             "spicy"
             ]


# HOMEWORK: Add a number to the end of the string
def generatePassword():
    password = choice(adjectives).capitalize()
    password += choice(nouns).capitalize()
    print(password)


# CONSTANTS
WIDTH = 600
HEIGHT = 400


tk = Tk()
tk.title("Password Generator")
tk.geometry(f"{WIDTH}x{HEIGHT}")

# Row 1, title
titleLabel = Label(tk, text="Title:")
titleLabel.grid(row=0, column=0)
titleValue = Text(tk, height=1, width=20)
titleValue.grid(row=0, column=1, sticky=W)

# Row 2, length
lengthLabel = Label(tk, text="Length:")
lengthLabel.grid(row=1, column=0)
spin = Spinbox(tk, from_ = 8, to=16, width=2)
spin.grid(row=1, column=1, sticky=W)

# Row 3, password value box
passwordValue = Text(tk, height=1, width=40)
passwordValue.grid(row=2, column=1)

generateButton = Button(tk, text="Generate", command=generatePassword)
generateButton.grid(row=3, column=1, sticky=W)

decryptButton = Button(tk, text="Decrypt")
decryptButton.grid(row=3, column=1)


tk.mainloop()
