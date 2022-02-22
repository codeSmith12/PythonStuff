import turtle, time
pen = turtle.Turtle()

# Pen settings
pen.hideturtle()
pen.speed(0)

# Draw the face
pen.color("yellow")
pen.begin_fill()
pen.circle(200) # Radius == 200, diameter == 400
pen.end_fill()


# Get to eye level, draw eyes
pen.color("black")
pen.up()
# Get to eye level
pen.forward(80)
pen.left(90)
pen.forward(300)

# Place right eye
pen.dot(75) # Diameter = 10, radius = 5
# Get to left eye
pen.left(90)
pen.forward(150)
# Place left eye
pen.dot(65)
#  Get to mouth
pen.left(90)
pen.forward(200)

# Draw mouth
pen.color("red")
pen.begin_fill()
pen.down()
pen.circle(75, 180)
pen.up()
pen.end_fill()

# Get to hat
pen.color("purple")
pen.goto(-200, 200) # x, y
pen.down()
pen.right(35)

# Draw Hat and fill it in
pen.begin_fill()
pen.forward(250)
pen.left(120)
pen.forward(250)
pen.left(120)
pen.forward(250)
pen.left(120)
pen.end_fill()
# 360 / # sides = degrees you must turn, per side
# For triangle, 360 / 3 = ???
turtle.done()
