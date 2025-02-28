import turtle
pen = turtle.Turtle()

# Face color parameters
faceColor = "grey"
eyeColor = "blue"
mouthColor = "green"
noseColor = "purple"
hatColor = "red"


# Draw base of face
pen.color(faceColor)
pen.begin_fill()
pen.circle(100)
pen.end_fill()

# Get to right eye
pen.color(eyeColor)
pen.up()
# Decides how far to the right the eye is
pen.forward(45)
pen.left(90)
# Decides how high up the right eye is
pen.forward(145)
# Dot makes the eye
pen.dot(27)

# Get to left eye
pen.left(90)
pen.forward(90)
# Draw left eye
pen.dot(27)

# Get to left corner of mouth
pen.left(90)

# How high the mouth is
pen.forward(80)
pen.color(mouthColor)
pen.begin_fill()
# Draw mouth....
pen.circle(45, 180)
pen.end_fill()

noseSize = 30
# Get to Nose
# X,Y (X == horizontal, Y == up and down)
pen.goto(-noseSize / 2, 95) # Change y value for nose height

# Draw the nose
pen.right(90)
pen.color(noseColor)
pen.begin_fill()
for i in range(3):
  pen.forward(noseSize)
  pen.left(120)
pen.end_fill()

# Get to left side of hat
pen.goto(-100,100)
# Tilt the hat
pen.left(65)

hatSize = 110

# Move up the head to place the hat
# correctly
# How far up the head we go
pen.forward(80)
# tilt the hat 
pen.right(55)
pen.color(hatColor)

pen.begin_fill()

for i in range(3):
  pen.forward(hatSize)
  pen.left(120)

pen.end_fill()


turtle.mainloop()