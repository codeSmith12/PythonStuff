
"""
Writen in Python 3.9.5

"""
"""
NOTES:
Might need to change stripping algorithm depending on which operating system

Logging soon, but was working on the buttons lighting up when they are playing a sound
and turning off when they are no longer playing. 1 sound works for all buttons...
Buttons aren't individually detectable if they are currently playing.

"""


from tkinter import *
import time
import pygame as pg


class SoundboardButton:
    CHANNELNUM = 0
    def __init__(self):
        # Refactor this once file system is working
        print(SoundboardButton.CHANNELNUM)
        self.fileName = r"C:\Users\bsmit\Documents\PythonStuff\SoundBoard\Later.mp3"
        self.soundFile = pg.mixer.Sound(self.fileName)
        self.channel = pg.mixer.Channel(SoundboardButton.CHANNELNUM)
        SoundboardButton.CHANNELNUM += 1
        # Strip the name of the button to the files name, with no file extension
        self.btnName = self.fileName[self.fileName.rfind("\\")+1:self.fileName.rfind(".")]
        self.id = Button(tk, text=self.btnName, width=BTNWIDTH, height=BTNHEIGHT, command=lambda: [self.play(), test], font=btnFont)

    def play(self):
        self.id.config(bg="green")
        self.soundFile.play()
    def turnOff(self):
        print(self.channel.get_busy())
        if not self.channel.get_busy():
            self.id.config(bg="white")

    def stop(self):
        self.soundFile.stop()

def stopSounds(btns):
    for btn in btns:
        btn.stop()


def test():
    print("test..???")


# CONSTANTS, CHANGE AS YOU WISH
BTNS_PER_ROW = 8
NUMROWS = 2
BTNWIDTH = 5
BTNHEIGHT= 1
XPADDING=10
YPADDING=30
FONTSIZE = 20 # Button size is based on font-size as well

# Using pygame to support playing sounds
pg.mixer.init(44100, -16, NUMROWS * BTNS_PER_ROW, 2048) # frequency, size, channels, buffer.. attempting to increase quality
pg.init()

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
stopBtn.grid(row=NUMROWS+1,columnspan=BTNS_PER_ROW)
settingsBtn = Button(tk, text="Settings", font=btnFont)
settingsBtn.grid(row=NUMROWS+1,column=BTNS_PER_ROW//2 + 1)

tk.geometry(f"{WIDTH}x{HEIGHT}")

running = True
tick=.01

while running:
    tk.update()
    for btn in buttons:
        btn.turnOff()
    time.sleep(tick)
