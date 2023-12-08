# housePrinter.py
import turtle
pen = turtle.Turtle()

# Define a function called drawSquare
def drawSquare(size, color): # parameter, size == 50
    pen.speed(0)
    pen.color(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(size) # function AKA a command or action.
        pen.left(90)
    pen.end_fill()

def drawTriangle(size, color): # tell this function to expect a size parameter
    pen.color(color)
    pen.begin_fill()
    for i in range(3): # Make the triangle the correct size
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawDoor(size, color):
    pen.up()
    pen.goto(size/3, 0)
    pen.down()
    pen.color(color)
    # Draw the door
    pen.begin_fill()
    pen.left(90)
    pen.forward(size/3)
    pen.right(90)
    pen.forward(size/3)
    pen.right(90)
    pen.forward(size/3)
    pen.end_fill()

def drawWindows(size, color):
    pen.up()
    pen.color(color)
    pen.goto(size/4, size * 0.75) # Go up by 75% of size
    pen.down()
    # Draw left window
    for i in range(4):
        # Makes a single pane of the window
        for j in range(4): # Draw Square
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)
    # Get to the right window
    pen.up()
    pen.goto(size*3/4, size * 0.75)
    pen.down()

    # Draw the right window
    for i in range(4):
        # Makes a single pane of the window
        for j in range(4): # Draw Square
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)

# make a drawHouse function that does the commands below:
def drawHouse(size, baseColor, roofColor, doorColor):
    drawSquare(size, baseColor)
    pen.goto(0, size)
    drawTriangle(size, roofColor)
    drawDoor(size, doorColor)
    drawWindows(size, "black")# Function call (activate the function)

#        size, basecolor, roofclr, doorColor
drawHouse(200, "crimson", "teal", "saddle brown")

turtle.done()
