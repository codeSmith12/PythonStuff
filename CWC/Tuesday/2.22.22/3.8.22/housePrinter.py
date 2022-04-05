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
    pen.color(color)
    pen.up()
    pen.goto(size/3, 0)
    pen.left(90)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size/3)
        pen.right(90)
    pen.end_fill()
# DEFINE WHAT WE MEAN WHEN WE SAY DRAWWINDOWS
def drawWindows(size, color): # colon
    pen.color(color)
    pen.up()
    pen.goto(size/4, size*3/4)
    pen.down()

    # Repeat for each pane
    for j in range(4):
        # Draw a single pane
        for i in range(4):
            pen.forward(size/8)
            pen.right(90)
        pen.right(90)





# Make the house function take in a size , base color and roof color
def drawHouse(size, baseColor, roofColor, doorColor, windowColor):
    drawSquare(size, baseColor) # Calling the function
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    drawTriangle(size, roofColor) # Calling the function
    drawDoor(size, doorColor)
    drawWindows(size, windowColor)
# Make sure to give the information to the function
drawHouse(200, "crimson", "teal", "saddle brown", "black")










turtle.done()
