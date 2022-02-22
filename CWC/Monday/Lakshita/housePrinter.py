import turtle
pen = turtle.Turtle()

# Draw a square
def drawSquare(color, size):
    pen.color(color)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        pen.fd(size) # Forward decides the size of the SIDES of the house
        pen.lt(90)
    pen.end_fill()
    pen.up()

# Draw Triangle
def drawTriangle(color, size): # definition =  arguments
    pen.color(color)
    pen.down()
    pen.begin_fill()
    for i in range(3):
        pen.fd(size)
        pen.lt(120)
    pen.end_fill()
    pen.up()

def drawBase(size):
    drawSquare("cyan", size) # parameter (Information given to a function, so it can do its job)
    # Get to the top of the square
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTriangle("crimson", size) # parameters - function call
    pen.left(90)
    drawDoor(size/3)


def drawDoor(size): # size = previous size /3
    pen.goto(size, 0)
    pen.down()
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.right(90)
    pen.end_fill()
    pen.up()
    # Draw the rest of the door

def drawWindows(size):
    pen.goto(size/4, size*3/4)


drawBase(150)
drawWindows(150)





turtle.done()
