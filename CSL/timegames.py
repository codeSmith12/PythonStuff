import random, time

timeGame = False
reactionGame = True

if timeGame:
    
    target_time = random.randint(2,10)
    
    print(f"Your target time is {target_time} seconds.")
    
    input("Press enter to start your timer.")
    start_time = time.time()
    
    input("Press enter again to stop the timer.")
    elapsed_time = time.time() - start_time
    
    difference = abs(target_time - elapsed_time)    
    print(f"You were {difference:.2f} seconds off from {target_time}!")
    
elif reactionGame:
    
    print("Welcome to the reaction time game!")
    print("You will be tested 5 times.")
    print("Press Enter as soon as you see the word, 'NOW!'")
    average_time = 0

    for i in range(5):

        time.sleep(random.randint(2,5))

        start_time = time.time()
        input("NOW! Press Enter!\n")
        end_time = time.time()
        reaction_time = end_time - start_time
        print(f"It took you {reaction_time:.3f} seconds to react!\n")

        average_time += reaction_time

    print(f"Your average reaction time was {average_time/5:.3f}\n")
