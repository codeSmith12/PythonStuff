# snake.py
import tkinter, time

class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0                  # x1,y1, x2,y2
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white", tags=('snake'))
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def moveUp(self, event):
        if self.y != SPEED:
            self.x = 0
            self.y = -SPEED

    def moveDown(self, event):
        if self.y != -SPEED:
            self.x = 0
            self.y = SPEED

    def moveRight(self, event):
        if self.x != -SPEED:
            self.x = SPEED
            self.y = 0

    def moveLeft(self, event):
        if self.x != SPEED:
            self.x = -SPEED
            self.y = 0

    def updatePosition(self):
        canvas.move(self.head, self.x, self.y)
        pos = canvas.coords(self.head)
        print(pos)



# Functions
def drawGrid(): # 20
    CELL_WIDTH = WIDTH // HEADSIZE
    CELL_HEIGHT = HEIGHT // HEADSIZE
    # Create horizontal lines
    for i in range(CELL_HEIGHT):
        canvas.create_line(0, CELL_HEIGHT*i, WIDTH, CELL_HEIGHT*i, fill="ivory3")
    # Create vertical lines
    for i in range(CELL_WIDTH):
        canvas.create_line(CELL_WIDTH*i, 0, CELL_WIDTH*i, HEIGHT, fill="ivory3")


tk = tkinter.Tk()
tk.title("Snake")
# Constants
WIDTH = 800
HEIGHT = 800
HEADSIZE = 25
SPEED = HEADSIZE
TICK = 0.15

# Set the size of the window
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT)
# Change the background color to black
canvas.configure(bg="black")
canvas.pack()

drawGrid()
snake = Snake()

# Keeps window open
while True:
    snake.updatePosition() # Moves snake
    tk.update() # Keeps window open
    time.sleep(TICK)
