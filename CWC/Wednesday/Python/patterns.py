import turtle
pen = turtle.Turtle() # Create a pen object, store in pen

# pen.begin_fill()
# for i in range(4): # pen.begin_fill()
#     pen.forward(100) # pen.end_fill()
#     pen.left(90)
# pen.end_fill()
# # TRIANGLE TIME!! USING A FORLOOP
# pen.begin_fill()
# for i in range(3): # pen.begin_fill()
#     pen.forward(100) # pen.end_fill()
#     pen.left(120)
# pen.end_fill()
# # 360 / 6 = 60
# pen.begin_fill()
# for i in range(6): # pen.begin_fill()
#     pen.forward(100) # pen.end_fill()
#     pen.left(60)
# pen.end_fill()
pen.speed(0)

def drawShape(numSides):
    # pen.begin_fill()
    for i in range(numSides): # pen.begin_fill()
        pen.forward(50)   # pen.end_fill()
        pen.left(360 / numSides) # integers, whole number
    # pen.end_fill()

for i in range(36):
    pen.color("blue")
    drawShape(4)
    pen.left(10)
    pen.color("red")
    pen.forward(50)
    drawShape(3)
    pen.backward(50)




turtle.done()
