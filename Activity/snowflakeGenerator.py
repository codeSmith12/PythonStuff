import turtle, time
# Set the background color to black
turtle.bgcolor("black")

# This code will make one branch and reset the pen where it started 
def makeBranch(size):
    pen.forward(size)
    pen.backward(size)

# This function will add numV's V's to each branch. Each V will be evenly spaced out based on size
def makeVs(size):
    for i in range(numVs):
        pen.forward(size/numVs)
        pen.left(45)
        pen.forward(vSize)
        pen.backward(vSize)
        pen.right(90)
        pen.forward(vSize)
        pen.backward(vSize)
        pen.left(45)
    pen.backward(size)
    pen.left(360 / branches)
        

    
# Create pen and format the pen
pen = turtle.Turtle()
pen.speed(0)

















# Number of V's per branch
numVs = 5
# Length of each V
vSize =31
# Number of main branches in the snowflake
branches = 25
# Length of each main branch
size = 10
# Thickness
penSize = 4
# Color...
penColor ="aqua"






# # Number of V's per branch
# numVs = 12
# # Length of each V
# vSize = 200
# # Number of main branches in the snowflake
# branches = 16
# # Length of each main branch
# size = 200
# # Thickness
# penSize = 2
# # Color...
# penColor = "cyan"








pen.color(penColor )
pen.width(penSize)

while True:
    pen.clear()
    for i in range(branches):
        makeBranch(size)
        makeVs(size)
        
        
    # pen.hideturtle()
    time.sleep(5)
turtle.mainloop()