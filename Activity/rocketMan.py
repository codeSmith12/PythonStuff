import random

# Scroll much further down for the actual code I can clean later :D

def updateDashes(secret, dashes, letter): # Create a function that takes 3 inputs
  dashes = list(dashes)                   # Convert dashes to a list
  for i in range(len(secret)):            # Iterates through each letter
    if letter == secret[i]:               # If current letter in secret is == to letter
      dashes[i] = letter                  # Replace dash with letter at that location
  dashes = "".join(dashes)                # Converts back to string.
  return dashes                           # Return dashes as a string


words = ["pizza", "dogs", "cats", "python", "slither","blank", "phone", "enigma", "coding", "problem", "trinket","satisfaction", "onion", "family", "dress", "producer","race", "glass", "quest", "bundle", "sick","elbow", "panel", "employee", "ticket", "fever","garlic", "liver", "chapter", "site", "bike","knee", "strict", "unique", "sailor", "glacier","create", "table", "unlikely", "loser", "winner","proof", "sandwich", "warm", "secret"]

# with open('dictionary.txt') as textFile: # Read in dictionary file
#   lines = [line.rstrip() for line in textFile]


# 

secret = random.choice(words) # was choice(words)
#print secret

dashes = '-' * len(secret)

guesses = [] # <----------

tries = 10

# run loop while I have tries, and while user hasn't guessed the entire word
while tries > 0 and dashes != secret:
  
  print (dashes)
  
  print("\nGuesses: ", guesses, "\n")
  
  letter = input("Guess a letter\n\n")
  
  if len(letter) != 1:
    print("Please enter only one letter.\n")
    
  elif letter in guesses: 
    print("\nLetter already guessed.\n")

  elif letter in secret:
    print("\nYou got one!\n")
    dashes = updateDashes(secret, dashes, letter) 
    guesses.append(letter)
  else: # If they guess wrong
    print("\nTry again.\n")
    tries -= 1 # Decrease tries by 1 
    guesses.append(letter) # <----------
    
  print("You have", tries, "tries.\n")
  
if tries == 0:
  print("Game over. The word was " + secret)
  
elif dashes == secret:
  print("You got it, the word was " + secret)

tries = 1

while dashes != secret and tries > 0:
  letter = input("Please guess a letter")

  if letter in secret:
    print ("You got it!")
  else:
    print ("Wrong!")
    tries = tries - 1 
