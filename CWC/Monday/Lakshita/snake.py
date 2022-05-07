from tkinter import *
import time
from random import randint


"""
BRAINSTORM OF WHAT TO DO AFTER SNAKE


"""





class Apple:
    def __init__(self):
        self.x = randint(0, WIDTH - HEADSIZE)
        self.y = randint(0, HEIGHT - HEADSIZE)
        self.x = self.x - self.x % HEADSIZE
        self.y = self.y - self.y % HEADSIZE
        self.hitBox = canvas.create_oval(self.x+HEADSIZE//2, self.y+HEADSIZE//2, self.x + HEADSIZE//2, self.y+HEADSIZE//2, fill="red")
        self.id = canvas.create_oval(self.x, self.y, self.x + HEADSIZE, self.y+HEADSIZE, fill="red")

    def respawnApple(self):
        self.x = randint(0, WIDTH - HEADSIZE)
        self.y = randint(0, HEIGHT - HEADSIZE)
        self.x = self.x - self.x % HEADSIZE
        self.y = self.y - self.y % HEADSIZE
        canvas.moveto(self.hitBox, self.x+HEADSIZE//2, self.y+HEADSIZE//2)
        canvas.moveto(self.id, self.x, self.y)

    def checkIfTouching(self, snake):
        pos = canvas.coords(self.hitBox) # Get the position of the apple
        overLapping = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])

        # if the snake is in the apples coordinate
        if 1 in overLapping:
            self.respawnApple()
            snake.eatApple()


class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        # Controls a players movement...
        self.movementLocked = False
        self.head = canvas.create_oval(WIDTH//2, HEIGHT//2, WIDTH//2+HEADSIZE, HEIGHT//2+HEADSIZE, fill="ivory3")
        self.bodyParts = []
        self.hitBoxes = []
        self.prevPos = []
        self.bodyCount = 0

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

    def eatApple(self):
        pos = canvas.coords(self.head)
        hitBox = canvas.create_oval(pos[0]+HEADSIZE//2,pos[1]+HEADSIZE//2, pos[0] + HEADSIZE//2,pos[1]+HEADSIZE//2, fill="ivory3")
        bodyPart = canvas.create_oval(pos[0],pos[1],pos[2],pos[3], fill="ivory3")
        self.bodyParts.append(bodyPart) # adds the new part to the list
        self.hitBoxes.append(hitBox) # adds the new part to the list
        self.bodyCount += 1

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)# <----
        self.prevPos.insert(0, pos)
        # if the list of prevPos extends past bodycount + head,
        if len(self.prevPos) > self.bodyCount + 1:
            del self.prevPos[-1] # Delete the last entry in the list
        # Remove old prevPos next time <-----
        canvas.move(self.head, self.x, self.y)

        for i in range(len(self.bodyParts)):
            canvas.moveto(self.hitBoxes[i], self.prevPos[i][0]+HEADSIZE//2, self.prevPos[i][1]+HEADSIZE//2)
            canvas.moveto(self.bodyParts[i], self.prevPos[i][0], self.prevPos[i][1])

        # Unlock players ability to choose new direction
        self.movementLocked = False
        pos = canvas.coords(self.head)

        # Perhaps check if head is overlapping a hitbox of the body
        if len(canvas.find_enclosed(pos[0],pos[1],pos[2],pos[3])) > 1:
            gameOver = True

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

scoreText = canvas.create_text(WIDTH//2 - HEADSIZE//2, HEADSIZE//2, text=0, font=("Helvetica",14,"bold"), fill="white")

global gameOver
gameOver = False

while not gameOver:
    tk.update() # keeps the window open
    snake.updatePosition() # Makes the snake move
    apple.checkIfTouching(snake)
    time.sleep(TICK)
