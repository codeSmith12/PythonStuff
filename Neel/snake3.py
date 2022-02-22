from tkinter import *
from random import randint
import time

class Mouse:
    def __init__(self):
        self.x = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, WIDTH-MOUSE_SPAWN_BORDER)
        self.y = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, HEIGHT-MOUSE_SPAWN_BORDER)
        self.id = canvas.create_rectangle(self.x, self.y, self.x + MOUSESIZE, self.y + MOUSESIZE, fill="grey" )
    def respawnMouse(self):
        self.x = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, WIDTH-MOUSE_SPAWN_BORDER)
        self.y = randint(MOUSESIZE + MOUSE_SPAWN_BORDER, HEIGHT-MOUSE_SPAWN_BORDER)
        canvas.moveto(self.id, self.x, self.y)
    def checkIfTouching(self, snake):
        pos = canvas.coords(self.id)
        overlap = canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])
        if len(overlap) == 2:
            self.respawnMouse()
            snake.eatMouse()


# class Node:
#     def __init__(self, x, y, oval):
#         self.prev_x = x
#         self.prev_y = y
#         self.oval = oval


class Snake:
    def __init__(self):
        self.x = SPEED
        self.y = 0
        self.bodyParts = []
        self.prevPos = []
        self.head = canvas.create_rectangle(WIDTH/2, HEIGHT/2, WIDTH/2 + HEADSIZE, HEIGHT/2 + HEADSIZE, fill="white" )
        self.tail = self.head
        tk.bind("<KeyPress-Up>", self.moveUp)
        tk.bind("<KeyPress-Down>", self.moveDown)
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)

    def updatePosition(self):
        global gameOver
        pos = canvas.coords(self.head)
        self.prevPos.append(pos)
        canvas.move(self.head, self.x, self.y)
        for i in range(len(self.bodyParts)):
            if i == 0:
                canvas.moveto(self.bodyParts[i], pos[0]+HEADSIZE/2, pos[1] + HEADSIZE/2)
            else:
                canvas.moveto(self.bodyParts[i], pos[0] + HEADSIZE / 2, pos[1] + HEADSIZE / 2)
        print(self.prevPos)
        if pos[0] < 0:
            gameOver = True
        elif pos[1] < 0:
            gameOver = True
        elif pos[2] > WIDTH:
            gameOver = True
        elif pos[3] > HEIGHT:
            gameOver = True
    def moveUp(self,key):
        if self.y != SPEED:
            self.y = -SPEED
            self.x = 0
    def moveDown(self,key):
        if self.y != -SPEED:
            self.y = SPEED
            self.x = 0
    def moveLeft(self,key):
        if self.x != SPEED:
            self.x = -SPEED
            self.y = 0
    def moveRight(self,key):
        if self.x != -SPEED:
            self.x = SPEED
            self.y = 0
    def getPos(self):
        return canvas.coords(self.head)
    def getSelf(self):
        return self.head
    def eatMouse(self):
        pos = canvas.coords(self.head)
        print(pos)
        part = canvas.create_oval(pos[2], pos[3], pos[2]+TAILSIZE, pos[3]+TAILSIZE, fill="white")
        self.bodyParts.append(part)
        self.tail = part


tk = Tk()

WIDTH=800
HEIGHT=800
HEADSIZE=25
TAILSIZE=18
MOUSESIZE=15
MOUSE_SPAWN_BORDER = 40
SPEED = 3
TICK = 0.01

tk.geometry(f"{WIDTH}x{HEIGHT}")
tk.configure(bg="black")
canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

snake = Snake()
global gameOver
gameOver = False
mouse=Mouse()
# Game Loop - updates the window with newly moved objects
while not gameOver:
    snake.updatePosition()
    mouse.checkIfTouching(snake)
    tk.update()
    time.sleep(TICK)
