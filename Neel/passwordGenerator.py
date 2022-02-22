# https://likegeeks.com/python-caesar-cipher/
from tkinter import *
from random import *
import cipher, webbrowser
from datetime import datetime

tk = Tk()
tk.geometry("500x600")
characters = ['!','@','$','#','%','^','&','*','(',')','_'+',']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z' ]
numbers = ['1','2','3','4','5','6','7','8','9','0']
Font = ("Times", 26, "bold")
spinFont = ("Times", 22, "normal") # <--- Spinbox's specific font

titleLabel = Label(tk, text="Title:", font=Font)
titleValue = Text(tk, height=1, width=20, font=Font)
titleLabel.grid(sticky=W, row=0,column=0)
titleValue.grid(sticky=W, row=0,column=1)

lengthLabel = Label(tk, text="Length:", font=Font)
spin1 = Spinbox(tk, from_ = 8, to = 16, width=5, font=spinFont)
lengthLabel.grid(sticky=W, row=1, column=0)
spin1.grid(sticky=W, row=1, column=1)

global password
password = ""

def generate():
    global password
    length = int(spin1.get())
    print("Generating password of length", length)
    for i in range(length):
        if i % 3 == 0:
            letter = choice(letters)
        elif i % 3 == 1:
            letter = choice(characters)
        elif i % 3 == 2:
            letter = choice(numbers)
        password += letter
    today = datetime.now()
    print(today)
    print(password)

    passwordLabel ['text'] = "Your new password is:"
    passwordValue.delete("0.-1",END)
    passwordValue.insert(INSERT, password)

    timeStamp = today.strftime("%B %d, %Y %H:%M:%S")

    # Get formatted string into a variable
    message = "\nTitle: " + titleValue.get("1.0", END) + "\nDate: " + timeStamp + "\nPassword: " + password + "\n\n"
    # Encrypt the message and store in variable
    encryptedMessage = cipher.encrypt(message, 5)
    decryptedMessage = cipher.decrypt(encryptedMessage, 5)
    print(decryptedMessage)
    file = open('passwords.txt', 'a')
    # Write the ecrypted message into the file.
    file.write(encryptedMessage)
    file.close()
    password = ""

def decryptFile():
    with open('passwords.txt', 'r') as file:
        data = file.read()
    file.close()
    decoded = cipher.decrypt(data,5)
    temp = open('tmp.txt', 'w')
    temp.write("YOU HAVE 15 SECONDS. \nBURN AFTER READING")
    temp.write(decoded)
    temp.close()
    webbrowser.open('tmp.txt')
    time.sleep(15)
    os.system('taskkill /im notepad.exe /f')
    os.remove('tmp.txt')

# Try to add these to the grid at proper locations
passwordLabel = Label(tk, text="")
passwordValue = Text(tk, height=1, width=54)
generateBtn = Button(tk, command = generate, text="Generate")
generateBtn.grid(row=3, column=1)

decryptBtn = Button(tk, command = decryptFile, text="Decrypt")
decryptBtn.grid(sticky=W, row=3, column=1)
# Try to add these to the grid at proper locations
passwordLabel.grid(sticky=W, row=2, column=0)
passwordValue.grid(sticky=W, row=2, column=1)

tk.mainloop()
