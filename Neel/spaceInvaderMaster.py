from tkinter import *
import time

class Invader:
    def __init__(self):
        pass


class Ship:
    def __init__(self):
        playerLoc = [WIDTH//2-SHIPSIZE //2, HEIGHT*7//8, WIDTH//2+SHIPSIZE //2, HEIGHT*7//8, WIDTH//2, HEIGHT*7//8-SHIPSIZE ]
        self.id = canvas.create_polygon(playerLoc, fill=SHIPCOLOR)
        self.bullets = []
        self.shotDelay = 0.0
        tk.bind("<KeyPress-Left>", self.moveLeft)
        tk.bind("<KeyPress-Right>", self.moveRight)
        tk.bind("<space>", self.shoot)

    def moveLeft(self, event):
        canvas.move(self.id, -SHIPSPEED, 0)

    def moveRight(self, event):
        canvas.move(self.id, SHIPSPEED, 0)

    def shoot(self, event):
        if self.shotDelay > SHOTDELAY:
            pos = canvas.coords(self.id)
            # Below creates a bullet from the middle point (tip) of the ship. builds in relation to the middle point
            bullet = canvas.create_rectangle(pos[4]-SHIPSIZE//10,pos[1]-SHIPSIZE//2, pos[4]+SHIPSIZE//10, pos[5], fill=BULLETCOLOR)
            self.bullets.append(bullet)
            self.shotDelay = 0

    def updateBullet(self):
        self.shotDelay += .05
        for bullet in self.bullets:
            canvas.move(bullet, 0, -10)


# Dimensions of space invader are square
WIDTH=600
HEIGHT=WIDTH
SHIPSIZE = 25
SHIPSPEED = 10
TICK = .001
SHOTDELAY = 2 # Not in seconds, its some kind of math.

SHIPCOLOR = "lime"
BULLETCOLOR = "lime"

tk = Tk()
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player = Ship()

global gameOver
gameOver = False

while not gameOver:
    tk.update()
    player.updateBullet()
    time.sleep(TICK)
