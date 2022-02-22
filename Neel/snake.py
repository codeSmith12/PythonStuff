from tkinter import *
from random import randint
import time

class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white" )
    def updatePosition(self):
        canvas.move(self.head, self.x, self.y)

tk = Tk()

WIDTH=800
HEIGHT=800
HEADSIZE=20
SPEED = 3
TICK = 0.01

tk.geometry(f"{WIDTH}x{HEIGHT}")
tk.configure(bg="black")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = Snake()

# Game Loop - updates the window with newly moved objects
while True:
    snake.updatePosition()
    tk.update()
    time.sleep(TICK)
