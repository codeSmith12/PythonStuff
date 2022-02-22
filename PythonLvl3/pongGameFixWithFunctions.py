from tkinter import *
import time

tk = Tk()
tk.geometry("400x400")
windowWidth = 400
windowHeight = 400
paddleWidth = 100
paddleHeight = 20
canvas = Canvas(tk, width=windowWidth, height=windowHeight)

paddle = canvas.create_rectangle(0,0, paddleWidth, paddleHeight, fill="red")
canvas.move(paddle, windowWidth/2, windowHeight/2)
canvas.pack()

x=10
y=0

def left():
    return -10

def right():
    return 10

def updatePos():
    canvas.move(paddle, x, y)


x = left()
while True:
    tk.update()
    updatePos()
    time.sleep(.1)
