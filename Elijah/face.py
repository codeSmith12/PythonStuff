import turtle
pen = turtle.Turtle()

pen.speed(0)
# Draw face
pen.color("red")
pen.pensize(4)
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Draw Eyes
pen.color("yellow")
pen.up()
pen.forward(50)
pen.left(90)
pen.forward(150)

# Draw right Eye
pen.dot(35)
pen.left(90)

# Draw left eye
pen.forward(100)
pen.dot(35)









turtle.done()
