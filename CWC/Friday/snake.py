# snake.py
import tkinter, time
from random import randint

class Mouse:
    def __init__(self):
        self.x = randint(0, WIDTH)
        self.y = randint(0, HEIGHT)     # x1,y1,x2,y2, color
        self.id = canvas.create_rectangle(self.x, self.y,self.x, self.y)

class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0                  # x1,y1, x2,y2
        self.movementLocked = False
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white", tags=('snake'))
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

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
        canvas.move(self.head, self.x, self.y)
        # After move, we may change directions again
        self.movementLocked = False

        pos = canvas.coords(self.head)
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
TICK = 0.15
ROWS = HEIGHT//HEADSIZE # Division with rounding to nearest integer
COLS = WIDTH//HEADSIZE

# Set the size of the window
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT)
# Change the background color to black
canvas.configure(bg="black")
canvas.pack()

drawGrid()
snake = Snake()

global gameOver # Variable that can be accessed from anywhere...
gameOver = False

# Keeps window open
while not gameOver:
    snake.updatePosition() # Moves snake
    tk.update() # Keeps window open
    time.sleep(TICK)
