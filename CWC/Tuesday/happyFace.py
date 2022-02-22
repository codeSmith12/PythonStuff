# ATOM -> Allows me to develop code FASTER
# and BETTER
import turtle

pen = turtle.Turtle()
pen.speed(0)

# Draw and fill face
pen.color("yellow")
pen.begin_fill()
pen.circle(200)
pen.end_fill()

# Get to right eye
pen.up()
pen.forward(100)
pen.left(90)
pen.forward(300)
pen.down()

# Draw right eye
pen.color("green")
pen.dot(50)

# Get to left eye
pen.up()
pen.left(90)
pen.forward(200)

# Draw left eye
pen.down()
pen.dot(50)
pen.up()

# Get to mouth
pen.color("red")
pen.left(90)
pen.forward(150) # decides how high up the mouth is drawn

# Draw the mouth
pen.begin_fill()
pen.down()
pen.circle(95, 180)
pen.end_fill()
pen.up()

# Get to Nose
pen.goto(0, 250)
pen.left(150)
pen.down()
pen.color("blue")

# Draw the nose
pen.begin_fill()
pen.forward(50)
pen.left(120)
pen.forward(15)
# Left nostril
pen.dot(15)
pen.forward(25)
# Right nostril
pen.dot(15)
pen.forward(15)
pen.left(120)
pen.end_fill()

# Get to top of head
pen.up()
pen.goto(0,400) # Absolute coordinate
# Draw hat!
# The angle of the hat!
pen.left(90)
pen.down()
# Color of the hat
pen.color("purple")

# Draw the hat using a loop
pen.begin_fill()
for i in range(3):
    pen.forward(200) # Size of the hat
    pen.right(120)
pen.end_fill() # Not tabbed, not inside the forloop









turtle.done()
