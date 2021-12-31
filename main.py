from gui import *
from board import *
from engine import *
from math import sqrt

display_surface = initBoard()
board = createBoard()

drawBoard(board, display_surface)
firstClick = None

while True:

        # board = doMove(11, 3, 12, 4, board, 1)

        x = pg.mouse.get_pos()[0]
        y = pg.mouse.get_pos()[1]

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1 and firstClick == None:
                    for key, val in circlePos.items():
                        if sqrt((x - val[0]) ** 2 + (y - val[1]) ** 2) < CIRCLE_RADIUS:
                            print(x, y)
                            print(circlePos[(key[0], key[1])])
                            firstClick = key
                            print('cord: ', firstClick, ' - Value: ', board[firstClick[0]][firstClick[1]])
                    print("Left mouse button pressed.")
                elif event.button == 1 and firstClick != None:
                    for key, val in circlePos.items():
                        if sqrt((x - val[0]) ** 2 + (y - val[1]) ** 2) < CIRCLE_RADIUS:
                            print('move', firstClick, key)
                            board = doMove(firstClick[0], firstClick[1], key[0], key[1], board, board[firstClick[0]][firstClick[1]])
                            firstClick = None
                            drawBoard(board, display_surface)
        pg.display.update()