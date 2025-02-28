'''
                NOTES
----------------------------------------

Below is a rendition of the classic Rock Paper Scissors game.

Remember that Avyan has been learning Python for a while but it's been a LONG time since we've reviewed the basics. 

The idea is that today you can demo the results of the game without showing any of the code.

We want Avyan to do as much heavy lifting as possible. What was told to me is that the father wants our time with Avyan to be FUN but also challenging. I've focused a bit much on the fun part and not challenging Avyan enough so lets try to work that into our approach.

Make sure to ask Avyan a lot of questions about how he thinks things work. Part of the first few sessions are you understanding where he is and where he falls short.
Remember we don't want to tell him how things work unless we HAVE to. This is where I made mistakes.

Avyan can get distracted easily, so remember to gently guide him back on track.
If the "gentle" part doesn't work, you can be more firm with him or ask him how he thinks his parents would react if he wasn't using our time wisely. Normally thats enough to get him back on track.

Whenever he says something like, "I just want to try something", normally he's about to go off track. You can entertain it for maybe 1 min but otherwise we have to be back on track. If he keeps doing it you can ask, "Is this relevant to our lesson? If not, how about we experiment after we're done with the lesson"

----------------------------------------------
               APPROACH
----------------------------------------------
0. Demo the project, ask him to make observations about the output of the game.
   Make sure to touch on how you're telling the game to play again. 
   What happens if you type 'Y', what happens if you type 'yes'
   What happens if you type Rock, or ROCK, or rok
   (We don't do much error checking and that's okay)
 
1. Create a list that holds the robots choices (make sure to ask him how to do it, what kind of data types)

2. How can we randomly choose from a list?
   How can we save their choice for use later?
   
3. Allow the user to enter their choice.
   How do we ask the user for information?
   How do we store that for later use?
   
4. Check who won
   How do we ask questions in our code?
   How would we check if the user chose rock and the bot chose scissors?
   Make the program respond with who won
   
5. After checking each combination of results,
   let's allow the player to play multiple rounds. What do you think we could use to repeat until told not to?
   
6. Tally up who wins

7. Upon termination, print the final results.
   How do we print variables? Do we know of any "fancy" ways of printing data?
   (fstrings are called formatted strings but I call them fancy strings
   however he wants to do it is fine..)

------------------------------------------------
'''

# ------------- CODE ---------------------------

# We will need this in order to choose randomly from a list
import random
# Array that holds the choices our bot will randomly select
choices = ["rock", "paper", "scissors"]

# Keep track of how many times each player has won
playerWins = 0
botWins = 0

playAgain = 'y'
# The game will play until playAgain is anything but the letter 'y' (lowercase)
while playAgain == 'y':
  # Have our bot choose their play
  botChoice = random.choice(choices)
  # Allow the player to give their choice
  playerChoice = input("\nRock, paper or scissors? ").lower() # convert to lower for easy comparisons later
  # Inform the user of what the bot chose
  print(f"\nBot chose {botChoice}\n")
  # Check each combination of outcomes
  # Print results and record the scores
  if playerChoice == "rock":
    if botChoice == "paper":
      print("Bot wins")
      botWins += 1
    elif botChoice == "scissors":
      print("Player wins!")
      playerWins += 1
    else: # Bot must have chosen rock as well
      print("Tie")
  elif playerChoice == "paper":
    if botChoice == "scissors":
      print("Bot wins")
      botWins += 1
    elif botChoice == "rock":
      print("Player wins!")
      playerWins += 1
    else:
      print("Tie")
  elif playerChoice == "scissors":
    if botChoice == "rock":
      print("Bot wins")
      botWins += 1
    elif botChoice == "paper":
      print("Player wins!")
      playerWins += 1
    else: 
      print("Tie")
  # Allow the user to play again if they'd like, covert to lower case for while loop condition
  playAgain = input("\nWould you like to play again? (y/n) ").lower()

# Print final game scores
print("\nGame over.\n")
print(f"You won {playerWins} time(s)")
print(f"Bot won {botWins} time(s)")


# /----------------- CODE -------------------\