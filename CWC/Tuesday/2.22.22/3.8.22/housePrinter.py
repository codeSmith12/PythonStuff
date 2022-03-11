import turtle
pen = turtle.Turtle() # Creates a pen object and stores it in a variable

# for loop
def drawSquare(size, color): # Function
    pen.color(color) # String
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

def drawTriangle(size, color): # Function
    pen.color(color) # String
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawHouse():
    drawSquare(100, "crimson") # Calling the function
    pen.left(90)
    pen.forward(100)
    pen.right(90)
    drawTriangle(100, "teal") # Calling the function

drawHouse()










turtle.done()
