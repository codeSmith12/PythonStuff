# fireworks
import turtle
import random

pen = turtle.Turtle() # pull out the pen from the toolbox
pen.speed(0)

# Create black background
pen.color("black")
pen.pensize(5000)
pen.forward(1)
# Set the size back to normal
pen.pensize(4)

# Create list of colors...
colors = ["maroon","lime","purple",
          "magenta", "blue", "gold", "orange red",
          "pale violet red", "dark orchid", "dark violet",
          "indigo", "medium violet red", "red", "navy"]


for i in range(6):
    # Set random color
    pen.color(random.choice(colors))
    # Set random size
    size = random.randint(50, 200) # 99

    # Go to random location
    x = random.randint(-200,200) # Generate a random value
    y = random.randint(-200,200) # Generate a random value
    pen.up()
    pen.goto(x,y)
    pen.down()

    # Draw the firework
    for i in range(36):
        pen.forward(size)
        pen.backward(size) # backward, NOT backwards
        pen.left(10)















turtle.done()
