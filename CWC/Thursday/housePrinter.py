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
    pen.color(color) # " " <--- quotation marks
    pen.begin_fill() # () <---- Parethesis
    for i in range(3): # Make the triangle the correct size
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawDoor(size, color):
    print("Draw Door....")

# make a drawHouse function that does the commands below:
def drawHouse(size, baseColor, roofColor, doorColor):
    drawSquare(size, baseColor)
    pen.goto(0, size)
    drawTriangle(size, roofColor)
    drawDoor(size, doorColor)
drawHouse(200, "orange", "green", "brown")








turtle.done()
