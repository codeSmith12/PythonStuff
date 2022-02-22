import pygame

class Game:
    def __init__(self, id):
        self.p1Locked = False
        self.p2Locked = False
        self.ready = False
        self.id = id
        self.moves = [None, None]
        self.wins = [0,0]
        self.ties = 0

    def get_player_move(self, p):
        return self.moves[p] # p in range of 0 or 1, returns move

    def play(self,player,move):
        self.moves[player] = move
        if player == 0:
            self.p1Locked = True
        else:
            self.p2Locked = True
    def connected(self):
        return self.ready

    def bothLocked(self):
        return self.p1Locked and self.p2Locked

    def winner(self):
        p1 = sef.moves[0].upper()[0]
        p2 = sef.moves[1].upper()[0]

        winner = -1
        if p1 == "R" and p2 == "S":
            winner = 0
        elif p1 == "S" and p2 == "R":
            winner = 1
        elif p1 == "R" and p2 == "P":
            winner = 1
        elif p1 == "S" and p2 == "P":
            winner = 0
        elif p1 == "P" and p2 == "R":
            winner = 0
        elif p1 == "P" and p2 == "S":
            winner = 1
        return winner

    def resetLocked(self):
        self.p1Locked = False
        self.p2Locked = False
