# smiley.py
import turtle
pen = turtle.Turtle()
pen.speed(0)

# Draw face
pen.color("yellow")
pen.begin_fill() # Set the beginning of the fill
pen.circle(100) # radius
pen.end_fill()
# Draw right eye
pen.color("black")
pen.up()
pen.forward(50)
pen.left(90)
pen.forward(150)
pen.begin_fill()
pen.circle(15)
pen.end_fill()

# Draw left eye
pen.left(90)
pen.forward(70)
pen.right(90)
pen.begin_fill() # Set the beginning of the fill
pen.circle(15) # radius
pen.end_fill()

# Get to top left corner of the mouth
pen.left(180)
pen.forward(81)
pen.right(90)
pen.forward(30) # Here is how left or right the mouth is..
pen.left(90) # Point the pen in the correct direction

# Draw mouth
pen.color("red") # Set the color of the mouth
pen.begin_fill()
pen.circle(50, 180) # Draws half a circle
pen.end_fill()

noseSize = 30
# Get to nose
pen.goto(noseSize / 2, 120) # integer is a whole number
pen.left(90)
# Draw the nose
pen.color("purple")
pen.begin_fill()
for i in range(3):
    pen.forward(noseSize)
    pen.left(120) # 360 / # sides (3) == degrees per turn
pen.end_fill()

# Get to hat
pen.goto(-100, 100)

# Function that draws any shape
def drawPoly(sides):
    for i in range(sides):
        pen.forward(120) # Decides how big the hat is
        pen.right(360/sides)

pen.down()
# Please fill the hat in
pen.right(65) # Decides how angled the hat is,6
pen.begin_fill() # Fills in the hat
drawPoly(3) # Draws the hat
pen.end_fill() # end the fill

for i in range(36):
    drawPoly(4)
    pen.left(10)








turtle.done()
