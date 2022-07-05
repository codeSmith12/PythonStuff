
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
from tkinter import filedialog
import time
import pygame as pg
from functools import partial


class SoundboardButton:
    CHANNELNUM = 0
    def __init__(self, fileName=""):
        # Refactor this once file system is working
        # print(SoundboardButton.CHANNELNUM)
        self.fileName =  fileName# Fix for comp...
        if len(self.fileName) > 0:
            self.soundFile = pg.mixer.Sound(self.fileName)
            self.channel = pg.mixer.Channel(0)# 0 -> SoundBaordbutton.CHANNELNUM
        self.num = SoundboardButton.CHANNELNUM
        SoundboardButton.CHANNELNUM += 1
        # Strip the name of the button to the files name, with no file extension
        self.btnName = self.fileName[self.fileName.rfind("\\")+1:self.fileName.rfind(".")]
        self.id = Button(tk, text=self.btnName, width=BTNWIDTH, height=BTNHEIGHT, command=lambda: [self.play(), displaySettings], font=btnFont) # Why did I use a list here??
        # self.id.bind("<Button-3>", displaySettings)
    def play(self):
        self.id.config(bg="green")
        self.soundFile.play()
    def turnOff(self):
        # print(self.channel.get_busy())
        if not self.channel.get_busy():
            self.id.config(bg="white")

    def stop(self):
        self.soundFile.stop()

def displaySettings(btn, event):
    # Open up the file browser, searching for mp3 and wav files.
    btn.fileName = filedialog.askopenfilename(initialdir = ".", title = "Select a File", filetypes = (("mp3 files", "*.mp3"),
    ("wav files", "*.wav")))
    if btn.fileName: # if someone made a selection
        btn.soundFile = pg.mixer.Sound(btn.fileName) # Assign the file to the sound
        # Strip the name and display on the button
        btn.btnName = btn.fileName[btn.fileName.rfind("/")+1:btn.fileName.rfind(".")] # Sometimes rfind("\\") for windows, sometimes not..
        btn.id.config(text=btn.btnName)

def stopSounds(btns):
    for btn in btns:
        btn.stop()

def onClosing():
    global running
    listOfSound = open("sounds.txt", "w")
    for btn in buttons:
        listOfSound.write(f"{btn.fileName}\n")
    listOfSound.close()
    running = False

# CONSTANTS
BTNS_PER_ROW = 8
NUMROWS = 2
BTNWIDTH = 5
BTNHEIGHT= 1
XPADDING=10
YPADDING=30
FONTSIZE = 20 # Button size is based on font-size as well
RIGHT_CLICK = 3 # Windows uses 3, other OS may use 2 for right click
global SETTINGS_OPEN # Bool so we dont open multiple settings windows.
SETTINGS_OPEN = False

# Using pygame to support playing sounds
pg.mixer.init(44100, -16, NUMROWS * BTNS_PER_ROW, 2048) # frequency, size, channels, buffer.. attempting to increase quality
pg.init()

tk = Tk()
tk.title("SoundBoard by codeSmith12")
btnFont = ("Helvetica", FONTSIZE)

# Create all the buttons depending on the constants provided.
getSoundFiles = open("sounds.txt", "r")
buttons = []
for i in range(NUMROWS):
    for j in range(BTNS_PER_ROW):
        sound = getSoundFiles.readline().rstrip()
        btn = SoundboardButton(sound)
        btn.id.grid(row=i, column=j, padx=XPADDING, pady=YPADDING, sticky="W")
        btn.id.update() # used because it updates the width and height of btn.id
        buttons.append(btn)

for btn in buttons:
    closure = partial(displaySettings, btn)
    btn.id.bind(f"<Button-{RIGHT_CLICK}>", closure)


# Calculate width & height based on the size and amount of buttons
WIDTH=(buttons[0].id.winfo_width()*BTNS_PER_ROW+XPADDING*2*BTNS_PER_ROW)
HEIGHT=((buttons[0].id.winfo_height()*NUMROWS+1)+YPADDING*2*(NUMROWS+1)) # numrows +1 for the stop button.

stopBtn = Button(tk, text="Stop", font=btnFont, command=lambda: stopSounds(buttons), bg="red")
stopBtn.grid(row=NUMROWS+1,columnspan=BTNS_PER_ROW)

tk.geometry(f"{WIDTH}x{HEIGHT}")
global running
running = True
tick=.01

tk.protocol("WM_DELETE_WINDOW", onClosing)

while running:
    tk.update()
    for btn in buttons:
        btn.turnOff()
        time.sleep(tick)
