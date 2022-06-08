from tkinter import *
import time


# FIX BULLETS, THEY GO INTO SPACE FOREVER


class Invader:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = INVADERSPEED
        self.id = canvas.create_rectangle(self.x, self.y, self.x+INVADERSIZE, self.y+INVADERSIZE, fill="lime", outline="")
        self.destroyed = False

    def updatePosition(self):
        pos = canvas.coords(self.id)
        canvas.move(self.id, self.speed, 0)
        if pos[2] >= WIDTH - 20:
            self.speed *= -1
            canvas.move(self.id, self.speed - 5, DROPSIZE)
        elif pos[0] < 20:
            self.speed *= -1
            canvas.move(self.id, self.speed + 5, DROPSIZE)

        pos = canvas.coords(self.id)
        # Check if touched a bullet
        if len(canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])) > 1:
            if 1 in canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3]) and not self.destroyed:
                print("game over")
            else:
                canvas.itemconfig(self.id, fill="black")
                self.destroyed = True
            # canvas.delete(self.id)


class Bullet:
    def __init__(self, pos):
        self.hit = False
        self.id = canvas.create_rectangle(pos[4]-SHIPSIZE//10,pos[1]-SHIPSIZE//2, pos[4]+SHIPSIZE//10, pos[5], fill=BULLETCOLOR, outline="")
            #     self.destroyed = True




class Ship:
    def __init__(self):
        playerLoc = [WIDTH//2-SHIPSIZE //2, HEIGHT*7//8, WIDTH//2+SHIPSIZE //2, HEIGHT*7//8, WIDTH//2, HEIGHT*7//8-SHIPSIZE ]
        self.id = canvas.create_polygon(playerLoc, fill=SHIPCOLOR)
        self.bullets = []
        self.shotDelay = 0.0 # cool downs
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
            bullet = Bullet(pos)
            self.bullets.append(bullet)
            self.shotDelay = 0
    def updateBullets(self):
        self.shotDelay += .05
        for bullet in self.bullets:
            canvas.move(bullet.id, 0, -10)
            pos = canvas.coords(bullet.id)
            # Check if invader(?) touched a bullet
            if len(canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3])) > 1 and not bullet.hit:
                # Make sure the ship isn't the object that touched the bullet.
                if 1 not in canvas.find_overlapping(pos[0],pos[1],pos[2],pos[3]):
                    canvas.itemconfig(bullet.id, fill="black")
                    bullet.hit=True


# Dimensions of space invader are square
WIDTH=600
HEIGHT=WIDTH
SHIPSIZE = 25
SHIPSPEED = 10
INVADERSIZE = 15
SPACEBETWEEN = 75
SPACEABOVE = 50
INVADERSPEED = 1.5
DROPSIZE = 25
TICK = .001
SHOTDELAY = 2 # Not in seconds, its some kind of math.

SHIPCOLOR = "lime"
BULLETCOLOR = "lime"

tk = Tk()
tk.title("Space Invader")
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player = Ship()

global gameOver
gameOver = False

invaders = []
for i in range(3): # 3 rows
    for j in range(6): # 6 columns
        invader = Invader(20 + j*SPACEBETWEEN, 20+i*SPACEABOVE)
        invaders.append(invader)

while not gameOver:
    tk.update()
    player.updateBullets()
    for invader in invaders:
        invader.updatePosition()
    time.sleep(TICK)
