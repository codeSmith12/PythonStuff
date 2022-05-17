import time

# ToDo:

# A few more loose ends on the choices

# Maybe put a use for the moon key here, to get secret item for win at the end? I think the option for the win will only show up if you get the item from the tree room.

# Maybe make F2 more explorable, with only 1 choice per set that allows user to live and explore more ? Maybe F2 will have the item... Barry's Magnum??

# Maybe moon room won't be fatal if you pull some level outside of the room before entering?


answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]
inventory = []
treeDoorUnlocked = 0 # Doesn't work, need to find out how to work with
 # variables and functions.
trapSet = True

def enter():
  print("\n\nEnter the survival horror...\n")

  print("""\nYou wake up on the floor of a large sprawling hallway.
  The floors are made of white marble, with old dusty rugs scattered on the floor.
  'Where am I?' you ask yourself. As you walk through the hallway, you get a glimpse outside of a window.
  Your vision is obscurred by overgrown bushes, but it appears you are on the second floor of a large mansion.
  You continue down the hall, passing by grand, artisticly crafted wooden doors.
  You hear slow, dull footsteps behind you. You quicken your stride to put some distance between you and this unknown entity.
  You reach a stairway..

  You have the choice to...
  A: go down stairs
  B: go up stairs
  C: stay on this floor.

  Which do you choose?\n""")

  choice = input(">>>")

  if choice in answer_A:
    stairsDownF1()
  elif choice in answer_B:
    stairsUpF3()
  elif choice in answer_C:
    stayOnF2()




def stairsDownF1():
  print("""\nYou shuffle down the rickety spiral staircase and find yourself in a expansive room filled with medieval objects.
  A mural of angels stretch across the high ceilings. Their faces appear to be sad, and they all seem to be watching you.
  You scan the room in front of you and see a large set of double doors. 'The way out!', you exclaim, as you run towards the door.
  You throw the latch open in attempt to open the door, however it won't budge. 'Of course... That would have been too easy...', you think to yourself.
  You face the stairset, perplexed. To the left of the stairset, you see a small door with a tree etched into the frame.
  To the right of the stairset, you see a large door with a moon welded into the metal frame.
  Where do you go?\n
  A: tree door
  B: moon door
  C: back upstairs

  """)
  choice = input(">>>")

  if choice in answer_A:
    if "Tree Key" in inventory:# or treeDoorUnlocked == 1:
      #inventory.remove("Tree Key")
      #treeDoorUnlocked = 1
      treeRoom()
    else:
      print("It's locked. Maybe there's a key somewhere?")
      stairsDownF1()
  elif choice in answer_B:
    if "Moon Key" in inventory:
      inventory.remove("Moon Key")
      moonRoom()
    else:
      print("It's locked. Maybe there's a key somewhere?")
      stairsDownF1()
  elif choice in answer_C:
    stairsUpF3() # This is where we explore the tree room.

  elif choice in answer_C:
    stairsUpF3()

def inspectTree():
  print("""You reach your hand inside the knotthole. You pull out a golden medalion with a wolf on it.\n""")
  print("You have picked up the Wolf Medalion.")
  inventory.append("Wolf Medalion")
  print("Inventory: ", inventory)
  treeRoom()

def treeRoomInspect():
  print("""\nYou walk around the tree at the center of the room. You notice a small decorated box with a moon symbol on it. \n""")
  if "Moon Key" in inventory:
    print("You use the Moon Key to unlock it. Out of it, you pull a revolver. 'Finally, something to protect myself...'\n")
    inventory.append("Revolver")
    print("\nInventory: ", inventory, "\n")
  treeRoom()


def treeRoom():
  print("""You use the Tree Key. The door unlocks but the key breaks in the process. You enter into a room with a tree growing in the middle of it.
  As you peer around, you see something shining in a knotthole in the tree.

  Do you:

  A: Inspect the tree
  B: Leave this room
  C: Walk around room
  """)

  choice = input(">>>")

  if choice in answer_A:
    inspectTree()
  elif choice in answer_B:
    stairsDownF1()
  elif choice in answer_C:
    treeRoomInspect()

