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


# Make a house function that can make any size, colors
def drawHouse(size, baseColor, roofColor, doorColor):
    drawSquare(size, baseColor)
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTriangle(size, roofColor)
    drawDoor(size, doorColor)

drawHouse(300, "crimson", "teal", "saddle brown")















turtle.done()
