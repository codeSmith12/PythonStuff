import time, datetime
# from pydub import AudioSegment
# from pydub.playback import play
# typeWriter = AudioSegment.from_mp3("./typeWriter.mp3")
# play(typeWriter)
# Add typewriter sound when possible...
global scroll # <--
scroll = False # <--

global eyeInjured
eyeInjured = False

def scrollingText(text):
    global scroll # <---
    for i in range(len(text)):
        print(text[i], end="", flush=True)
        if scroll == True: # <--
            time.sleep(.04) # <--

'''
    Text based adventure, plot ideas:

    Unreliable Narrator -> Based on Evil Within, attempt on an insane perspective..
    Can hardly guess what is real...
    Starts of with you dying -> BUT YOU DONT KNOW !!! (6th sense?)
    Start dead, but you don't know. You're looking for your daughter
    Wake up to dark voice in the forest, "you must live you must live"
    Potentially hearing monster marching but its not real.
    Need to have things that aren't real happening before Narrator, in great detail.

    Or clock tower story, bring it back to life.
    Portal from mind projects into the world.

    Second-person Narrator
    Protogonist has died and the 3 endings leave user in limbo, goes to hell or heaven

    CHOICES COULD BE HARD LIKE WALKING DEAD STATUS

    Your past haunts you, if you rectify the mistakes you made in the past, you can get to the good ending.

    In an argument you pushed your friend off the second floor of the barn, he broke his arm and was never

    able to play football, which he admitted was always his dream to do.

    Start mashing current events with childhood to remove ideas of reality

    Parallels between your childhood and the one your producing for your child.

    Lucid dreaming, maybe eventually gain control of the dream.

    IDEA: Get to the very end, if you try to escape your regrets, you get placed back at the beginning
    If you choose to let the monster get you, you accept yourself and go to heaven or something


    ** FINISHING TOUCHES **
    Play sounds at certain times to help complete the feel of the environment
    A function that displays these long strings, but letter by letter, or word by word...



    Ideas for things you did to wrong people that you regret:

    Pushed your friend & they broke their arm (Maybe they ended up dying in the army?)

    Broke into a candy shop for candy, but also stole the money forcing the candy shop to close,
    Employees are also coming out like zombies and grabbing you
    setting is much darker(evil), with all kinds of kids toys that now look demonic

    Beat up some kid to take their money, or bike?

    Your crush denied (Was watching a movie at her house, you asked her out)
        you and you took revenge by spreading rumors about her, anonymously


        IDEAS FOR FINAL SCENE:




    Locations character will visit: (Teleporting to parts of your childhood...)
    Forest, barn, a candy shop you broke the window, alley way,


'''



def intro():
    scrollingText("""
"Wake up Daddy.", you hear your daughter saying softly.
You jolt awake to find yourself in a dense forest, in the middle of a halo of mushrooms.
"Sarah, where are you!?" you call out, to no reply. The silence is so loud,
your ears begin to ring. In a daze, you look around, trying to soak in your surroundings.
"Where am I, for that matter?". This forest is unfamiliar, dark and foreboding.
Not like the one you grew up in. You see a bright flash in the sky, almost as if a star exploded.
It illuminates the path forward, through the thicket and to a barn nearby. As you walk forward,
a rumble ripples through the trees. You hear something massive approaching. You quicken your pace to
put distance between you and this mysterious entity. As you near the barn, your eyes begin to focus.
You can see this barn is in disrepair, however, something is oddly familiar about it.
The loud footsteps of the encroaching monster become closer and closer. You choose to:

A) Hide behind the barn
B) Hide inside the barn

""")
    barn = input()

    if barn.upper() == "A":
        hideBehindBarn()
    elif barn.upper() == "B":
        hideInBarn()
    else:
        print("Wrong entry, you die...")

def hideBehindBarn():
    scrollingText("""
You scurry to the back of the barn and see some rusty farming equiptment.
You hide underneath an old tractor that looks as if it hasn't been used in decades.

The monster stomps around you, sniffing the air. You hear a crunch and the groan of metal as the collassal figure
picks up the tractor you're hiding under. Effortly it tosses the hunk of metal to the side and grabs you.
You feel your insides begin to burst as the giant squeezes you. You hear popping sounds as everything turns black.
The next thing you see is fire surrounding you and nothing but crimson. You have died.

""")

