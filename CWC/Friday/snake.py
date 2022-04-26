# snake.py
import tkinter, time
from random import randint

class Mouse:
    def __init__(self):
        self.x = randint(0, WIDTH-MOUSESIZE)
        self.y = randint(0, HEIGHT-MOUSESIZE)     # x1,y1,x2,y2, color
        self.x = self.x - (self.x % HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        self.hitBox = canvas.create_rectangle(self.x + MOUSESIZE/2, self.y + MOUSESIZE/2, self.x + MOUSESIZE/2, self.y + MOUSESIZE/2, fill="white")
        self.id = canvas.create_rectangle(self.x, self.y, self.x + MOUSESIZE, self.y + MOUSESIZE, fill="white")

    def respawnMouse(self):
        self.x = randint(0, WIDTH-MOUSESIZE)
        self.y = randint(0, HEIGHT-MOUSESIZE)     # x1,y1,x2,y2, color
        self.x = self.x - (self.x % HEADSIZE)
        self.y = self.y - (self.y % HEADSIZE)
        canvas.moveto(self.hitBox, self.x + MOUSESIZE/2, self.y+MOUSESIZE/2)
        canvas.moveto(self.id, self.x, self.y)

    def checkIfTouching(self, snake):
        pos = canvas.coords(self.hitBox)
        # A list of every canvas object that overlaps with the mouse
        overlap = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
        if 1 in overlap:
            self.respawnMouse()
            snake.eatMouse()

class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0                  # x1,y1, x2,y2
        self.movementLocked = False
        self.bodyParts = []
        self.prevPos = []
        self.bodyCount = 0
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white", tags=('snake'))
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def eatMouse(self):
        pos = canvas.coords(self.head)
        bodyPart = canvas.create_rectangle(pos[0], pos[1], pos[2], pos[3], fill="ivory3")
        self.bodyParts.append(bodyPart)
        self.bodyCount += 1


    def moveUp(self, event):
        if self.y != SPEED and not self.movementLocked:
            self.x = 0
            self.y = -SPEED
            self.movementLocked = True

    def moveDown(self, event):
        if self.y != -SPEED and not self.movementLocked:
            self.x = 0
            self.y = SPEED
            self.movementLocked = True

    def moveRight(self, event):
        if self.x != -SPEED and not self.movementLocked:
            self.x = SPEED
            self.y = 0
            self.movementLocked = True

    def moveLeft(self, event):
        if self.x != SPEED and not self.movementLocked:
            self.x = -SPEED
            self.y = 0
            self.movementLocked = True

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)
        self.prevPos.insert(0, pos)

        if len(self.prevPos) > self.bodyCount+1:
            del self.prevPos[-1] # Removes the last item in a list
        for i in range(len(self.bodyParts)):
            canvas.moveto(self.bodyParts[i], self.prevPos[i][0], self.prevPos[i][1])

        canvas.move(self.head, self.x, self.y)

        # After move, we may change directions again
        self.movementLocked = False


        # Check if out of bounds
        if pos[2] > WIDTH:
            gameOver = True
        if pos[3] > HEIGHT:
            gameOver = True
        if pos[0] < 0:
            gameOver = True
        if pos[1] < 0:
            gameOver = True

# Functions
def drawGrid(): # 20
    CELL_WIDTH = WIDTH // COLS
    CELL_HEIGHT = HEIGHT // ROWS
    # Create horizontal lines
    for i in range(ROWS):
        canvas.create_line(0, CELL_HEIGHT*i, WIDTH, CELL_HEIGHT*i, fill="ivory3")
    # Create vertical lines
    for i in range(COLS):
        canvas.create_line(CELL_WIDTH*i, 0, CELL_WIDTH*i, HEIGHT, fill="ivory3")

tk = tkinter.Tk()
tk.title("Snake")
# Constants
WIDTH = 800
HEIGHT = 800
HEADSIZE = 25
SPEED = HEADSIZE
MOUSESIZE = HEADSIZE
TICK = 0.15
ROWS = HEIGHT//HEADSIZE # Division with rounding to nearest integer
COLS = WIDTH//HEADSIZE

# Set the size of the window
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT)
# Change the background color to black
canvas.configure(bg="black")
canvas.pack()

# Create the snake first so it's id is 1, easier for checking if touching mouse.
snake = Snake()
drawGrid()
mouse = Mouse()

global gameOver # Variable that can be accessed from anywhere...
gameOver = False

# Keeps window open
while not gameOver:
    snake.updatePosition() # Moves snake
    mouse.checkIfTouching(snake)
    tk.update() # Keeps window open
    time.sleep(TICK)
