# TODO:
# Take in email account? Title + Email + PW, everything needed
# Weakly cover encryption, we could make a cypher encrypter / decrypter
# If we had decrypter, we would probably have to load the data from file into
# the program and show the passwords through a GUI instead of just a text file?

from tkinter import *
from random import *
from datetime import datetime

tk = Tk()
tk.geometry("800x200")
tk.title("Password Generator 2.0")

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z']
characters = ['!','@','#','$','%','^','&','*','(',')','-','=']
numbers = ['0','1','2','3','4','5','6','7','8','9']


global password
password = ""

passwordFont = ("Times", 20,"bold")

titleLabel = Label(tk, text="Title:")
titleValue = Text(tk, height = 1, width=20)
titleValue.configure(font = passwordFont)

lengthLabel = Label(tk, text="Length")
spin = Spinbox(tk, from_= 8, to = 16)

passwordLabel = Label(tk, text="Password")
passwordValue = Text(tk, height = 1, width=54)
passwordValue.configure(font = passwordFont)

# First row
titleLabel.grid(row=0,column=0)
titleValue.grid(row=0,column=1)

# Second row
lengthLabel.grid(row=1,column=0)
spin.grid(row=1,column=1, sticky=W)

# Third row
passwordLabel.grid(row=2,column=0)
passwordValue.grid(row=2,column=1, sticky=EW) # Add fonts to this part

def generate(spin):
    global password
    length = int(spin.get())
    print("Generating password of length", length)
    for i in range(length):
        if i % 2 == -1:
            letter = choice(letters)
        elif i % 2 == 0:
            letter = choice(characters)
        elif i % 2 == 1:
            letter = choice(numbers)
        password += letter
    print(password)
    file = open("password.txt", "a")
    today = datetime.now()
    timeStamp = today.strftime("%B %d, %Y %H:%M:%S")
    fileEntry = "\nTitle: " + titleValue.get("1.0", END) + "Password: " + password + "\nDate Generated: " + timeStamp + "\n\n"

    file.write(fileEntry)
    # file.write(password + "\n")
    file.close()

    passwordValue.delete("0.-1",END)
    passwordValue.insert(INSERT, password)
    password = ""


generateBtn = Button(tk, command=lambda:generate(spin), text="Generate", padx=20, font=passwordFont)
generateBtn.grid(row=3,column=1)



tk.grid_columnconfigure(0,weight=1)
tk.grid_columnconfigure(1,weight=3)


tk.mainloop()
