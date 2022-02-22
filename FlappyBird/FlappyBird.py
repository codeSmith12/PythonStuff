from tkinter import *
from random import randint
import time
# from PIL import ImageTk, Image

# Game Configurations
canvasHeight = 800
canvasWidth = 1500
obstacleWidth = 140 # How wide is each obstacle
gapSpace = 150 # Gap size between the two "pipes"
spaceBetween = 500 # Space between obstacles
gameStep = .00000001 # Time between each game loop
gravity = 2 # How fast gravity pulls down
flapHeight = 60 # How high each flap brings the dot
textSize = 10
gameTime = 0 # Starting time, counts up as the player goes
startX = canvasWidth/6
startY = canvasHeight/2
ballSize = 20 # Radius? of the ball


# Create window and canvas to draw on
tk = Tk()
c = Canvas (tk, bg="black",height=canvasHeight, width=canvasWidth)
# timer = c.create_text(canvasWidth/2, 0, text=("Time:",gameTime))
c.pack() # add canvas to the tk


class Bird:
    def __init__(self, canvas,color):
        self.dot = c.create_oval(startX, startY,startX + ballSize, startY + ballSize,fill=color)
        self.c = canvas
        self.score = 0
        self.x = self.c.coords(self.dot)[0]
        self.y = self.c.coords(self.dot)[1]
        self.debounce = True # Used for jump cooldown... but not really.
        tk.bind("<space>",self.spacePressed)

    def spacePressed(self, event):
        if self.debounce == True:
            self.debounce == False
            self.y -= flapHeight
            self.c.coords(self.dot, self.x, self.y, self.x + ballSize, self.y + ballSize)
            tk.update()
            self.debounce == True

    def gravityTic(self):
        self.y += 10
        self.c.coords(self.dot, self.x, self.y, self.x + ballSize, self.y + ballSize)
        tk.update()

class FlappyBirdGame:
    def __init__(self, birds, obstacles):
        self.birds = birds
        self.gameOver = False
        self.obstacles = obstacles
        self.mainLoop()
        # self.firstRun = True

    def checkLoss(self):
        for obst in self.obstacles:
            coords2 = c.coords(obst.rectBot)
            coords3 = c.coords(obst.rectTop)
            for i in range(len(birds)):
                coords1 = self.birds[i].c.coords(self.birds[i].dot)
                if coords1[0] < 0 or coords1[1] < 0 or coords1[2] > canvasWidth or coords1[3] > canvasHeight:
                    # Output information here before ending game ?
                    self.gameOver = True
                elif coords1[0] > coords2[0] and coords1[1] > coords2[1] and coords1[2] < coords2[2] and coords1[3] < coords2[3]:
                    self.gameOver = True
                elif coords1[0] > coords3[0] and coords1[1] > coords3[1] and coords1[2] < coords3[2] and coords1[3] < coords3[3]:
                    self.gameOver = True

    def mainLoop(self):
        print("Beginning game.")
        while self.gameOver == False:
            for bird in birds:
                bird.gravityTic()
            self.checkLoss()
            # if self.firstRun == True:
            for obst in self.obstacles:
                obst.moveRect()
                # self.firstRun = False
            # time.sleep(gameStep)
            tk.update()



class obstacle:
    def __init__(self, color, num):
        self.step = 15
        # Top obst
        self.x3 = canvasWidth - obstacleWidth + (num * spaceBetween) # num * spacebetween allows us to put the obstacles spaced away
        self.y3 = 0
        self.x4 = canvasWidth + (num * spaceBetween)
        self.y4 =  randint(100, 600)
        self.rectTop = c.create_rectangle(self.x3, self.y3, self.x4, self.y4, fill=color)

        # Bottom obst
        self.x1 = canvasWidth - obstacleWidth + (num * spaceBetween)
        self.y1 = self.y4 + gapSpace
        self.x2 = canvasWidth + (num * spaceBetween)
        self.y2 = canvasHeight
        self.rectBot = c.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill=color)

            #self.c.coords(self.dot, self.x, self.y, self.x + ballSize, self.y + ballSize)
    def moveRect(self):
        self.x1 -= self.step
        self.x2 -= self.step
        self.x3 -= self.step
        self.x4 -= self.step

        c.coords(self.rectBot, self.x1, self.y1,self.x2 ,self.y2 )
        c.coords(self.rectTop, self.x3, self.y3,self.x4 ,self.y4 )
        coords1 = c.coords(self.rectTop)
        coords2 = c.coords(self.rectBot)
        if coords1[2] < 0:
            print("Resetting location")
            # top obby
            self.x3 = canvasWidth-obstacleWidth
            self.y3 = 0
            self.x4 = canvasWidth
            self.y4 =  randint(100,600)

            # bot obby
            self.x1 = canvasWidth-obstacleWidth
            self.y1 = self.y4 + gapSpace
            self.x2 = canvasWidth
            self.y2 = canvasHeight
            c.coords(self.rectBot, self.x1, self.y1,self.x2 ,self.y2)
            c.coords(self.rectTop, self.x3, self.y3,self.x4 ,self.y4)



        time.sleep(gameStep)








bird1 = Bird(c, "white")
startX = startX + 20
#bird2 = Bird(c, "blue")
birds = [bird1]
obst1 = obstacle("red", 1)
obst2 = obstacle("red", 2)
obst3 = obstacle("red", 3)
obstacles = [obst1,obst2,obst3]
game = FlappyBirdGame(birds,obstacles)


# while true update
