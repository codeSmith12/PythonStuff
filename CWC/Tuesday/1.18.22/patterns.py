import turtle
pen = turtle.Turtle()

pen.speed(0)

# Set background color to black..
pen.color("black")
pen.pensize(2000)
pen.forward(1)
pen.pensize(1)

# Function that draws any shape
def drawPoly(sides, size, color):
    pen.color(color) # <------------
    for i in range(sides):
        pen.forward(size) # Decides how big the hat is
        pen.right(360/sides)

for i in range(36):
    drawPoly(8, 75, "crimson")
    pen.left(10)
    drawPoly(4, 50, "cyan")








turtle.done()
