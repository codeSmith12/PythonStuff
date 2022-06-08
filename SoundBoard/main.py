"""
Writen in Python 3.9.5

"""



"""
NOTES:
Might need to change stripping algorithm depending on which operating system

"""


from tkinter import *
import pygame as pg

# Using pygame to support playing sounds
pg.mixer.init()
pg.init()
pg.mixer.set_num_channels(50)

class SoundboardButton:
    def __init__(self):

        # Refactor this, seems repetetive...
        self.fileName = r"C:\Users\bsmit\Documents\PythonStuff\SoundBoard\coin.wav"
        self.soundFile = pg.mixer.Sound(self.fileName)
        # Strip the name of the button to the files name, with no file extension
        self.btnName = self.fileName[self.fileName.rfind("\\")+1:self.fileName.rfind(".")]
        self.id = Button(tk, text=self.btnName, width=BTNWIDTH, height=BTNHEIGHT, command=self.play, font=btnFont)
    def play(self):
        self.soundFile.play()


BTNWIDTH = 5
BTNHEIGHT= 2
XPADDING=10
YPADDING=30
HEIGHT=300
FONTSIZE = 20
WIDTH=(90*8+10*8)*2 # Figure out width to work proportionately...


tk = Tk()
tk.title("Sound Board by codeSmith12")
tk.geometry(f"{WIDTH}x{HEIGHT}")

btnFont = ("Helvetica", FONTSIZE)


buttons = []
for i in range(2):
    for j in range(8):
        btn = SoundboardButton()
        btn.id.grid(row=i, column=j, padx=XPADDING, pady=YPADDING)
        btn.id.update()
        print(btn.id.winfo_width())
        buttons.append(btn)



tk.mainloop()
