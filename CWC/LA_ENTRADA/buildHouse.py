import turtle

def makeHouse(size):
    drawSquare(size)

def drawSquare(size):
    pen.begin_fill() # Begin fill
    for i in range(4): # Draw the shape
        pen.forward(size)
        pen.left(90)
    pen.end_fill() # end fill    

def drawRoof(size):
    pen.color("crimson")
    pen.begin_fill()
    for i in range(3):
        pen.forward(size)
        pen.left(120)
    pen.end_fill()

pen = turtle.Turtle()
pen.color("cyan")
pen.speed(0)
size = 100
# Draw Base of house


drawSquare(size)
# Get to top left corner of house
pen.left(90)
pen.forward(size)
pen.right(90)
# Build roof
# DEFINE A NEW FUNCTION THAT DRAWS THE ROOF

# CALL THE FUNCTION
drawRoof(size)
# Build Door
pen.right(90)
pen.up()
pen.forward(size)
pen.left(90)

pen.forward(size/3)
pen.down()
pen.left(90)
# YOUR CHALLENGE IS TO MAKE A SQUARE THATS FILLED WITH A COLOR (BROWN?)

# DRAW DOOR
pen.begin_fill()
for i in range(4):
    pen.forward(size/3)
    pen.right(90)
pen.end_fill()

pen.up()
pen.goto(size/4, size*3/4)
pen.down()

# CHALLENGE DRAW 1 SQUARE (SIZE/8) FOR THE WINDOW
for i in range(4):
    pen.forward(size/8)
    pen.right(90)

turtle.mainloop()



