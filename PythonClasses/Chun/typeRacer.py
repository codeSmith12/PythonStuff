# 1. Imports
import tkinter as tk
import random as r

# 2. Class definitions
class Word:
    def __init__(self,text, x,y):
        self.text = text
        self.x = x
        self.y = y
        self.typed = False

class Player:
    def __init__(self, name):
        self.score = 0
        self.words_typed = 0
        self.name = name

    def increase_score(self, points):
        self.score += points
        self.words_typed += 1

# 3. Functions
def draw_word(canvas, word):
    canvas.create_text(word.x, word.y, text=word.text, fill="lightgrey")

def update_display():
    global current_word
    canvas.delete("all")
    current_word.y+=1
    draw_word(canvas, current_word)

    if current_word.y > 400:
        game_over()
    else:
        window.after(50, update_display)

def game_over():
    canvas.create_text(200, 200, text="Game Over!")

def generate_word():
    words = ["python", "test", "programming", "computer", "algorithm", "developer"]
    text = r.choice(words)
    x = r.randint(50, WIDTH-50)
    return Word(text, x, 0)

# Main program

window = tk.Tk()
window.title("Type Racer (KnockOff)")

player = Player("Brian is a great professor")
score_label = tk.Label(window, text=f"Score: {player.score}")
score_label.pack() 



# 1. CREATE CONSTANTS FOR WIDTH AND HEIGHT
WIDTH = 400
HEIGHT = 600
INPUT_HEIGHT = 50

# 2. SET THE WINDOW SIZE TO THESE VALUES
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT-INPUT_HEIGHT, bg="black")
canvas.pack()

current_word = generate_word()
draw_word(canvas, current_word)

update_display()

tk.mainloop()
