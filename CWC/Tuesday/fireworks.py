import turtle, random
pen = turtle.Turtle()
pen.speed(100)
# turtle.bgcolor("black") # Change background color to black
pen.pensize(10000000)
pen.color("black")
pen.forward(10)
pen.pensize(4)
 # Algorithm -> Series of steps to take, to solve a problem.
for i in range(15):
    x = random.randint(-250, 250)
    y = random.randint(-250, 250)

    pen.up()
    pen.goto(x,y)
    pen.down()
    size = random.randint(50,300)

    colors = ["green", "red", "blue", "crimson", "maroon", "teal", "cyan", "pink", "purple", "salmon"]
    # aqua

    pen.color(random.choice(colors))
    for i in range(36):
        pen.forward(size)
        pen.backward(size)
        pen.left(10)

turtle.mainloop()
