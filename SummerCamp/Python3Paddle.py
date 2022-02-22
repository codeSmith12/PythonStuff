import tkinter as tk
import time

# class Smith:
#     def __init__(self,firstName):
#         self.lastName='Smith'
#         self.firstName = firstName
#         self.age = 0
#     def introduction(self):
#         print("My name is ", self.firstName)
# brian = Smith("Brian")
# brian.introduction()

window = tk.Tk()
window.title("Pong Game")
window.geometry("300x300")
windowWidth = 300
windowHeight = 300
canvas = tk.Canvas(window, width=windowWidth, height=windowHeight)
canvas.pack()

width = 100
height = 40

class Paddle:
    def __init__ (self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,0,100,10, fill=color)
        self.canvas.move(self.id, (windowWidth / 2) - (width / 2),
                    (windowHeight / 2) - (height / 2))

paddle = canvas.create_rectangle(0, 0, width, height, fill="red")
#                   X, Y
canvas.move(paddle, (windowWidth / 2) - (width / 2),
                    (windowHeight / 2) - (height / 2))

# Function that will move the paddle to the left by X
# when the left arrow key is pressed
def goLeft(event):
    x = -10
    y = 0
    # Moves paddle to the left by -10
    canvas.move(paddle,x,y)

# Function that will move the paddle to the right by X
# when the left arrow key is pressed
def goRight(event):
    x = 10
    y = 0
    # Moves paddle to the right by -10
    canvas.move(paddle,x,y)

# Must create x and y outside of functions
# so that we can use them in main loop
# Otherwise, the variables will only exist in the functions.
x=0
y=0

window.bind("<KeyPress-Left>", goLeft)
window.bind("<KeyPress-Right>", goRight)

# INFINITE LOOP
while True:
    canvas.move(paddle, x, y)
    window.update()
    time.sleep(.1)
