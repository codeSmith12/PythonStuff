import turtle, time
pen = turtle.Turtle()
# 360 / number of sides == degrees you need to turn
# 360 / 4 = 90
# 360 / 3 = 120
pen.circle(100)

    
# draw Square
for i in range(4):
    pen.forward (100)
    pen.left(90)

pen.left(90)
pen.forward(100)
pen.right(90)

for i in range(3):
    pen.forward (100)
    pen.left(120)















while True:
    time.sleep(2)
