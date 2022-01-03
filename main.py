from gui import *
from math import sqrt
from board import *

def runGame():

    # initialize game
    board = Board()
    displaySurface = initBoard()
    drawBoard(board.array, displaySurface)
    pg.display.update()

    while True:

        for event in pg.event.get():

            # exit game
            if event.type == pg.QUIT:
                pg.quit()
                break

            # if mousebutton is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                
                # if first click
                if event.button == 1:

                    # get mouse position
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]

                    if board.selection.selected == False:
                        # if no piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            # use mouse pos to find piece clicked
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                                if board.array[pieceCoord[0]][pieceCoord[1]] != 0:
                                    board.selection.select(pieceCoord)
                                    print(board.selection.coord, "selected")
                                    break
                                else:
                                    print("No piece selected")
                                    break
                    else:
                        # if piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                                if pieceCoord != board.selection.coord:
                                    # attempt move
                                    if board.movePiece(pieceCoord):
                                        print(board.selection.coord, " moved to", pieceCoord)
                                        break
                                    else:
                                        print("invalid move:", board.selection.coord, "deselected")
                                        board.selection.deselect()
                                        break
                                else:
                                    print(board.selection.coord, "deselected")
                                    board.selection.deselect()
                                    break

            drawBoard(board.array, displaySurface)
            pg.display.update()

if __name__ == "__main__":
    runGame()