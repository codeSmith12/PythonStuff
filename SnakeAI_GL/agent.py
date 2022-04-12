import torch
import random
import numpy as np
from collections import deque
from game import SnakeGameAI, Direction, Point
from model import Linear_QNet, QTrainer
from helper import plot


MAX_MEMORY = 100_000
BATCH_SIZE = 1000
LR = 0.001

class Agent:
    def __init__(self):
        self.numGames = 0
        self.epsilon = 0 # Controls the randomness
        self.gamma = 0.9 # discount rate, needs to be less than 1
        self.memory = deque(maxlen=MAX_MEMORY) # popleft..
        self.model = Linear_QNet(11, 256, 3) # Inputs, hidden layer nodes, output
        self.trainer = QTrainer(self.model, lr=LR, gamma=self.gamma)


    def getState(self, game):
        head = game.snake[0]
        pointL = Point(head.x - 20, head.y) # Hard coded block size, maybe fix
        pointR = Point(head.x + 20, head.y) # Hard coded block size, maybe fix
        pointU = Point(head.x , head.y - 20) # Hard coded block size, maybe fix
        pointD = Point(head.x , head.y + 20) # Hard coded block size, maybe fix

        dirL = game.direction == Direction.LEFT
        dirR = game.direction == Direction.RIGHT
        dirU = game.direction == Direction.UP
        dirD = game.direction == Direction.DOWN

        state = [

            # Danger Straight
            (dirR and game.is_collision(pointR)) or
            (dirL and game.is_collision(pointL)) or
            (dirU and game.is_collision(pointU)) or
            (dirD and game.is_collision(pointD)),
            # Danger Right
            (dirU and game.is_collision(pointU)) or
            (dirD and game.is_collision(pointD)) or
            (dirL and game.is_collision(pointL)) or
            (dirR and game.is_collision(pointR)),
            # Danger Left
            (dirD and game.is_collision(pointD)) or
            (dirU and game.is_collision(pointU)) or
            (dirR and game.is_collision(pointR)) or
            (dirL and game.is_collision(pointL)),

            # Move Direction
            dirL,
            dirR,
            dirU,
            dirD,

            game.food.x < game.head.x, # food is left
            game.food.x > game.head.x, # food is right
            game.food.y < game.head.y,  # food up
            game.food.y > game.head.y  # food down

        ]

        return np.array(state, dtype=int)

    def remember(self, state, action, reward, nextState, gameOver):
        self.memory.append((state, action, reward, nextState, gameOver)) # popleft if maxed, stored as tuple

    def train_long_memory(self):
        if len(self.memory) > BATCH_SIZE:
            miniSample = random.sample(self.memory, BATCH_SIZE) # Returns list of tuples
        else:
            miniSample = self.memory

        states, actions, rewards, nextStates, gameOvers = zip(*miniSample)
        self.trainer.trainStep(states, actions, rewards, nextStates, gameOvers)

    def train_short_memory(self, state, action, reward, nextState, gameOver):
        self.trainer.trainStep(state, action, reward, nextState, gameOver)

    def getAction(self, state):
        # Random moves: tradeoff exploration / exploitation
        self.epsilon = 80 - self.numGames
        finalMove = [0,0,0]

        # The longer the training goes, the smaller epsilon gets, less randomization of moves
        if random.randint(0,200) < self.epsilon:
            move = random.randint(0, 2)
            finalMove[move] = 1
        else:
            state0 = torch.tensor(state, dtype=torch.float)
            prediction = self.model(state0)
            move = torch.argmax(prediction).item() # Converts to integer?
            finalMove[move] = 1
        return finalMove

def train():
    plotScores = []
    plotMeanScores = []
    totalScore = 0
    record = 0
    agent = Agent()
    game = SnakeGameAI()

    while True:
        # get old state
        stateOld = agent.getState(game)
        # Get move
        finalMove = agent.getAction(stateOld)
        # Perform move and get new state
        reward, gameOver, score = game.play_step(finalMove)
        stateNew = agent.getState(game)
        # Train short memory
        agent.train_short_memory(stateOld, finalMove, reward, stateNew, gameOver)
        # remember
        agent.remember(stateOld, finalMove, reward, stateNew, gameOver)

        if gameOver:
            # Train long memory (replay memory), plot results
            game.reset()
            agent.numGames += 1
            agent.train_long_memory()

            if score > record:
                record = score
                agent.model.save()
            print(f"Game: {agent.numGames} Score: {score} Record: {record}")

            plotScores.append(score)
            totalScore += score
            mean_score = totalScore / agent.numGames
            plotMeanScores.append(mean_score)
            plot(plotScores, plotMeanScores)


if __name__ == "__main__":
    train()