def moonRoom():
  print("""You use the Moon Key. The door unlocks. You enter into a room with pipes coming from the ceiling.
  The door slams shut behind you. You try your hardest to turn the handle but it's stuck shut.
  Water begins to pour from the pipes above. You do your best to stay afloat, but the room is almost entirely full.
  You take your last few gulps of air, however it is futile. Everything goes black. You have died.""")


def stairsUpF3():
  print(""" The stairs creak as you ascend. At the top of the stairs, you find yourself in another hallway that looked almost identical to the one you just came from.
  'Great..', you say sarcastically. Below you, the steps continue.
  What ever's down there, it doesn't seem to want to come up to this floor.
  You continue to explore the hallway. You find a fancy looking coffee table that has two urns on it.
  One with a tree symbol and one with a moon symbol. Hanging above the coffee table is a poem.
  It reads, "Under the moon, oceans swell. Under the tree, life flourishes."

  What do you do?

  A: Smash the tree urn
  B: Smash the moon urn
  C: Continue exploring

  """)

  choice = input(">>>")

  if choice in answer_A:
    if "Tree Key" in inventory:
      print ("You've already grabbed the Tree Key.")
    else:
      treeUrn()

  elif choice in answer_B:
    if "Moon Key" in inventory:
      print("You've already grabbed the Moon Key.")
    else:
      moonUrn()

  elif choice in answer_C:
    exploreF3()

def escape():
  print("""You climb down the ladder, and find yourself in the woods. You run as fast as you can, anywhere that isn't here.
  After running for what felt like hours, you stop to catch your breath.
  You sit on a log to regain some composure and process what just happened. You look up at the moon, it shines bright.
  Suddenly, out from a bush near by, the creature that was stalking you emerges.
  You let out a scream that you never thought possible.""")

  if "Revolver" in inventory: # Cold metal, steel, feels powerful
    print("""You pull out the revolver you picked up in the mansion. You point it in the direction of the encroaching monster and squeeze the trigger.
    *BANG* The monster recoils, clutching it's side. It slowly gets back to it's feet and begins to walk towards you again, arms stretched out.
    One more time, you squint down the sight and pull the trigger. The bullet flies right into the head of the monster.
    Only what could be described as confetti explodes out of the monsters head.
    As it collapses, you finally feel the sense of dread has lifted.
    You sit back down on the log under the tree. """)

  else:
    print("'If only I had something to protect myself!', you scream in your head. You sit there, paralysed by fear. The monster comes closer and closer, until you are face to face. You have died...")


def useMedalion():
  print("""\nYou place the Wolf Medalion into the indentation with a click, and push open the door.
  The wind whips your face, the cool, fresh air dances around you.
  You never thought you'd feel this excited to be out on a windy day at night.
  You see the ladder in front of you.

  Do you:

  A: Climb down the ladder
  B: Go back inside
  """)
  choice = input(">>>")

  if choice in answer_A:
    escape()
  elif choice in answer_B:
    print("Reluctantly, you turn around and go back inside. 'Why am I doing this?'")
    stairsUpF3()

def lowArrowJump():
  print("""You quickly get to your feet and jump over the low flying arrow.
  It grazes your pant leg, but you are otherwise unharmed. 'I really have to be more careful in this place...' you say to yourself.
  You cautiously walk to the end of the hall to find another door.
  The door has a window next to it where you can see a ladder that decends to the first floor outside of the mansion.
  'There is hope!', you cheer internally.
  As you approach the door, you see that instead of having a door knob, there's an circular indentation.

  Do you:

  A: Try to push open the door
  B: Use an item
  C: Turn back around

  """)
  choice = input(">>>")

  if choice in answer_A:
    print("""You push on the door, it won't budge. 'I wonder if it has to do with this weird indentation?' You head back in hopes to find something important.\n""")
    stairsUpF3()
  elif choice in answer_B:
    print("""\nYou check what items you have picked up from your time in the mansion: """)
    print (inventory)
    choice = input("\nWhich item would you like to use?\n")
    if choice.lower() == 'wolf medalion' and 'Wolf Medalion' in inventory:
      useMedalion()
    else:
      print (choice, "doesn't seem to work here. Let's go back and explore.\n")
      stairsUpF3()
  elif choice in answer_C:
    print ("You turn back around.\n")
    stairsUpF3()
  # Take input, pushing door doesn't work, item only works if medalion in inventory, turn back around puts you at F3 urns
