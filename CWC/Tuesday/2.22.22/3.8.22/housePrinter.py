import turtle
pen = turtle.Turtle() # Creates a pen object and stores it in a variable

pen.speed(0)

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

def drawDoor(size, color):
         #  (x,y)
    pen.goto(size/3, 0)


# Make the house function take in a size , base color and roof color
def drawHouse(size, baseColor, roofColor):
    drawSquare(size, baseColor) # Calling the function
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTriangle(size, roofColor) # Calling the function
    drawDoor(size, "saddle brown")
# Make sure to give the information to the function
drawHouse(200, "crimson", "teal")










turtle.done()
