from gui import *
from math import sqrt
from board import *


board = Board()

display_surface = initBoard()
drawBoard(board.array, display_surface)
pg.display.update()


while True:
        

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

            # If mousebutton is pressed
            if event.type == pg.MOUSEBUTTONDOWN:
                
                # If first click
                if event.button == 1:

                    # Get mouse position
                    x = pg.mouse.get_pos()[0]
                    y = pg.mouse.get_pos()[1]

                    if board.selection.selected == False:
                        # If no piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            # Use mouse pos to find piece clicked
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                                if board.array[pieceCoord[0]][pieceCoord[1]] != 0:
                                    board.selectPiece(pieceCoord)
                                    print(board.selection.coord, "selected")
                                else:
                                    print("No piece selected")
                    else:
                        # If piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:

                                # Move piece
                                try:
                                    board.doMove(pieceCoord)
                                    
                                except Exception as e:
                                    if e.args[0] == "Error - Invalid move, same position":
                                        print(board.selection.coord, "deselected")
                                        board.deselectPiece()
                                    else:
                                        print(e.args[0])

            drawBoard(board.array, display_surface)
            pg.display.update()