def lowArrowDuck():
  print("""Already crouching from ducking earlier, you attempt to get even lower. Despite your best efforts, you catch the arrow straight between the eyes. You have died.""")
def highArrowJump():
  print("""You attempt to jump over the arrow, however, the arrow sinks right into your belly. You lay on the ground in agony. You have died.""")

def highArrowDuck():
  print("""You duck under the arrow. 'Phew', you sigh in relief. Just as you do, you hear a second whoosh. Another arrow is coming right towards you, knee level.
  Do you:

  A: duck
  B: jump

  """)

  start = time.time()
  choice = input(">>>")
  end = time.time()
  duration = end-start

  if duration > 10:
    print("""You took too long to decide and took an arrow to the knee. You hobble around, doing your best to not put pressure on your wounded knee. You collapse against the wall. You have died.""")
  elif choice in answer_A:
    lowArrowDuck()
  elif choice in answer_B:
    lowArrowJump()

def exploreF3():
  print("""You walk around the other side of the hallway.
  Midway through the hallway, you step on a marble piece that receeds into the ground with a click.
  You turn towards a wooshing sound and see an arrow flying right towards your chest.

  Do you:

  A: jump
  B: duck

  """)

  start = time.time()
  choice = input(">>>")
  end = time.time()
  duration = end-start

  if duration > 10:
    print("""You took too long to decide and took an arrow to the chest. You have died.""")
  elif choice in answer_A:
      highArrowJump()
  elif choice in answer_B:
      highArrowDuck()

def attackF2():
  print("""You swing your hardest at the head of the creature. It catches your feeble punch and strikes you down..

  You have died.""")

def runF2():
  print("""You see a slight opening to the creatures left side. You make a break for it, however, you clumsily fall. The creature has you in it's grip.

  You have died.""")
def screamF2():
  print("""You continue to shriek. Your throat feels like it's about to burst. And it does. The monster slashes through your throat and warm blood begins to pour from your wound.

  You have died. """)

def treeUrn():
  print("""You pick up the tree urn to throw it, and you hear a metal tinging inside.
  You turn it over and out comes a key with a tree on it.
  You take the key and place the urn back.""")

  if "Tree Key" not in inventory:
    inventory.append("Tree Key")
    print("Inventory: ", inventory)
  print("""\nYou go back down to the first floor.""")
  stairsDownF1()



def moonUrn():
  print("""You pick up the moon urn to throw it, and you hear a metal tinging inside.
  You turn it over and out comes a key with a moon on it.
  You take the key and place the urn back.""")

  if "Moon Key" not in inventory:
    inventory.append("Moon Key")
    print("Inventory: ", inventory)
  print("""You go back down to the first floor.""")
  stairsDownF1()

def stayOnF2():
  print("""\nDespite the pit in your stomach, you decide to stay on this floor. You continue to explore through the hallway, checking each door that you pass by.
  You reach a door at the end of the hallway. You try the handle. *click* The door opens.
  As you shut the door, you see a dark hooded figure rounding the corner, slowly walking towards you. *thump... thump... thump...*
  Frantically, you search your room for an exit. You see a small window welded with metal bars.
  You shake the bars with all of your might. 'OPEN UP PLEASE!!!' To no avail. *Thump.. thump... thump...*
  The footsteps are at the door. You see the shadow at the base. *WHACK* The door flies open, the monster walks in.
  You scream, but no one can hear you, for you are alone with this monster. Your fight or flight response kicks in.

  Do you:
  
  A: Fight back
  B: Try to run by
  C: Continue to shriek in terror
  """)
  choice = input(">>>")

  if choice in answer_A:
    attackF2()
  elif choice in answer_B:
    runF2()
  elif choice in answer_C:
    screamF2()

enter()
