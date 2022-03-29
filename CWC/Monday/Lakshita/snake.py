from tkinter import *
import time

class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.head = canvas.create_oval(WIDTH//2, HEIGHT//2, WIDTH//2+HEADSIZE, HEIGHT//2+HEADSIZE, fill="ivory3")
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
    def moveUp(self, key):
        self.x = 0
        self.y = -SPEED
    def moveDown(self, key):
        self.x = 0
        self.y = SPEED

    def updatePosition(self):
        canvas.move(self.head, self.x, self.y)


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

drawGrid()

snake = Snake()

gameOver = False

while not gameOver:
    tk.update() # keeps the window open
    snake.updatePosition() # Makes the snake move
    time.sleep(TICK)
