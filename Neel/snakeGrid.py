from tkinter import *
from random import randint
import time

class Mouse:
    def __init__(self):
        self.x = randint((MOUSESIZE + MOUSE_SPAWN_BORDER), (WIDTH-MOUSE_SPAWN_BORDER))
        self.x = self.x - (self.x % HEADSIZE)
        self.y = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, HEIGHT-MOUSE_SPAWN_BORDER)
        self.y = self.y - (self.y % HEADSIZE)
        self.hitBox = canvas.create_rectangle(self.x+MOUSESIZE/2, self.y+MOUSESIZE/2, self.x + MOUSESIZE/2, self.y + MOUSESIZE/2, fill="black" )
        self.id = canvas.create_rectangle(self.x, self.y, self.x + MOUSESIZE, self.y + MOUSESIZE, fill="grey" )
    def respawnMouse(self):
        self.x = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, WIDTH-MOUSE_SPAWN_BORDER)
        self.x = self.x - (self.x % HEADSIZE)
        self.y = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, HEIGHT-MOUSE_SPAWN_BORDER)
        self.y = self.y - (self.y % HEADSIZE)
        canvas.moveto(self.hitBox, self.x+MOUSESIZE/2, self.y+MOUSESIZE/2)
        canvas.moveto(self.id, self.x, self.y)


    # Fix the parameters ...
    def checkIfTouching(self, snakeTag):
        pos = canvas.coords(self.hitBox)
        snakePos = canvas.coords(snakeTag)
        # print(pos, snakePos)
        # tag = canvas.gettags(snake)
        overlap = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
        if 1 in overlap:
            self.respawnMouse()
            snake.eatMouse()



# May also need hitbox for snake, appears to exit game too early and too late sometimes..
class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.bodyCount = 0
        self.bodyParts = []
        self.hitBoxes = []
        self.prevPos = []
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white", tags=('snake'))
        self.tail = self.head
        self.movementLocked = False
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)
        # self.prevPos = []
        self.prevPos.insert(0, pos)
        if len(self.prevPos) > self.bodyCount+1:
            del self.prevPos[-1]
        canvas.move(self.head, self.x, self.y)
        for i in range(len(self.bodyParts)):
                canvas.moveto(self.hitBoxes[i], self.prevPos[i][0]+HEADSIZE//2, self.prevPos[i][1]+HEADSIZE//2)
                canvas.moveto(self.bodyParts[i], self.prevPos[i][0], self.prevPos[i][1])

        # If a body hitbox is enclosed within the head, GG
        if len(canvas.find_enclosed(pos[0],pos[1],pos[2],pos[3])) > 1:
            gameOver = True

        self.movementLocked = False
        if pos[0] < 0:
            gameOver = True
        elif pos[1] < 0:
            gameOver = True
        elif pos[2] >= WIDTH:
            gameOver = True
        elif pos[3] >= HEIGHT:
            gameOver = True

    def moveUp(self,key):
        if self.y != SPEED and not self.movementLocked:
            self.y = -SPEED
            self.x = 0
            self.movementLocked = True
    def moveDown(self,key):
        if self.y != -SPEED and not self.movementLocked:
            self.y = SPEED
            self.x = 0
            self.movementLocked = True

    def moveLeft(self,key):
        if self.x != SPEED and not self.movementLocked:
            self.x = -SPEED
            self.y = 0
            self.movementLocked = True

    def moveRight(self,key):
        if self.x != -SPEED and not self.movementLocked:
            self.x = SPEED
            self.y = 0
            self.movementLocked = True

    def getPos(self):
        return canvas.coords(self.head)
    def getSelf(self):
        return self.head
    def eatMouse(self):
        pos = canvas.coords(self.head)
        hitBox = canvas.create_rectangle(self.prevPos[-1][0]+HEADSIZE//2, self.prevPos[-1][1]+HEADSIZE//2, self.prevPos[-1][0]+HEADSIZE//2, self.prevPos[-1][1]+HEADSIZE//2, fill="black")
        part = canvas.create_rectangle(self.prevPos[-1][0], self.prevPos[-1][1], self.prevPos[-1][2], self.prevPos[-1][3], fill="white")
        self.hitBoxes.append(hitBox)
        self.bodyParts.append(part)
        self.bodyCount += 1
        self.tail = part

def drawGrid():
    cellWidth = WIDTH // COLS
    cellHeight = HEIGHT // ROWS
    for i in range(ROWS):
        canvas.create_line(0, i*cellHeight, WIDTH, i*cellHeight, fill="ivory3")
    for i in range(COLS):
        canvas.create_line(i*cellWidth, 0, i*cellWidth, HEIGHT, fill="ivory3")

tk = Tk()
tk.title("Snake")
WIDTH=800
HEIGHT=800
HEADSIZE=25
assert WIDTH % HEADSIZE == 0, "Width does not divide evenly by Headsize of snake"
assert HEIGHT % HEADSIZE == 0, "Height does not divide evenly by Headsize of snake"
ROWS = HEIGHT//HEADSIZE
COLS = WIDTH//HEADSIZE

TAILSIZE=18
MOUSESIZE=HEADSIZE
MOUSE_SPAWN_BORDER = 40
SPEED = HEADSIZE
TICK = 0.15

tk.geometry(f"{WIDTH}x{HEIGHT}")
tk.configure(bg="black")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = Snake()
drawGrid()


global gameOver
gameOver = False
mouse=Mouse()
# Game Loop - updates the window with newly moved objects
while not gameOver:
    snake.updatePosition()
    mouse.checkIfTouching(snake.getSelf())
    tk.update()
    time.sleep(TICK)
