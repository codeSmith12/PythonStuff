# print("Hello world!")
# print("I love my dog, Ferox.")

import turtle, time
pen = turtle.Turtle()
pen.pensize(8)
pen.color("red")
#
# square
def drawSquare():
    # pen.begin_fill()
    for i in range(4):
        pen.forward(100)
        pen.left(90)
    # pen.end_fill()
# drawSquare()
# for i in range(10):
#     drawSquare() # Calling the function...
#     pen.left(10)


# 360 / # sides = degrees to turn by.
# drawPolygon
# TODO Cover input with students first thing tomorrow...
def drawPolygon(size):
    numSides = 10
    degrees =  360 / numSides
    for i in range(numSides):
        pen.forward(size)
        pen.left(degrees)
drawPolygon(150)
# # triangle
# for i in range(3):
#     pen.forward(100)
#     pen.left(120)
#
# pen.begin_fill()
# pen.circle(100)
# pen.end_fill()


time.sleep(20)
