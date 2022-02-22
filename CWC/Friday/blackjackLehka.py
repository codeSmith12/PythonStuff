import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def display(self):
        if self.num <= 10:
            print(f"{self.num} of {self.suit}")
        elif self.num == 11:
            print(f"Jack of {self.suit}")
        elif self.num == 12:
            print(f"Queen of {self.suit}")
        elif self.num == 13:
            print(f"King of {self.suit}")

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def addCard(self, card):
        self.hand.append(card)

    def showHand(self):
        for card in self.hand:
            card.display()

class Deck:
    def __init__(self):
        self.cards = []
        # Create every card, and add it to the deck
        for i in range(1,14):
            self.addCard(Card(i, "Hearts"))
            self.addCard(Card(i, "Diamonds"))
            self.addCard(Card(i, "Clubs"))
            self.addCard(Card(i, "Spades"))

    def addCard(self, card):
        self.cards.append(card)

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def displayDeck(self):
        for card in self.cards:
            card.display()
    def dealCards(self, players):
        for player in players:
            player.addCard(self.cards.pop())
            player.addCard(self.cards.pop())
        # Use a forloop to iterate through each player in the players list

# items = [] # a stack
# items.append("Plate 1")
# items.append("Plate 2")
# plate = items.pop() # removes the last item from a list
# print(plate)
# for item in items:
#     print(item)



Brian = Player("Brian")
Lekha = Player("Lekha")

players = [Brian, Lekha]


deck = Deck()

deck.shuffleDeck()
deck.dealCards(players)
