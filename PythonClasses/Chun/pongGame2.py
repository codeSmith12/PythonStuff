'''
Ball:

Speed / direction

Collision detection
x
y

Paddle:
WIDTH and HEIGHT
SPEED
Collision detection
Color, maybe chosen at begining, maybe shifts over time
Y Movement


'''

import tkinter as tk
import time

class Ball:
    def __init__(self, color):
        self.x = WIDTH/2 - BALL_SIZE/2
        self.y = HEIGHT/2 - BALL_SIZE/2
        self.x_velocity = X_VEL
        self.y_velocity = Y_VEL
        self.id = canvas.create_oval(self.x, self.y, self.x+BALL_SIZE, self.y+BALL_SIZE, fill=color, outline=color)
        
    def update_position(self):
        canvas.move(self.id, self.x_velocity, self.y_velocity)
        



# Constants
WIDTH = 1000
HEIGHT = 800
LINE_WIDTH = 10
BALL_SIZE = 40
TICK = .01*6 # 60 frames per second (I think)
X_VEL = 5
Y_VEL = 5

# Window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

# Canvas
canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Draw Line
canvas.create_line(WIDTH/2, 0, WIDTH/2, HEIGHT, width=LINE_WIDTH, fill="white")

# BUILD THE BALL
ball = Ball("red")

#window.mainloop()

while True:
    ball.update_position()
    window.update()
    time.sleep(TICK)
