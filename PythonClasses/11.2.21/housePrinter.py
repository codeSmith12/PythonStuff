# HousePrinter
import turtle
pen = turtle.Turtle() # Constructor


# Find the degrees to turn by for a triangle....

# what is a funtion? : Certain lines of code that we put in a list.
                    # call the function and it does those things!
# Function that draws a square
def drawSquare(size): # Size is a parameter
    pen.color("crimson")
    pen.begin_fill()
    # Create a square
    for i in range(0,4):
        pen.forward(size) # Chance this value
        pen.left(90) # Keep this value
    pen.end_fill()

def drawTri(size): # Size is a parameter
    # Create a triangle
    pen.color("cyan")
    pen.begin_fill()
    for i in range(0,3):
        pen.forward(size) # Chance this value
        pen.left(120) # Keep this value
    pen.end_fill()
def drawDoor(size):
    pen.up()
    pen.goto(size/3, 0)
    pen.down()
    pen.left(90)


# Creating a triange function that can make a triangle of any size..
# EXTRA CREDIT create a house function
def housePrinter(size): # parameter
    drawSquare(size) # size 100
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTri(size) # size 100
    drawDoor(size)


housePrinter(100) # argument
turtle.done()
