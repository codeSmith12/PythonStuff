from tkinter import *
from random import randint
import time
# ADD MOUSE CLASS
# Making a mouse class to randomly place a mouse on the map in a grid position
class Mouse:
    def __init__(self):
        self.x = randint(0, WIDTH - MOUSESIZE)
        # Next time -> Get Random Y value in range



class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.directionLocked = False # Allows for cooldown between moves, stops us from being able to change directions multiple times between TICKs
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill = "red")
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Right>", self.moveRight)
        tk.bind("<KeyPress-Left>", self.moveLeft)

    def updatePosition(self):
        global gameOver
        canvas.move(self.head, self.x, self.y)
        self.directionLocked = False
        pos = canvas.coords(self.head)

        # x1,y1,x2,y2
        if pos[2] > WIDTH:
            gameOver = True
        if pos[3] > HEIGHT:
            gameOver = True
        if pos[0] < 0:
            gameOver = True
        if pos[1] < 0:
            gameOver = True


    def moveUp(self,evnt):
        if self.y != SPEED and not self.directionLocked:
            self.x = 0
            self.y = -SPEED
            self.directionLocked = True
    def moveDown(self,evnt):
        if self.y != -SPEED and not self.directionLocked:
            self.x = 0
            self.y = SPEED
            self.directionLocked = True
    def moveRight(self,evnt):
        if self.x != -SPEED and not self.directionLocked:
            self.y = 0
            self.x = SPEED
            self.directionLocked = True
    def moveLeft(self,evnt):
        if self.x != SPEED and not self.directionLocked:
            self.y = 0
            self.x = -SPEED
            self.directionLocked = True

tk = Tk()
WIDTH=800
HEIGHT=800
HEADSIZE = 25
MOUSESIZE = HEADSIZE
# Make sure dimensions of the map vs the snake size is acceptable
assert WIDTH % HEADSIZE == 0, "Width does not divide evenly by Headsize of snake"
assert HEIGHT % HEADSIZE == 0, "Height does not divide evenly by Headsize of snake"

SPEED = HEADSIZE
TICK = 0.15

tk.configure(bg="lime")

tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="lime")
canvas.pack()

global gameOver

gameOver = False

snake = Snake()

while not gameOver:
    snake.updatePosition()
    tk.update()
    time.sleep(TICK)
