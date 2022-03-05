# snake.py
import tkinter

# Functions
def drawGrid(): # 20
    CELL_WIDTH = WIDTH // HEAD_SIZE
    CELL_HEIGHT = HEIGHT // HEAD_SIZE
    for i in range(CELL_HEIGHT):
        canvas.create_line(0, CELL_HEIGHT*i, WIDTH, CELL_HEIGHT*i, fill="ivory3")
    # TODO: Make loop for columns
tk = tkinter.Tk()
tk.title("Snake")
# Constants
WIDTH = 800
HEIGHT = 800
HEAD_SIZE = 25
# Set the size of the window
tk.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tkinter.Canvas(tk, width=WIDTH, height=HEIGHT)
# Change the background color to black
canvas.configure(bg="black")
canvas.pack()
drawGrid()



# Keeps window open
tk.mainloop()
