from gui import *
from board import *
from engine import *
from math import sqrt

display_surface = initBoard()
board = createBoard()

drawBoard(board, display_surface)
selectedPiece = None
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

                    if selectedPiece == None:
                        # If no piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            # Use mouse pos to find piece clicked
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:
                                if board[pieceCoord[0]][pieceCoord[1]] != 0:
                                    selectedPiece = pieceCoord
                                    print(selectedPiece, "selected")
                                    #TODO - highlight selected piece
                                else:
                                    print("No piece selected")
                    else:
                        # If piece is selected
                        for pieceCoord, pixedCoord in circlePos.items():
                            if sqrt((x - pixedCoord[0]) ** 2 + (y - pixedCoord[1]) ** 2) < CIRCLE_RADIUS:

                                # Move piece
                                try:
                                    doMove(selectedPiece, pieceCoord, board, board[selectedPiece[0]][selectedPiece[1]])
                                
                                    # Reset selected piece
                                    selectedPiece = None

                                    # Update board
                                    drawBoard(board, display_surface)
                                    pg.display.update()
                                except Exception as e:
                                    if e.args[0] == "Error - Invalid move, same position":
                                        print(selectedPiece, "deselected")
                                        selectedPiece = None
                                    else:
                                        print(e.args[0])