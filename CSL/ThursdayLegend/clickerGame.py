import tkinter as tk

def click():
    global clicks
    clicks += multiplier
    clicks_label.config(text=f"Clicks: {clicks}")

def buyMulti():
    global multiplier, clicks
    if clicks >= MULTI_COST:
        multiplier += 1
        clicks -= 20
        clicks_label.config(text=f"Clicks: {clicks}")
    else:
        print("Peasant... You need more skrill")


window = tk.Tk() # Constructor, builds an object

# Constants
WIDTH = 400
HEIGHT = 400
MULTI_COST = 20

# Game variables
clicks = 0
multiplier = 1


window.geometry(f"{WIDTH}x{HEIGHT}")

clicks_label = tk.Label(window, text=f"Clicks: {clicks}")
clicks_label.pack()

click_button = tk.Button(window, text="Click me!", command=click)
click_button.pack()

multi_button = tk.Button(window, text=f"Buy Multiplier ({MULTI_COST} clicks)", command=buyMulti)
multi_button.pack()

window.mainloop()