from math import sqrt
from board import *
from gui import *


class Game():

    def __init__(self, noOfPlayers = 2):
        self.board = Board(noOfPlayers)
        self.displaySurface = initBoard()

        self.playerList = list(self.board.playerSets.keys())

        self.turn = 0
        
        # iterate the dictionary to get the first player
        self.currentPlayer = self.playerList[0]

    def updateBoard(self):
        drawBoard(self.board.array, self.displaySurface)
        pg.display.update()
    
    def getClickedPiece(self):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        for pieceCoord, pixedCoord in circlePos.items(): # use mouse pos to find piece clicked
            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                if self.board.array[pieceCoord] >= 0:
                    return pieceCoord
                else:
                    raise Exception("Empty space clicked")
        raise Exception("No piece found at mouse position")
    
    def getCurrentPlayer(self):
        return self.playerList[self.turn % len(self.playerList)]
    
    def getCurrentPlayerColor(self):
        return self.board.colorMapping[self.getCurrentPlayer()]


    def play(self):
        self.updateBoard()
        print(self.getCurrentPlayerColor(), "goes first.")


        while True:

            # get events
            for event in pg.event.get():

                # event - exit game
                if event.type == pg.QUIT:
                    pg.quit()
                    break

                # event - key pressed
                if event.type == pg.KEYDOWN:
                    if event.key == ord("r"):
                        self.turn = 0
                        self.board.resetBoard()
                        print("\nGame restarted.")
                        print("---------------------------")
                        print(self.getCurrentPlayerColor(), "goes first.")

                    elif event.key == ord("h"):
                        if self.board.toggleAssist():
                            print("Move assist activated")
                        else:
                            print("Move assist disabled")
                        # pieceMoves = self.board.findAllLegalMoves(self.currentPlayer)
                        # for clickedPiece in pieceMoves:
                        #     for move in clickedPiece:
                        #         self.board.array[move] = 11

                # event - mousebutton pressed
                if event.type == pg.MOUSEBUTTONDOWN:
                    
                    if event.button == 1: # left click

                        try:
                            clickedPiece = self.getClickedPiece() # get piece clicked
                        except Exception as e:
                            continue

                        if self.board.selection.selected == False: # if no piece is selected
                            if self.board.array[clickedPiece] == self.getCurrentPlayer(): # if piece belongs to player
                                self.board.selection.select(clickedPiece)
                            elif self.board.array[clickedPiece] == 0:
                                continue
                            else:
                                print(self.getCurrentPlayerColor(), "is up to move.")
                        else:

                            if self.board.movePiece(clickedPiece): # if move is successful
                                self.turn += 1
                                print("Player", self.getCurrentPlayerColor(), "is playing.")
                                break
                            else:
                                self.board.selection.deselect()
                                break

                self.updateBoard()

    def end(self):
        pass
        