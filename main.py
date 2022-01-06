from gui import *
from math import sqrt
from game import *

def runGame():
    game = Game(noOfPlayers=3)
    game.play()

if __name__ == "__main__":
    runGame()