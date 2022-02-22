import random

class Card:
    def __init__(self, num, suit):
        self.num = num
        self.suit = suit

    def display(self):
        if self.num == 1:
            print(f"Ace of {self.suit}")
        elif self.num <= 10:
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
        self.hit = False
        self.bust = False
        self.hand = []
        self.hasWon = False
        self.stay = False

    def addCard(self, card):
        self.hand.append(card)
    def checkBust(self):
        total = 0
        for card in self.hand:
            if card.num == 1:
                total += 11
            elif card.num > 10:
                total += 10
            else:
                total += card.num
        for card in self.hand:
            if total > 21 and card.num == 1:
                total -= 10

        print(f"{self.name}'s total is {total}\n")
        if total > 21:
            self.bust = True
            print(f"{self.name} has busted. Poor luck :(\n")
        if total == 21:
            print(f"{self.name} has won!!!\n")
            self.hasWon = True
        return total

    def showHand(self):
        print(f"{self.name}'s hand:")
        for card in self.hand:
            card.display()
        print("")

class Dealer(Player):
    def __init__(self):
        Player.__init__(self,"Dealer")
        self.cards = []
        for i in range(1,14):
            self.addCard(Card(i, "Hearts"))
            self.addCard(Card(i, "Diamonds"))
            self.addCard(Card(i, "Clubs"))
            self.addCard(Card(i, "Spades"))
        # Outside of for loop
        self.shuffleDeck()

    def addCard(self, card):
        self.cards.append(card)

    def shuffleDeck(self):
        random.shuffle(self.cards)

    def displayDeck(self):
        for card in self.cards:
            card.display()

    def drawCard(self):
        # Removes the last card (top of the deck), and gives it back
        return self.cards.pop()

    def dealCards(self, players):
        for player in players:
            player.addCard(self.drawCard())
            player.addCard(self.drawCard())
            player.showHand()

        self.hand.append(self.drawCard())
        self.hand.append(self.drawCard())
        self.showHand()

    def checkWin(self, players):
        # Calculate dealer total
        dealerTotal = self.checkBust()
        # loop through each player
        for player in players:
            # Calculate their total
            playerTotal = player.checkBust()
            # Check if they beat the dealer by being
            # closer to 21 than the dealer.
            # Oliver got 21, Dealer got 23
            if not self.bust: # <------
                if playerTotal > dealerTotal and playerTotal <= 21:
                    print(f"{player.name} has beaten the dealer!")
                    player.hasWon = True
                else:
                    print(f"{player.name} has lost to the dealer.")
            else:
                print(f"{player.name} has beaten the dealer!")


    def askPlayer(self, players):
        for player in players:
            if not player.bust and not player.hasWon and not player.stay:
                player.showHand()
                hit = input(f"{player.name}, would you like to (H)it or (S)tay?")
                if hit.lower() == "h":
                    player.addCard(self.drawCard())
                    player.showHand()
                    player.checkBust()

                elif hit.lower() == "s":
                    player.checkBust()
                    player.stay = True # <--------------
        self.hitOrStay()


# Fix hit or Stay with class
    def hitOrStay(self):
        total = self.checkBust()
        if total < 17:
            print("Dealer hits.")
            self.hand.append(self.drawCard())
            self.showHand()
        else:
            print("Dealer stays.")

    def stillPlaying(self, players):
        # Check if any of the players are still playing...
        for player in players:
            if player.bust == False and player.hasWon == False and player.stay == False:
                return True
        # Calculate Total for Dealer
        # If no players are playing, check if dealer is still in the game.
        total = self.checkBust()
        if total < 17:
            return True
        else: # Else the game is over.
            return False


player1 = Player("Brian")
player2 = Player("Oliver")
player3 = Player("Jeremy")
player4 = Player("Lekha")

players = [player1, player2, player3, player4]

dealer = Dealer()

# Deal out initial cards
dealer.dealCards(players)
while dealer.stillPlaying(players):
    dealer.askPlayer(players)
dealer.checkWin(players) # <-----
