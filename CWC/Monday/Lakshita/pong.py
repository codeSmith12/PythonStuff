#pong.py
# Take out all of the tkinter tools
from tkinter import *
import time


class Ball:
    def __init__(self):
        self.y = -BALLSPEED # Negative to make ball start going up
        self.x = BALLSPEED # Positive to send the ball towards the bot at first
        self.id = canvas.create_oval(WIDTH/2 - BALLSIZE/2, HEIGHT/2 - BALLSIZE/2, WIDTH/2 + BALLSIZE/2, HEIGHT/2 + BALLSIZE/2, fill="white")


        # Need to use playerPos and opPos to detect for bounce
    def updatePosition(self, playerPos, opPos):
        global playerScore, botScore
        canvas.move(self.id, self.x, self.y)
        pos = canvas.coords(self.id)
        if pos[1] < 0 or pos[3] > HEIGHT:
            self.y = -self.y
        if pos[2] > WIDTH:
            playerScore += 1
            print("Player score:", playerScore)
            self.resetPosition()
        if pos[0] < 0: # Do the rest for the bot
            botScore += 1
            print("Bot score:", botScore)
            self.resetPosition()

    def getCoords(self):
        return canvas.coords(self.id)

    def resetPosition(self):
        canvas.moveto(self.id, WIDTH/2 - BALLSIZE/2, HEIGHT/2 - BALLSIZE/2)
        self.y = -self.y # Negative to make ball start going up
        self.x = -self.x # Positive to send the ball towards the bot at first

class Paddle:
    NUM_PADDLE=0 # Variable held by the class itself...
    def __init__(self):
        self.y = 0 # Variable that controls direction of motion
        self.bot = False
        if Paddle.NUM_PADDLE == 0:
            self.id = canvas.create_rectangle(WIDTH/26, HEIGHT/2 - PADDLEHEIGHT/2, WIDTH/26 + PADDLEWIDTH, HEIGHT/2 + PADDLEHEIGHT/2, fill="white")
            window.bind("<KeyPress-Down>", self.moveDown)
            window.bind("<KeyPress-Up>", self.moveUp)
            Paddle.NUM_PADDLE += 1
        else:
            self.id = canvas.create_rectangle(WIDTH*25/26, HEIGHT/2 - PADDLEHEIGHT/2, WIDTH*25/26 + PADDLEWIDTH, HEIGHT/2 + PADDLEHEIGHT/2, fill="white")
            self.bot = True


    def moveDown(self,key):
        self.y = SPEED
        # canvas.move(player, 0,10)
    def moveUp(self,key):
        self.y = -SPEED
        # canvas.move(player, 0,-10)
    def updatePosition(self, ballCoords):
        canvas.move(self.id, 0, self.y)
        pos = canvas.coords(self.id)

        if self.bot:
            if ballCoords[1] < pos[1]:
                self.moveUp("key")
            elif ballCoords[3] > pos[3]:
                self.moveDown("key")
        # Bounce if paddle goes out of bounds (top or bottom)

        if pos[3] > HEIGHT or pos[1] < 0:
            self.y = -self.y

    def getCoords(self):
        return canvas.coords(self.id)

# create a tk object
window = Tk()
window.title("Pong Game")

# Game constants
WIDTH = 800
HEIGHT = 600
PADDLEWIDTH = 10
PADDLEHEIGHT = 50
BALLSIZE = 20
BALLSPEED = 2
SPEED = 3
TICK = 0.01
global playerScore
playerScore = 0
global botScore
botScore = 0
global canvas
canvas = Canvas(window, width=WIDTH, height=HEIGHT)
canvas.configure(bg="black") # set the background color to black
canvas.pack()

player = Paddle()
opponent = Paddle()
global ballCoords
ball = Ball()

while True:
    ballCoords = ball.getCoords() # Couldnt seem to get ball coords in paddles updatepos so we did it outside of the function
    playerPos = player.getCoords() # Couldnt seem to get player coords in balls updatepos so we did it outside of the function
    opPos = opponent.getCoords() # Couldnt seem to get opponent coords in balls updatepos so we did it outside of the function
    player.updatePosition(ballCoords)
    opponent.updatePosition(ballCoords)
    ball.updatePosition(playerPos, opPos)
    window.update()
    time.sleep(TICK)
