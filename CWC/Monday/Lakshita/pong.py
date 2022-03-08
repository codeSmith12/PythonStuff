#pong.py
# Take out all of the tkinter tools
from tkinter import *
import time


# Note: Maybe place line down the middle to simulate a pong table
# NOTE: Need to increase speed to make bot able to lose
class Ball:
    def __init__(self):
        self.y = -BALLSPEED # Negative to make ball start going up
        self.x = BALLSPEED # Positive to send the ball towards the bot at first
        self.id = canvas.create_oval(WIDTH/2 - BALLSIZE/2, HEIGHT/2 - BALLSIZE/2, WIDTH/2 + BALLSIZE/2, HEIGHT/2 + BALLSIZE/2, fill="white")
        self.bounced = False # <--- Added to stop ball from bouncing inside of the paddle
        self.delay = 0 # <---- Keeps track of how much time since last bounce
        # self.speedIncrease = 0

    def updatePosition(self, playerPos, opPos):
        global playerScore, botScore
        canvas.move(self.id, self.x, self.y)
        pos = canvas.coords(self.id)
        self.delay +=1

        if not self.bounced:# <---- If we haven't bounced in the past 10 ticks
            if pos[2] >= opPos[0] and (pos[3] >= opPos[1] and pos[3] <= opPos[3] or pos[1] >= opPos[1] and pos[1] <= opPos[3]):
                # self.speedIncrease += .5
                # self.x = BALLSPEED + self.speedIncrease
                self.x = -self.x
                self.bounced = True# <---- Flag that bounce has occurred
            if pos[0] <= playerPos[2] and (pos[1] >= playerPos[1] and pos[1] <= playerPos[3] or pos[3] >= playerPos[1] and pos[3] <= playerPos[3]):
                # self.speedIncrease += .5
                # self.x = BALLSPEED + self.speedIncrease
                self.x = -self.x
                self.bounced = True# <---- Flag that bounce has occurred
        if self.delay == 50:# If 10 ticks have transpired, reset ability to bounce
            self.delay = 0# <----
            self.bounced = False# <----

        if pos[1] < 0 or pos[3] > HEIGHT:
            self.y = -self.y
        if pos[2] > WIDTH:
            playerScore += 1
            player.increaseScore()
            self.resetPosition()
        if pos[0] < 0: # Do the rest for the bot
            botScore += 1
            opponent.increaseScore()
            self.resetPosition()

    def getCoords(self):
        return canvas.coords(self.id)

    def resetPosition(self):
        canvas.moveto(self.id, WIDTH/2 - BALLSIZE/2, HEIGHT/2 - BALLSIZE/2)
        self.y = -self.y # Negative to make ball start going up
        # self.speedIncrease = 0
        self.x = -self.x # Positive to send the ball towards the bot at first

class Paddle:
    NUM_PADDLE=0 #  Keeps track of which paddle we are creating
    def __init__(self):
        self.y = 0 # Variable that controls direction of vertical motion
        self.bot = False
        self.score = 0 # Changed to a normal int because StringVar became unnecessary when we wanted to update the scoreLabel
        if Paddle.NUM_PADDLE == 0: # Create the human paddle
            self.id = canvas.create_rectangle(WIDTH/26, HEIGHT/2 - PADDLEHEIGHT/2, WIDTH/26 + PADDLEWIDTH, HEIGHT/2 + PADDLEHEIGHT/2, fill="white")
            self.scoreLabel = canvas.create_text(WIDTH/4, HEIGHT/20, text=self.score, fill="white", font="Helvetica 30 bold") # Changed Label to just text placed onto the canvas
            window.bind("<KeyPress-Down>", self.moveDown)
            window.bind("<KeyPress-Up>", self.moveUp)
            Paddle.NUM_PADDLE += 1
        else: # Create the bot paddle
            self.scoreLabel = canvas.create_text(WIDTH*3/4, HEIGHT/20, text=self.score, fill="white", font="Helvetica 30 bold") # Changed Label to just text placed onto the canvas
            self.id = canvas.create_rectangle(WIDTH*25/26 - PADDLEWIDTH, HEIGHT/2 - PADDLEHEIGHT/2, WIDTH*25/26, HEIGHT/2 + PADDLEHEIGHT/2, fill="white")
            self.bot = True

    def increaseScore(self):
        # Increase score variable
        self.score += 1
        # Change text on canvas to updated value
        canvas.itemconfig(self.scoreLabel, text=self.score)

    def moveDown(self,key):
        if self.bot:
            self.y = BOTSPEED
        else:
            self.y = SPEED

    def moveUp(self,key):
        if self.bot:
            self.y = -BOTSPEED
        else:
            self.y = -SPEED

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
PADDLEWIDTH = 20
PADDLEHEIGHT = 50
BALLSIZE = 20
BALLSPEED = 3
SPEED = 3.5
BOTSPEED = 2.5
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
