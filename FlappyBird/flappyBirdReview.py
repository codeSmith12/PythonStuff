from tkinter import *
from random import *
import time

tk = Tk()
tk.geometry("1200x700")

canvasHeight = 700
canvasWidth = 1200
backgroundColor = "black"
gapSpace = 150
ballSize = 20
gravity = 2
gameStep = .0001
flapHeight = 50
obstacleWidth = 140
global gameOver
gameOver = False

def flap(event):
    coords = c.coords(dot)
    c.coords(dot, coords[0], coords[1] - flapHeight, coords[2], coords[3] - flapHeight)

    # 0 = x1, 1 = y1, 2 = x2, 3 = y2
def checkLoss(obst):
    global gameOver
    coords = c.coords(dot)
    obstCoords = coords(obst)
    if coords[1] < 0 or coords[3] > canvasHeight:
        gameOver = True
    elif

class obstacle:
    def __init__(self, color):
        self.step = 15
        self.TopX1 = canvasWidth - obstacleWidth
        self.TopY1 = 0
        self.TopX2 = canvasWidth
        self.TopY2 = randint(100,500)
        self.rectTop = c.create_rectangle(self.TopX1, self.TopY1, self.TopX2, self.TopY2, fill=color)

        self.BotX1 = self.TopX1
        self.BotY1 = self.TopY2 + gapSpace
        self.BotX2 = canvasWidth
        self.BotY2 = canvasHeight
        self.rectBot = c.create_rectangle(self.BotX1, self.BotY1, self.BotX2, self.BotY2, fill=color)

    def moveRect(self):
        self.TopX1 -= self.step
        self.TopX2 -= self.step

        self.BotX1 -= self.step
        self.BotX2 -= self.step

        c.coords(self.rectTop, self.TopX1, self.TopY1, self.TopX2, self.TopY2) # Redraw obstacle with new coords
        c.coords(self.rectBot, self.BotX1, self.BotY1, self.BotX2, self.BotY2) # Redraw obstacle with new coords




tk.configure(background='black')

tk.bind("<space>", flap)

c = Canvas(tk, bg=backgroundColor, height=canvasHeight, width=canvasWidth)
dot = c.create_oval(canvasWidth/6, canvasHeight/2, canvasWidth/6 + ballSize, canvasHeight/2 + ballSize, fill="white")
obst1 = obstacle("red")


c.pack()
while not gameOver:
    coords = c.coords(dot) # coords[0]=='x1', [1] == y1, [2] == x2, [3] y2
    c.coords(dot, coords[0], coords[1] + gravity, coords[2], coords[3] + gravity)
    obst1.moveRect()
    tk.update()
    checkLoss()
    time.sleep(gameStep)
