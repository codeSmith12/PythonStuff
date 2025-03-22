import random,time
# AUTO REMOVE CHOSEN ITEM, LOOP ONCE ENTER IS PRESSED
presenters = ["Group 1", "Group 2", "Group 3", "Group 4"]
from pathlib import Path
from playsound import playsound

SCRIPT_DIR = Path(__file__).parent
TIC = SCRIPT_DIR / 'TIC3.wav'


SPEED_FACTOR = 100

while len(presenters) > 0:
    NUM_SPINS = random.randint(25,50)
    chosenOne = ""
    for i in range(NUM_SPINS):
        if i == NUM_SPINS-1:
            time.sleep(1.5)
            chosenOne = random.choice(presenters)
        else:
            time.sleep(i/SPEED_FACTOR)
            chosenOne = random.choice(presenters)
        print(f"\n{chosenOne}")
        playsound(str(TIC))
        
    
    print(f"\nThe next presenter will be {chosenOne}!!!")
    presenters.remove(chosenOne)
    input("\nPress enter to continue...")