def hideInBarn():
    scrollingText("""
You burst through the double door of the barn, latching it shut behind you.
"Hopefully that thing won't find me in here." you think to yourself. Panting
from the excertion, you look around the room. You've find that you've entered
your families old barn you used to play in years ago as a child. You see the hay bales you
used to jump from, the gates you used to swing from and the poles you used to climb.

Across the room from you, you see there's a door to the outside. You look up and
notice there's a small dark figure on the second floor. You choose to:

A) Take the backdoor to outside the barn
B) Go upstairs to the dark figure

""")

    barnChoice = input()
    if barnChoice.upper() == "A":
        hideBehindBarn() # Added to cut lose end, reused from the choice before.
    elif barnChoice.upper() == "B":
        goUpstairsToFigure()
    else:
        print("Wrong entry, you die...")

def goUpstairsToFigure():
    scrollingText("""
You make your way upstairs, begrudgingly. The boards creak with each step you take. You see
that the figure is clutching their arm, which appears to be bent backward in a
way that doesn't look natural. As you reach the top of the stairs, you find yourself looking into the smoldering eyes
of your childhood friend, Ben. The hatred on his face makes you recoil. "Here to finish the job?",
he asks. You know immediately what he's referring to. You recall that moment, when you
pushed him off of this very floor of the barn, where he fell down onto the ground with a loud crack.
His forearm snapped, bent backwards towards his shoulder(Put more detail about the arm).
You remember the sounds of his screams, the blood gushing from his arm.
You remember the remorse you felt when you heard about how Ben's arm would never heal the same.
How his scholarship and future had shattered with his arm. You invision the moment
that you found out about his death. Gripping the obituary, white knuckled, knowing
that you caused him to give up his football dreams and join the army.

He had nothing left. All because of you.

You begin to feel sick to your stomach, just the same as you did when you first found out.

You choose to:
A) Reach out to your friend Ben
B) Listen to what Ben has to say""")

    benChoice = input()
    if benChoice.upper() == 'A':
        scrollingText("""
"I'm so sorry..", you plead. As you reach towards him, he disolves into a black smokey wisp.
The smoke pours through your fingers, and you hear the shriek that Ben gave out long ago when
everything he had going for him came falling down.""")

    elif benChoice.upper() == 'B':
        scrollingText("""
 Ben began to speak, "You know, you were my best friend. I always admired how little you cared for
 the rules, not like me. I always did what my parents told me.
 Go to practice and you'll achieve your dreams, they said.. little did they know..", he scoffed.
 "Too bad I had no idea that your love for rule breaking would result in me suffering for the rest of my life.
 After the incident, everything I had worked for was taken from me. When the doctors told me I'd never
 be able to throw again, I was devestated. My scholarship to play in college was rescended. My girlfriend left me,
 as I was now a disfigured man. I was forced to sell my life to the army, as it wasn't much good to anyone else..

 You wanna know how it happened? How I died? I was in combat, hiding behind cover. Afraid for my life. Wishing that
 things just could have been different. That's when I hear it. A grenade landed to my right.
 I tried to pick it up to toss it back, however, my crippled arm, thanks to you, failed me.
 The grenade blew up in my hand, and now I'm here...

 I hope you rot for the things you did to me."

 "I'm so sorry Ben..", you begin to appologize. However, as you do, Ben dissolves away into a black smoke.
 You grasp at the smoke, but it slides through your fingers. "What have I done.." """)



    scrollingText("""
You fall to the floor and curl into a ball, wishing yourself to be anywhere but here.
"Why is this happening to me?!" you shout.

The monster begins to come towards the barn, you hear the stomps getting louder.
It begins to smash on the double doors of the barn. You can see the latch is barely holding on,
the door is cracking at the seams.

You choose to:
A) Hide in the top floor of the barn
B) Drop out of the window

""")

    barnChoice = input()
    if barnChoice.upper() == "A":
        pass
    elif barnChoice.upper() == "B":
        candyShop()

