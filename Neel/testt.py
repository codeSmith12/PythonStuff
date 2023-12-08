import time
def scrollingText(text):
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        time.sleep(.1)

scrollingText("Hello world. A long sentence, lets just see what the timing is like.")
