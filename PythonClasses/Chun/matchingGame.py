import tkinter as tk
import random

class Tile:
    def __init__(self, window, color, row, col):
        self.color = color
        self.flipped = False
        self.matched = False
        self.label = tk.Label(window, width=10, height=5, bg="grey")
        self.label.bind('<Button-1>', self.flip)
        self.label.grid(row=row, column=col, padx=5, pady=5)


    def flip(self, event):
        global guess
        if not self.flipped and not self.matched and len(guess) < 2:
            self.label.config(bg=self.color)
            self.flipped = True
            guess.append(self) # concatenate
            if len(guess) == 2:
                window.after(1000, checkMatch)
            
def checkMatch():
    global guess, tries,scoreLabel
    
    tries += 1
    scoreLabel.config(text=f"Score: {tries}")
    if guess[0].color == guess[1].color:
        guess[0].matched = True
        guess[1].matched = True
    else:
        for tile in guess:
            tile.label.config(bg="grey")
            tile.flipped = False
    guess.clear()
    

window = tk.Tk()
window.title("Memory Game")
WINDOW_WIDTH = 425
WINDOW_HEIGHT = 425

tries = 0

colors = ["cyan", "light sky blue", "medium spring green", "light salmon", "medium orchid", "orange red", "dark olive green", "chartreuse"] * 2
guess = []

window.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")

for i in range(4):
    for j in range(4):
        # Grab random color
        color = random.choice(colors)
        # Remove the color from the list
        colors.remove(color) # Save the new list in the same variable
        tile = Tile(window, color, i, j)


scoreLabel = tk.Label(window, text=f"Score: {tries}")
scoreLabel.grid(row=5,column=1)
window.mainloop()