def candyShop():
    scrollingText("""
You rush across the rafts to an open window you see. You peer down, and only see darkness.
Knowing that there's no other way, you hop out of the window and brace for the ground.
However, you don't stop falling. Your insides turn upside down as you fall
through pitch black nothingness. You can feel wind blowing on your face,
that you're rotating in a freefall, but where is the ground?! Suddenly,
you SLAM down on something hard, knocking the wind out of you.

You roll to your side with a groan and sit up. You rub your eyes to help focus, your head is spinning.
As focus on your surroundings, you hear a music box playing somewhere near you.
You recognize the sound. It reminds you of blissful memories with your mother
when she took you to your favorite candy shop. You look around and see that
you're in the very same one. The shop has seen better days. The ceiling is sunken in,
and there's dust covering every surface. As you regain your footing, the wooden floorboards
creak and squeel as you shift your weight.

You look around at the sad husk of the candy store that you once knew and loved and felt a pang of guilt.
You didn't mean to do it. It wasn't your fault that the door was left unlocked.
You had suffered an entire week of school, AND did a handful of chores to scrape up enough,
for that mouth watering salt-water toffee.
You deserved it; and so you would get it. It just so happened that the cash register was open.
The money laid before you was so tantilizing.

You "reminded" yourself of how last Christmas your sister was so disappointed when she received "such few gifts".
You thought of the Poly Pocket that she always wanted but your parents could never afford. So you took the money.
Little did you know, the candy shop had not been profitable for a while, and this would be the straw that broke the camels back..
The owner was forced to close down the shop.

You notice that all of the toys on the shelves turn their heads towards you as you walk around the room.
The murderous stares unmoving as they pierce into your heart. Strangely, they have sharpened candy canes and toy swords.
You hear a clang and twirl around as a toy has fallen off the shelf.

You choose to:
A) Inspect the toy
B) Move to the back of the store

""")
    candyShop = input()
    if candyShop.upper() == "A":
        towardsToy()
    elif candyShop.upper() == "B":
        goToBackOfStore() # Survive without injury

def towardsToy():
    global scroll, eyeInjured
    scrollingText("""
As you move towards the fallen toy, **THUD** another toy falls off the shelf, **THUD** then another.
The floorboards begin to rumble as all of the toys seem to animate and come to life.
The sounds of the music box begin to blare as they walk slowly towards you, weapons drawn.
In a split second, one of them has thrown a candy cane at you.

Quickly, you must make a choice, either you...
A) Roll to the side
B) Guard your face with your hand

    """)
    # timed choice, so if they take too long, they die via suffication
    startTime = time.time()
    toyChoice = input()
    endTime  = time.time()
    timeTaken = endTime - startTime

    if not scroll:
        timeTaken -= 12

    if timeTaken < 5: # if they responded in the correct amount of time.
        if toyChoice.upper() == "A": # Escape with a stab in the back, all good
            rollOver() # Roll to your side
        elif toyChoice.upper() == "B": # Get hurt in the eye
            raiseHand() # Put hand up
            eyeInjured = True
    else:
        print("""
As you stand there contemplating your choices, the toys begin to pile up on top of you.
You flail your arms in an attempt to break free, but they just keep coming.
As you tire, you can feel tiny pricks of candy canes going through your body.
The music box fades into the background as everything goes dark and silent.
        """)

def rollOver():
    print("""
You roll to your side, and cover the back of your neck. During this action, a sudden snap erupts.
You can see a razor-sharp candycane lodged in between your arm and your torso, narrowly missing your heart.
You get up from the attack and run towards the storage room as fast as your legs can carry you and slam the door.
    """)
    enterStorageRoom()

def raiseHand():
    print("""
You raise your hand close to your face in order to defend yourself from the incoming candied projectiles.
Suddenly, you see a flash of red. You pull your hand away, blood is pouring from your face
and there's a candycane stuck in your left hand. Looking around at all the advancing toys,
you notice you can only see from your right eye. You get up and sprint towards the
storage room before they can do any more damage, and slam the door shut behind you.
    """)
    enterStorageRoom()

def goToBackOfStore():
    print("""
As time was running out you sprint toward the door to the storage room you and
everything around you seems to be moving in slow motion. The toys create a murderous trail of havoc
as you come to the dark realization that they are catching up.
Using your last bit of strength, you make a massive leap towards the door and barely get into it as you slam the door shut.
""")
    enterStorageRoom()

def enterStorageRoom(): # Transition to the family home.
    print("""
The door begins to budge as the toys smash on it from the other side.
Your fingers fumble over the lock as you frantically bolt the door closed to buy you some time.
As you peer around, you see there's a familiar teddy bear sitting on a cardboard box. It's the same one
you got your daughter for her 4th birthday. You remember being so proud that you were able to get
her all the toys you wish you had as a child. You reach for it, and as you touch it you feel your world begin to spin.
The incandescent bulb hanging from the ceiling whirls around you, becoming greater and greater in it's brightness.
Blinded and disoriented, you stumble to the floor.
""")
    oldHouse()

