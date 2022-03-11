import turtle
pen = turtle.Turtle() # Pulls pen out of toolbox

# Draws a square of any size
def drawSquare(size, color): # parameter
    pen.color(color) # String, word or string of characters
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

def drawTriangle(size, color): # parameter
    pen.color(color) # String, word or string of characters
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120) # 360 / 3 = 120 || 360 / # sides = Degrees to turn
    pen.end_fill()

def drawDoor(size, color):
    pen.up()
    pen.goto(size/3, 0)
    pen.left(90)
    pen.color(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size/3)
        pen.right(90)
    pen.end_fill()

def drawWindows(size):
    # Get to left window
    pen.goto(size/4, size*3/4)
    pen.color("black")
    pen.down()
    # Draw left window
    for i in range(4):
        for j in range(4): # Draws a single pane
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)

    # Get to right window
    pen.up()
    pen.goto(size*3/4, size*3/4)
    pen.down()

    # Draw right window
    for i in range(4):
        for j in range(4): # Draws a single pane
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)

# Make a house function that can make any size, colors
def drawHouse(size, baseColor, roofColor, doorColor):
    drawSquare(size, baseColor)
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTriangle(size, roofColor)
    drawDoor(size, doorColor)
    drawWindows(size)

drawHouse(200, "crimson", "teal", "saddle brown")















turtle.done()
