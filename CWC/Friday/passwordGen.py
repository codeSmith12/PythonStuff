from tkinter import * # Grabbing GUI (Graphic User Interface) building tools
import random, datetime, cypher
tk = Tk() # Creating a TK window, store in variable called tk
tk.geometry("600x300") # Sets the dimensions of the TK window
tk.title("Password Generator") # self explanatory
# "red", "sloppy", "slippery", "tired", beautiful, slow, fast,
adjectives = ["Red","Beautiful", "Slow", "Cold", "Flimsy", "Puzzling",
                "Stupendous", "Horrific", "Speckled", "Enigmatic", "Cloudy",
                "Slippery", "Perplexing", "Questionable", "Problematic", "Old", "Pickling",
                "Rotten"]

nouns = ["Dog","Cat","Bird", "Bug","Wall","Cup", "Lamp", "Mango",
            "Fan", "Shoes", "Pillow", "Books", "Paintings",
            "Mirror",  "Mouse", "Mice", "Moose", "Pickle", "Sandwich", "Problem"]


# GUI == Graphic User Interfaces
titleLabel = Label(tk, text="Title:")
titleLabel.grid(row=0,column=0)
titleValue = Text(tk, height=1, width=54)
titleValue.grid(row=0,column=1)

LengthLabel = Label(tk, text="Length:") # THIS LINE IS INCOMPLETE, FINISH IT YOURSELF :)
LengthLabel.grid(row=1,column=0)                        # PACK
LengthValue = Spinbox(tk, from_= 8, to = 25)
LengthValue.grid(row=1,column=1, sticky=W)                        # PACK

passwordLabel = Label(tk, text="Password") # THIS LINE IS INCOMPLETE, FINISH IT YOURSELF :)
passwordLabel.grid(row=2,column=0)                        # PACK
passwordValue = Text(tk, height=1, width=54)
passwordValue.grid(row=2,column=1)








def generate():
    global password
    endNum = random.randint(0,999)
    password = random.choice(adjectives) + random.choice(nouns) + str(endNum)

    if len(password) < int(LengthValue.get()):
        print("Length not valid, regenerating.")
        password = generate()

    passwordValue.delete("0.-1", END)
    passwordValue.insert(INSERT, password)
    # print(password)
    myFile = open("password.txt", 'a')
    # DATE TIME NEXT SESSION
    today = datetime.date.today()

    passStr = str(today) + "\n" + titleValue.get('1.0', END)  + "\n" + password + "\n"

    encrypted = cypher.encrypt(passStr, 5)
    print(encrypted)

    myFile.write(encrypted)
    myFile.close()

    return password

def decryptFile():
    print("Commensing decyption of file...")
    file = open("password.txt", "r")
    data = file.read()
    data = cypher.decrypt(data, 5)
    print(data)





generateBtn = Button(tk, text="Generate", command=generate)
generateBtn.grid(row=3, column=1, sticky=W)
decryptBtn = Button(tk, text="Decrypt", command=decryptFile)
decryptBtn.grid(row=3, column=1)


                        # ADD TO GRID AT PROPER LOCATION
tk.mainloop()
