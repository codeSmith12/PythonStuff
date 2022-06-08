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
        print(f"{self.name}'s hand:")
        for card in self.hand:
            card.display()
        print("")

class Deck:
    def __init__(self):
        self.cards = []
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
    def drawCard(self):
        card = self.cards.pop() # the last item in the list
        return card

    def dealCards(self, players):
        for player in players:
            player.addCard(self.drawCard())
            player.addCard(self.drawCard())
            player.showHand()

class Game:
    def __init__(self):
        deck = Deck()

        player1 = Player("Brian")
        player2 = Player("Jas")
        player3 = Player("Jerm")
        player4 = Player("Lekha")
        player5 = Player("Oliver")
        players = [player1, player2, player3, player4, player5]

        deck.shuffleDeck()
        deck.dealCards(players)
game = Game()
