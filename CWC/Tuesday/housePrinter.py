#housePrinter.py

# By suggestion, we will turn this into a village project

import turtle, random
pen = turtle.Turtle()

# Pen settings
pen.speed(0)

# Make a moon ????

def drawStars(num): # num == number
    pen.color("goldenrod")
    for i in range(num):
        x = random.randint(-600, 600)
        y = random.randint(-50, 550)
        pen.goto(x,y)
        pen.dot(random.randint(1, 6))
    # Draw moon
    pen.goto(515, 320)
    pen.color("lemon chiffon")
    pen.begin_fill()
    pen.circle(100)
    pen.end_fill()

def drawScene():
    # Set background to black (because replit has troubles)
    pen.pensize(10000)
    pen.color("black")
    pen.forward(1)
    pen.pensize(1)
    # Draw grass
    pen.up()
    pen.color("green")
    pen.goto(-650,-100)
    pen.begin_fill()
    pen.goto(650,-100)
    pen.goto(650,-550)
    pen.goto(-650,-550)
    pen.end_fill()

    # Draw stars
    drawStars(200)

drawScene()



def drawSquare(size, color):
    pen.color(color)
    pen.begin_fill()
    for i in range(4):
        pen.forward(size)
        pen.left(90)
    pen.end_fill()

def drawTriangle(size, color):
    pen.color(color)
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

def drawDoor(size, color):
    pen.up()
    pen.right(90)
    pen.forward(size)
    pen.left(90)
    pen.forward(size/3)

    pen.left(90)
    pen.color(color)
    pen.begin_fill()
    pen.forward(size/2.5)
    pen.right(90)
    pen.forward(size/3)
    pen.right(90)
    pen.forward(size/2.5)
    pen.end_fill()
    pen.right(90)
    # Go into the door for knob
    pen.forward(size/30)
    pen.right(90)
    # Go up to height of door nob
    pen.forward(size/6)

    pen.color("yellow")
    pen.dot(10)

def drawWindows(size, color):
    pen.up()
    # Get from door knob to the left window
    pen.backward(size/6)
    pen.left(90)
    pen.forward(2*size/3 - size/30)
    pen.backward(size/4)
    pen.right(90)
    pen.forward(3*size/4)

    # Draw the left window
    pen.color(color)
    pen.down()
    # This will draw 4 squares
    for i in range(4):
        # Draws 1 pane of the window
        for j in range(4):
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)

    pen.up()
    # Get to the right window from the left window
    pen.right(90)
    pen.forward(2*size/4)
    # Draw right window
    pen.color(color)
    pen.down()
    # This will draw 4 squares
    for i in range(4):
        # Draws 1 pane of the window
        for j in range(4):
            pen.forward(size/8)
            pen.left(90)
        pen.left(90)
    pen.up()

# Define a function that draws a house of any size and colors
def drawHouse(size, baseColor, roofColor, doorColor, windowColor):

    # Draw base of house
    drawSquare(size, baseColor)
    # Get to top of house
    pen.left(90)
    pen.forward(size)
    pen.right(90)
    # Draw roof onto house
    drawTriangle(size, roofColor)
    # Draw door onto house
    drawDoor(size, doorColor)
    # # Draw the windows
    drawWindows(size, windowColor)

# drawHouse(300, "purple", "blue", "saddle brown", "black")













turtle.done()
