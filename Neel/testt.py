import time, playsound
from playsound import playsound
def scrollingText(text):
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        time.sleep(.1)

scrollingText("Hello world. A lnog sentence, lets just see what the timing is like.")
