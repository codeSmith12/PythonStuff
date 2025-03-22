import tkinter as tk
import random

class Word:
    def __init__(self,text, x,y):
        self.text = text
        self.x = x
        self.y = y
        self.is_typed = False

class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.words_typed = 0
        
    def increased_score(self, points):
        self.score += points
        self.words_typed += 1


def drawWord(canvas, word):
    canvas.create_text(word.x, word.y,  text=word.text, fill="lightgrey")

def update_display():
    global current_word
    canvas.delete("all")
    current_word.y+=1
    drawWord(canvas, current_word)

    if current_word.y > 400:
        game_over()
    else:
        window.after(50, update_display)

def game_over():
    canvas.create_text(200,200,text="Game Over!")
    
def generate_word():
    words = ["python", "programming", "computer", "algorithm", "developer", "software"]
    text = random.choice(words)
    x = random.randint(50, 350)
    return Word(text, x, 0)

def check_word():
    global current_word
    typed_word = input_entry.get()
    if typed_word == current_word.text:
        player1.increase_score(len(typed_word))
        score_label.config(text=f"Score: {player1.score}")
        current_word = generate_word()
    input_entry.delete(0, tk.END)



window = tk.Tk()
window.title("Type Racer")

player1 = Player("Player 1")
score_label = tk.Label(window, text=f"Score: {player1.score}")
score_label.pack()

WIDTH = 400
HEIGHT = 600
window.geometry(f"{WIDTH}x{HEIGHT}")

canvas = tk.Canvas(window, width=WIDTH, height=HEIGHT-50, bg="black")
canvas.pack()

input_entry = tk.Entry(window, bg="white")
input_entry.pack()

input_entry.bind("<Return>", check_word)

current_word = generate_word()

drawWord(canvas, current_word)

update_display()

tk.mainloop()