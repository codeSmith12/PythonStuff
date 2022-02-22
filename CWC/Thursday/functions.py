# functions.py
import turtle
pen = turtle.Turtle()

# Define a function called drawSquare
def drawSquare(size): # parameter, size == 50
    for i in range(4):
        pen.forward(size) # function AKA a command or action.
        pen.left(90)

def drawTriangle(size): # tell this function to expect a size parameter
    for i in range(3): # Make the triangle the correct size
        pen.forward(size)
        pen.left(120)

pen.speed(0) # fastest speed
pen.color("cyan")
for i in range(36):
    drawSquare(100)
    pen.left(10)
    drawTriangle(50)



















turtle.done()
