import tkinter as tk
from pathlib import Path
import random
from PIL import Image, ImageTk
import time






'''
Homework idea:
Students have learned how to add images to the window, and were introduced to the grid.
Homework might be to make a collage of a topic of their choice.
They will need to gather 9(?) pictures, and display them in a window.
They will use lots of grid, and will likely need to resize images. Good practice!
'''

def clicked(event):
    print("Clicked!!")
    increment() 

# Constants
WIDTH = 1200
HEIGHT = 800

# How many player scores will we list on our board
NUM_TOP_SCORES = 9 # chose 9 because thats how many fit on the window..

FONT = ("FixedSys", 20)

# Build Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

PROJ_DIR = Path(__file__).parent

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
    global score
    score+=1
    scoreLabel.config(text=f"Score: {score}")

# Keep this at the bottom of the program,
# This command keeps the window open
window.mainloop()
