from tkinter import *
from random import *
import time
tk = Tk()

# Game Configurations
canvasHeight = 800 # Change these numbers to look good on your machine
canvasWidth = 1500 # Change these numbers to look good on your machine
backgroundColor = "black"
ballSize = 20
gravity = 2
gameStep = .0001
flapHeight = 60
obstacleWidth = 140 # How wide is each obstacle
gapSpace = 150 # Gap size between the two "pipes"
spaceBetween = 500 # Space between obstacles


global gameOver
gameOver = False
# Create the canvas
global c
c = Canvas(tk, bg=backgroundColor, height=canvasHeight, width=canvasWidth)

class obstacle:
        def __init__(self,color):
            global c
            self.step = 15
            # TOP RECTANGLE
            self.TopX1 = canvasWidth - obstacleWidth
            self.TopY1 = 0
            self.TopX2 = canvasWidth
            self.TopY2 = randint(100,600) # from random import * at the top
            self.rectTop = c.create_rectangle(self.TopX1, self.TopY1, self.TopX2, self.TopY2, fill=color)

            # BOTTOM RECTANGLE
            self.BotX1 = canvasWidth - obstacleWidth
            self.BotY1 = 0
            self.BotX2 = canvasWidth
            self.BotY2 = randint(100,600) # from random import * at the top
            self.rectBot = c.create_rectangle(self.BotX1, self.BotY2, self.BotX2, self.BotY2, fill=color)

        def moveRect(self):
            self.TopX1 -= self.step # Change X positions
            self.TopX2 -= self.step

            c.coords(self.rectTop, self.TopX1,self.TopY1,self.TopX2,self.TopY2) # Redraw obstacle with new coords
            time.sleep(gameStep)

dot = c.create_oval(canvasWidth/6, canvasHeight/2, canvasWidth/6 + ballSize, canvasHeight/2 + ballSize, fill="white")
# add canvas to tk object
def flap(event):
    coords = c.coords(dot)
    c.coords(dot, coords[0], coords[1] - flapHeight, coords[2], coords[3] - flapHeight)
tk.bind("<space>", flap)

def checkLoss():
    global gameOver
    coords = c.coords(dot) # coords[0] == x1, coords[1] == y1, coords[2] == x2, coords[3] == y2
    if coords[1] < 0 or coords[3] > canvasHeight:
        gameOver = True


c.pack()
obst1 = obstacle("red")

while not gameOver:
    coords = c.coords(dot)
    c.coords(dot, coords[0], coords[1] + gravity, coords[2], coords[3] + gravity)
    obst1.moveRect() # <-------
    checkLoss()
    time.sleep(gameStep)
    tk.update()
