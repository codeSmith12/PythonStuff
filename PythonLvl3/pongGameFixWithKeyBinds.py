from tkinter import *
import time

tk = Tk() # Create the tkinter object

# Set up variables so dimensions
# of window and paddle can be tweaked at anytime
windowWidth = 400
windowHeight = 400
paddleWidth = 100
paddleHeight = 20

# Create canvas object, pass in our dimension variables
canvas = Canvas(tk, width=windowWidth, height=windowHeight)

# paddle = canvas.create_rectangle(0,0, paddleWidth, paddleHeight, fill="red")
# Place canvas into the tk object.
canvas.pack()

# X is a variable that drives our paddle.
# Along with updatePos, which will continually move the paddle
# by X (-10 or 10)
x=10
y=0

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.paddle = self.canvas.create_rectangle(0, 0, paddleWidth, paddleHeight, fill=color)
        self.canvas.move(self.paddle, windowWidth/2, windowHeight/2)
        self.x=0
        tk.bind("<KeyPress-Left>", self.left)
        tk.bind("<KeyPress-Right>", self.right)

    # Sets X to move the paddle in the negative direction (left)
    def left(self,event):
        print("hello")
        self.x = -10

    # Sets X to move the paddle in the positive direction (right)
    def right(self,event):
        self.x = 10
    def update(self):
        self.canvas.move(self.paddle, self.x, 0)



paddle = Paddle(canvas, "red")
# Main Loop, moves the paddle, ball and updates their positions on the screen
while True:
    paddle.update()
    tk.update()
    time.sleep(.1)
