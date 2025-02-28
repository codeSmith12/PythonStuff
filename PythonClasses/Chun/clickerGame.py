import tkinter as tk
import math

'''
TODO:
Reduce time between tics for passive income

Ideas:
Passive income, tiers
Multiplier

RNG 1000 click (one time)

Random spawns, get fraction of second to click


challenges:
   Typing challenges
'''

def play_game():
    while True:
        display_clicks()
        print("1. Click")
        print("2. Leave game")
        choice = input()

        if choice == "1":
            click()
        elif choice == "2":
            break
        else:
            print("Invalid option, try again")

def click():
    global clicks
    clicks += multi
    display_clicks()

def display_clicks():
    global clicks
    clicks_label.config(text=f"Clicks: {clicks}")

def buyMulti():
    global clicks, multi
    # Check if we have enough clicks
    if clicks < 20:
        print("You don't have enough")
    else:
        clicks -= 20
        multi += 1
        display_clicks()

def buyPassive():
    global clicks, passive
    if clicks >= 100:
        clicks -= 100
        passive += 1 
        display_clicks()
    else:
        print("You don't have enough")
    
def processPassive():
    global passive, clicks
    clicks += passive
    display_clicks()
    window.after(1000, processPassive)
        

# CONSTANTS
WIDTH = 600
HEIGHT = 400
PASSIVE_REDUCE = .1

# Click related variables
clicks = 0
multi = 1
passive = 0

#GUI Variables ------------

# Set up window
window = tk.Tk()
window.geometry(f"{WIDTH}x{HEIGHT}")

# Create label to display number of clicks
clicks_label = tk.Label(window, text=f"Clicks: {clicks}")
clicks_label.pack() 

# Clickable button that gives points
click_btn = tk.Button(window, text="Click me!", command=click)
click_btn.pack() 

# Buy Multiplier buttons
multi_btn = tk.Button(window, text="Buy multiplier (20 clicks)", command=buyMulti)
multi_btn.pack() 

# Create a button for buying passive income
pass_btn = tk.Button(window, text="Buy passive (100 clicks)", command=buyPassive)
pass_btn.pack() 

processPassive()
# Keeps window open and running
window.mainloop()