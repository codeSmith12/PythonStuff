import random,time
myHealth = 10
enemyHealth = 10

while myHealth > 0 and enemyHealth > 0:
    myRoll = random.randint(0,6)
    enemyRoll = random.randint(0,6)

    print("\n")
    print(f"Health: {myHealth}")
    print(f"Goblin Health: {enemyHealth}\n")

    print(f"You rolled a {myRoll}")
    time.sleep(1)
    print(f"Goblin rolled a {enemyRoll}")
    time.sleep(1)
    
    if myRoll > enemyRoll:
        damage = myRoll-enemyRoll
        enemyHealth -= damage
        print(f"Goblin hit for {damage}")
    elif myRoll < enemyRoll:
        damage = enemyRoll-myRoll
        myHealth -= damage
        print(f"You were hit for {damage}")
    else:
        print("You both miss")
    print("\n")
    time.sleep(2)

if myHealth > 0:
    print(f"You won with {myHealth} health!")
else:
    print(f"Goblin won with {enemyRoll} health!")
    