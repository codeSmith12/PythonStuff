'''
Program created as a halloween themed class.
User will draw a pumpkin with Turtle.

'''

import turtle
pen = turtle.Turtle()

# Pen settings
pen.speed(0)
turtle.bgcolor("black")
pen.color("orange")

# Draw pumpkin outline
pen.begin_fill()
pen.circle(200)
pen.end_fill()

# Draw stem
pen.color("green")
pen.up()
pen.goto(-10,400)
pen.left(90)
pen.down()
pen.begin_fill()
for i in range(40):
    pen.right(1)
    pen.fd(2)
pen.right(75)
pen.fd(20)
pen.left(75)
for i in range(35):
    pen.left(1)
    pen.fd(-2)
pen.end_fill()
pen.up()

# Left Eye
pen.goto(-50, 300)



turtle.done()