def oldHouse():
    print("""
As you pick yourself up, you notice the floorboards that you and your ex-wife
installed in the house that you used to live together in. Except this time, they're huge.
The ceiling of the house seems to be hundreds of feet above you, and all of your old furniture is gigantic.
You feel as though you are Jack in the giants house. On the walls hang pictures of your family united.
The memories of the past, Christmas's, birthdays, all displayed on the walls. The happy family you once had,
before the gambling addiction took ahold of you.

The ground begins to rumble, similar to the time in the forest. From aroud the corner turns the "monster".
It's your ex-wife Jennifer, except it's not. She appears to have strings
attached to her back and all of her limbs. Her face is ghastly and doll-like, made of white porcelain.
The imposter is holding a gavel in it's hand.

The creature spoke, "You forgot to pick up Sarah. Let me guess, gambling again?"
You can see the strings pulling away at her legs and mouth
as she walks towards you.

"No, I was just out shopping"(Could make choice to lie or be honest), you begin to make up excuses, just like you did
the last time you had this conversation. "LIAR!", she screams. She begins to convulse, becoming
angered with your response. She quickly strides over, towering over you. In the blink of an eye,
she raises her arm, preparing to strike down.""")

    run = input("""
You choose to:
    A) Hide under furniture
    B) Hide in your daughters doll house
""")
    if run.upper() == "A":
        hideUnderFurniture()
    elif run.upper() == "B":
        dollHouse()

def hideUnderFurniture():
    print("""
Adrenaline begins to flow as you dive under a nearby couch. You tuck yourself into the
back corner by one of the legs of the couch. You see the monsters face emerge as
it tries to reach you. It can't seem to reach you with it's hand as it grabs at you.
After fruitless attempts, it takes the gavel and begins to slam it, getting closer with each hit.
*bang* *Bang* *BANG* She becomes furious that she can't reach you and gets up off the floor.

"If you don't want to talk, then I'll make you scream!" smashing the gavel on the ground.
The impact was tremendous, sending everything on the ground flying upward, including you.
As you decend and brace for impact, you force your eyes shut. You hit the ground with a thud,
and open your eyes.
""")
    if eyeInjured:
        courtHouseEyeInjured()
    else: # eyes are fine,
        courtHouseNonInjured()

def dollHouse():
    print("""
With you heart beating out of your chest, you run towards the doll house you got
your daughter for her 4th birthday. You open the plastic door and hide in one of the rooms.

The monster gives a gruesome laugh, "Oh, so now you want to play with your daughter?"
She swings the gavel down hard, **SMASH** The dollhouse breaks open, showering you with debris and
exposing you to the monster.

She swings down one last time with force. You feel the crunch of bones and everything
starts ringing. You lie there with shattered limbs, unable to move or talk. The world fades away.
You have died...
""")
    checkPoint = input("Would you like to try again? Y/N")
    if checkPoint.upper() == "Y":
        oldHouse()

def courtHouseEyeInjured():
    print("""
Blackspots begin to pulsate on the left side of your vision. You dab your eye with the
back of your hand and find its still bleeding from the attack at the candy shop.
    """)
    courtHouse()
def courtHouseNonInjured():
    print("""
You awaken to the echo of a gavel banging. Light begins to pour into your eyes, and
you realize you're in the place where your divorce was finalized. The courthouse where
you lost everything.( The sound of the gavel still haunts you.)
""")
    courtHouse()

def courtHouse():
    print("""
"Sleeping in my court? You must really not want custody of your child."
"No, your Honor I-", you begin.
"Upon review of this case, both of the biological parents of Sarah are deemed unworthy of
custody due to mental instability and a criminal record."
The judge strikes the gavel releasing a flash, which rings through the court with a booming echo.
In a glimpse, you see the silhoette of a figure holding a gavel similar to that of the judges.
Suddenly, the ringing stops as you see Jennifer in the middle of the courtroom. The judge
is gone. It's just you and the impersonator.

"Stealing from a candy shop? How low can you be? You caused that poor man to
close down his shop. Think of all the memories you had there with your mother.
Now no one can have any memories like that again." """)
    torment1 = input("You begin to say... ")
    print("\n" + torment1[0:7] + ".. the monster interrupts.")
    print("""
"Every night you were out gambling, you thought you'd be winning big..
but instead you lost your family." It laughs, appearing to relish in your torment.

"How could you live with yourself, knowing that you've killed your friend?
Maybe you haven't been living at all. That's why you want to drown your sorrows
with 'winning big'."
    """)
    consoleExplain = input("""
You choose to:
    A) Console Jennifer
    B) Explain yourself
""")
    if consoleExplain.upper() == "A":
        console()
    elif consoleExplain.upper() == "B":
        explain()
