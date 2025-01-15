import turtle, time

def drawPattern(numPatterns, numSides, distance, color):
  pen.color(color)
  for i in range(numPatterns):
    for j in range(numSides):
      pen.forward(length*distance)
      pen.left(360/numSides)
    pen.left(360/numPatterns)
    
pen = turtle.Turtle()
turtle.clear()
pen.color("black")
pen.pensize(100000)
pen.forward(1)
# Make the drawing FAST
pen.speed(0)
# Change these values to get different results!
length = 40
pensize = 2
pen.pensize(pensize)

# Control your beautiful design, change the numbers to experiment
# (How many objects, number of sides, distance from center multiplier, color of object)
drawPattern(80, 3, 7, "red")
drawPattern(80, 3, 6.5, "magenta")
drawPattern(80, 3, 5.5, "blue")
drawPattern(80, 3, 4.5, "lime")
drawPattern(100, 6, 1.5, "yellow")
drawPattern(30, 3, 1.5, "cyan")
drawPattern(20, 4, .8, "crimson")
  
