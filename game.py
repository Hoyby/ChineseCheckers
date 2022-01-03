from math import sqrt
from board import *
from gui import *


class Game():

    def __init__(self, players = 2):
        self.turn = 0
        self.board = Board(players)
        self.displaySurface = initBoard()

    def updateBoard(self):
        drawBoard(self.board.array, self.displaySurface)
        pg.display.update()
    
    def getClickedPiece(self):
        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]
        for pieceCoord, pixedCoord in circlePos.items(): # use mouse pos to find piece clicked
            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                if self.board.array[pieceCoord] > 0:
                    return pieceCoord
        return None

    def play(self):
        self.updateBoard()

        while True:

            # get events
            for event in pg.event.get():

                # event - exit game
                if event.type == pg.QUIT:
                    pg.quit()
                    break

                # event - mousebutton pressed
                if event.type == pg.MOUSEBUTTONDOWN:
                    
                    if event.button == 1: # left click

                        # get mouse position
                        x = pg.mouse.get_pos()[0]
                        y = pg.mouse.get_pos()[1]

                        if self.board.selection.selected == False: # if no piece is selected
                            piece = self.getClickedPiece()
                            if piece and self.board.array[piece[0]][piece[1]] != 0:
                                self.board.selection.select(piece)
                                print(self.board.selection.coord, "selected")
                                break
                            else:
                                print("No piece selected")
                                break
                        else:
                            # if piece is selected
                            for piece, pixedCoord in circlePos.items():
                                if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                                    if piece != self.board.selection.coord:
                                        # attempt move
                                        if self.board.movePiece(piece):
                                            print(self.board.selection.coord, " moved to", piece)
                                            break
                                        else:
                                            print("invalid move:", self.board.selection.coord, "deselected")
                                            self.board.selection.deselect()
                                            break
                                    else:
                                        print(self.board.selection.coord, "deselected")
                                        self.board.selection.deselect()
                                        break

                self.updateBoard()

    def turn(self):
        player = self.getPlayer()
        self.turn += 1

    def end(self):
        pass
        