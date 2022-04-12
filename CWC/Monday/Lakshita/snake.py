from tkinter import *
import time
from random import randint


class Apple:
    def __init__(self):
        self.x = randint(0, WIDTH - HEADSIZE)
        self.y = randint(0, HEIGHT - HEADSIZE)
        self.x = self.x - self.x % HEADSIZE
        self.y = self.y - self.y % HEADSIZE
        self.id = canvas.create_oval(self.x, self.y, self.x + HEADSIZE, self.y+HEADSIZE, fill="red")
        self.checkIfTouching()

    def respawnApple(self):
        self.x = randint(0, WIDTH - HEADSIZE)
        self.y = randint(0, HEIGHT - HEADSIZE)
        self.x = self.x - self.x % HEADSIZE
        self.y = self.y - self.y % HEADSIZE
        canvas.moveto(self.id, self.x, self.y)


    def checkIfTouching(self):
        pos = canvas.coords(self.id) # Get the position of the apple
        overLapping = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])

        # if the snake is in the apples coordinate
        if 1 in overLapping:
            self.respawnApple()



class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        # Controls a players movement...
        self.movementLocked = False
        self.head = canvas.create_oval(WIDTH//2, HEIGHT//2, WIDTH//2+HEADSIZE, HEIGHT//2+HEADSIZE, fill="ivory3")
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def moveUp(self, key):
        if self.y != SPEED and not self.movementLocked:
            self.x = 0
            self.y = -SPEED
            self.movementLocked = True

    def moveDown(self, key):
        if self.y != -SPEED and not self.movementLocked:
            self.x = 0
            self.y = SPEED
            self.movementLocked = True

    def moveLeft(self, key):
        if self.x != SPEED and not self.movementLocked:
            self.y = 0
            self.x = -SPEED
            self.movementLocked = True

    def moveRight(self, key):
        if self.x != -SPEED and not self.movementLocked:
            self.y = 0
            self.x = SPEED
            self.movementLocked = True

    def updatePosition(self):
        global gameOver
        canvas.move(self.head, self.x, self.y)
        # Unlock players ability to choose new direction
        self.movementLocked = False
        pos = canvas.coords(self.head)
        # pos = [x1,y1,x2,y2]
        if pos[2] > WIDTH:
            gameOver = True
        if pos[0] < 0:
            gameOver = True
        if pos[1] < 0:
            gameOver = True
        if pos[3] > HEIGHT:
            gameOver = True



def drawGrid():
    COLS = WIDTH // HEADSIZE
    colSize = WIDTH // COLS
    ROWS = HEIGHT // HEADSIZE
    rowSize = HEIGHT // ROWS

    # Draw columns
    for i in range(COLS):
        canvas.create_line(colSize*i, 0, colSize*i, HEIGHT, fill="ivory3")
    # Draw rows
    for i in range(ROWS):
        canvas.create_line(0, rowSize*i, WIDTH, rowSize*i, fill="ivory3")


# GAME CONSTANTS
WIDTH = 800
HEIGHT = 800
HEADSIZE = 25
SPEED = HEADSIZE
TICK = 0.15


assert WIDTH % HEADSIZE == 0, "WIDTH does not divide evenly by HEADSIZE."
assert HEIGHT % HEADSIZE == 0, "HEIGHT does not divide evenly by HEADSIZE."



tk = Tk()
tk.title("Snake")
tk.configure(width=WIDTH, height=HEIGHT)

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = Snake()
drawGrid()
apple = Apple()

global gameOver
gameOver = False

while not gameOver:
    tk.update() # keeps the window open
    snake.updatePosition() # Makes the snake move
    apple.checkIfTouching()
    time.sleep(TICK)