def console():
    print("""


    """)
def explain():
    print("""
'I've been very troubled.. for most of my life.'

'I stole from the candy shop because I wanted to get my sister the presents
my parents were too poor to get themselves. I was tired of eating potatoes and rice,
barely scraping by. I wanted to have nice things like the other kids. After finding
out that the shop closed, due to my actions, I was fraught with guilt. My parents
never looked at me the same when I told them what I had done.
From there on, I was only a disappointment to them. So I started to lash out.'

'I broke my best friends arm. We were in an argument in the barn, I got angry and so
I pushed him. I had no intention of breaking his arm, but, solving problems with violence
was what my dad taught me, so that's what I did. '

*** Elaborate more on feelings after arm break and eventual casualty
** Then gambling addiction

I thought that through gambling, I'd be able
to provide for my family in ways my parents never were able to before.'
    """)
"""
Courtroom Game Dynamics:
    What choices:
        Console or explain yourself(end up aggervating)
            -Console: Console your angry wife, MAYBE she stops being aggressive...
                or is less aggressive in next scene ?
            -Explain: Explain that you've been trouble, thought money would help the family.
                Makes her more angry perhaps ?

        Work in the eye injury some how - vision progressively receeds, timed
        Body systems progressively failing, hearing going out, sight, dizziness




Wifes backstory:

Due to her wanting a divorce because of the gambling and inattentiveness,
She ends up losing her child because she's deemed not mentally fit.

Stress of the divorce made her snap. During the divorce process, you moved out,
she tried to burn down you complex ??? For ruining her perfect life ?



1. Stealing from candy shop -> shop closure.
2. Breaking friends arm -> his death :(
3. Gambling -> losing family


Perhaps have a scene where you're at the casino, which is where a lot of the
problems have come from...



Maybe you explain about how you thought you were gonna win big but instead lost a lot
and thats why you didn't pick up Sarah

"""

"""
Project Ideas:
1. Wordle
2. Blackjack
5. Snake
6. Space invader
7. Pac Man
"""

# ** BEgin the boss fight on the gavel ringing .... Something like that..**
# Appears with gavel strike
# Child will be in an orphanage after this...


"""
    1. Youre the one divorcing, this is why exwife goes crazy... (Maybe you gain custody, or maybe neither)
    2. Shes divorcing you, You wake up (judge makes a comment about you sleeping in court because you dont care)
       Courthouse is when everything was taken from you. Why it's a pivotal place in your life..


       *******
       the final location we teleport to is the instance that you died,
       which lead us onto this adventure in the first place, (in the life between death)
       ********

    NOTE CONTINUE AFTER DEATH: Just call the function that was used last to allow the user to try again,
                                without having to start all the way at the beginning


    1. Something with family, with ex-wife, divorced, is massive, doll-themed, Ventriloquist
        How have you wronged this wife? :
        Abandoned your family : -> why?
        wife threatening to use the money
        in "bad ways" -> Both parents unfit to gain custody of Sarah,
                        You're unfit due to your history of crime...
                        OR just because you ran away from the family to start a newlife due to toxic wife?
                        Maybe you tried to fight for custody, but due to your past history, you were denied.
                        Mom is unfit because threats, and tries to burn down your apartment,
                        only to learn that you had moved, but it resulted in multiple deaths...

                        Doll is wielding a GAVEL, Gavel when slammed it CHANGES LOCATIONS!!!

                        Location ideas:
                        your house that you lived in with the wife, Court house, the burned down apartment

                        Puppet master has been yourself the whole time.
                        You've been the one destroying yourself the whole time.

                        Old house description:
                        Youre tiny, everything around you seems so enlarged. (2 inches tall)
                        hear stomping, just like at the beginning
                        Family photos

                        Wife's conversation:
                            - you forgot to pick up your daughter from school.
                            -> was really late when daughter got back by walking home, she was scared







"""

def main():
    global scroll
    scrollInput = input("Would you like scrolling text? (y/n)")
    if scrollInput.lower() == "y" or scrollInput.lower() == "yes":
        scroll = True

    # courtHouse()
    intro()


main()
