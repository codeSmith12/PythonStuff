import random

adjectives = ["Red","Beautiful", "Slow", "Cold", "Flimsy", "Puzzling",
                "Stupendous", "Horrific", "Speckled", "Enigmatic", "Cloudy",
                "Slippery", "Perplexing", "Questionable", "Problematic", "Old", "Pickling"]

nouns = ["Dog","Cat","Bird", "Bug","Wall","Cup", "Lamp", "Mango",
            "Fan", "Shoes", "Pillow", "Books", "Paintings",
            "Mirror", "Keyboard", "Mouse", "Mice", "Moose", "Pickle"]

endNum = random.randint(0,999)
password = random.choice(adjectives) + random.choice(nouns) + str(endNum)
print(password)
