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
pg.mixer.init(44100, -16, 50, 2048) # frequency, size, channels, buffer, attempting to increase quality
pg.init()

class SoundboardButton:
    def __init__(self):
        # Refactor this once file system is working
        self.fileName = r"C:\Users\bsmit\Documents\PythonStuff\SoundBoard\Later.mp3"
        self.soundFile = pg.mixer.Sound(self.fileName)

        # Strip the name of the button to the files name, with no file extension
        self.btnName = self.fileName[self.fileName.rfind("\\")+1:self.fileName.rfind(".")]
        self.id = Button(tk, text=self.btnName, width=BTNWIDTH, height=BTNHEIGHT, command=self.play, font=btnFont)

    def play(self):
        self.soundFile.play()
    def stop(self):
        self.soundFile.stop()

def stopSounds(btns):
    for btn in btns:
        btn.stop()



# CONSTANTS, CHANGE AS YOU WISH
BTNS_PER_ROW = 8
NUMROWS = 2
BTNWIDTH = 5
BTNHEIGHT= 1
XPADDING=10
YPADDING=30
FONTSIZE = 20 # Button size is based on font-size as well

tk = Tk()
tk.title("SoundBoard by codeSmith12")

btnFont = ("Helvetica", FONTSIZE)

buttons = []
for i in range(NUMROWS):
    for j in range(BTNS_PER_ROW):
        btn = SoundboardButton()
        btn.id.grid(row=i, column=j, padx=XPADDING, pady=YPADDING, sticky="W")
        btn.id.update() # used because it updates the width and height of btn.id
        buttons.append(btn)


# Calculate width & height based on the size and amount of buttons
WIDTH=(buttons[0].id.winfo_width()*BTNS_PER_ROW+XPADDING*2*BTNS_PER_ROW)
HEIGHT=((buttons[0].id.winfo_height()*NUMROWS+1)+YPADDING*2*(NUMROWS+1)) # numrows +1 for the stop button.

stopBtn = Button(tk, text="Stop", font=btnFont, command=lambda: stopSounds(buttons), bg="red")
stopBtn.grid(row=NUMROWS+1,columnspan=8)

tk.geometry(f"{WIDTH}x{HEIGHT}")

tk.mainloop()
