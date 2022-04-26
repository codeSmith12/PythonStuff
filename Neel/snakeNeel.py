from tkinter import *
from random import randint
import time

class Rat:
    def __init__(self):
        self.x = randint(0, WIDTH - MOUSESIZE)
        self.y = randint(0, HEIGHT - MOUSESIZE)
        self.x = self.x - (self.x % HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        # Create hit box that is at the center of the rats cell
        self.hitBox = canvas.create_rectangle(self.x + MOUSESIZE/2, self.y+MOUSESIZE/2, self.x + MOUSESIZE/2, self.y + MOUSESIZE/2, fill = "black")
        self.rat = canvas.create_rectangle(self.x, self.y, self.x + MOUSESIZE, self.y + MOUSESIZE, fill = MOUSECOLOR)
    def respawn(self):
        self.x = randint(0, WIDTH - MOUSESIZE)
        self.y = randint(0, HEIGHT - MOUSESIZE)
        self.x = self.x - (self.x % HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        canvas.moveto(self.hitBox, self.x+MOUSESIZE/2, self.y+MOUSESIZE/2)
        canvas.moveto(self.rat, self.x, self.y)
        # If the mouse spawns on the snake, move to new location
        pos = canvas.coords(self.hitBox)
        overlap = canvas.find_enclosed(pos[0], pos[1], pos[2], pos[3])
        if len(overlap) > 1:
            self.respawn()

    def checkIfTouching(self,snakeTag):
        pos = canvas.coords(self.hitBox)
        snakePos = canvas.coords(snakeTag)
        overlap = canvas.find_overlapping(pos[0], pos[1], pos[2], pos[3])
        if 1 in overlap:
            self.respawn()
            snakeTag.eatMouse()


class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.directionLocked = False
        self.bodyCount = 0
        self.bodyParts = []
        self.hitBoxes = []
        self.prevPos = []
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill = SNAKECOLOR)
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Right>", self.moveRight)
        tk.bind("<KeyPress-Left>", self.moveLeft)

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)
        self.prevPos.insert(0,pos)
        if len(self.prevPos) > self.bodyCount+1:
            del self.prevPos[-1]
        # Move the head to the next cell...
        canvas.move(self.head, self.x, self.y)
        # Move each body part from the beginning to the end.
        for i in range(len(self.bodyParts)):
            canvas.moveto(self.hitBoxes[i], self.prevPos[i][0]+HEADSIZE//2, self.prevPos[i][1]+HEADSIZE//2)
            canvas.moveto(self.bodyParts[i], self.prevPos[i][0], self.prevPos[i][1])
        # End the game if the snake has eaten its tail
        if len(canvas.find_enclosed(pos[0],pos[1],pos[2],pos[3])) > 1:
            gameOver = True

        self.directionLocked = False
        if pos[2] > WIDTH:
            gameOver = True
        if pos[3] > HEIGHT:
            gameOver = True
        if pos[0] < 0:
            gameOver = True
        if pos[1] < 0:
            gameOver = True


    def eatMouse(self):
        hitBox = canvas.create_oval(self.prevPos[-1][0] + HEADSIZE//2, self.prevPos[-1][1] + HEADSIZE//2, self.prevPos[-1][0] + HEADSIZE//2, self.prevPos[-1][1] + HEADSIZE//2, fill="ivory3")
        bodyPart = canvas.create_oval(self.prevPos[-1][0], self.prevPos[-1][1], self.prevPos[-1][0] + HEADSIZE, self.prevPos[-1][1] + HEADSIZE, fill="ivory3")
        self.bodyParts.append(bodyPart)
        self.hitBoxes.append(hitBox)
        self.bodyCount += 1

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

    def checkIfTouchingBody(self):
        pass


def drawGrid():
    cellWidth = WIDTH // COLS
    cellHeight = HEIGHT // ROWS
    for i in range(ROWS):
        canvas.create_line(0, i*cellHeight, WIDTH, i*cellHeight, fill="ivory3")
    for i in range(COLS):
        canvas.create_line(i*cellWidth, 0, i*cellWidth, HEIGHT, fill="ivory3")


tk = Tk()
WIDTH=800
HEIGHT=800
HEADSIZE = 20
MOUSESIZE = HEADSIZE
SNAKECOLOR = "ivory3"
GRIDCOLOR = SNAKECOLOR
BACKGROUNDCOLOR = "black"
MOUSECOLOR = "grey"


assert WIDTH % HEADSIZE == 0,  "WIGHT does not divide evenly by Headsize"
assert HEIGHT % HEADSIZE == 0, "HEIGHT does not divide evenly by Headsize"

ROWS = HEIGHT//HEADSIZE
COLS = WIDTH//HEADSIZE

SPEED = HEADSIZE
TICK = 0.1

tk.configure(bg="lime")

tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg=BACKGROUNDCOLOR)
canvas.pack()

scoreLabel = Label(canvas, text="test")
scoreLabel.pack()



# drawGrid()
global gameOver

gameOver = False

snake = Snake()
rat = Rat()

while not gameOver:
    snake.updatePosition()
    rat.checkIfTouching(snake)
    tk.update()
    time.sleep(TICK)
