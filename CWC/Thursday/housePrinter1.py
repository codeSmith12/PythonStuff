import turtle
pen = turtle.Turtle()
pen.speed(0)


def drawBase():
    pen.color("navy")
    pen.begin_fill()
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    pen.end_fill()

def drawRoof():
    pen.color("brown")
    pen.begin_fill()
    for i in range(3):
        pen.forward(100)
        pen.left(120)
    pen.end_fill()

# THIS CODE DRAWS THE WHOLE HOUSE
def drawHouse():
    drawBase()
    # Get to the top of the roof
    pen.left(90)
    pen.forward(100)
    pen.right(90)

    
    # Make a for loop that draws a triangle.
    drawRoof()

drawHouse()

turtle.done()