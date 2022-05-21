from tkinter import *

def moveLeft(event):
    canvas.move(player, -SHIPSPEED, 0)

def moveRight(event):
    canvas.move(player, SHIPSPEED, 0)


# Dimensions of space invader are square
WIDTH=600
HEIGHT=WIDTH
SHIPSIZE = 25
SHIPSPEED = 10

tk = Tk()
tk.title("Space Invader")
tk.geometry(f"{WIDTH}x{HEIGHT}")
tk.bind("<KeyPress-Left>", moveLeft)
tk.bind("<KeyPress-Right>", moveRight)

canvas = Canvas(tk, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

player = canvas.create_polygon(WIDTH//2-SHIPSIZE//2, HEIGHT*7//8, WIDTH//2 + SHIPSIZE//2, HEIGHT*7//8, WIDTH//2, HEIGHT*7//8-SHIPSIZE, fill="lime")


tk.mainloop()
