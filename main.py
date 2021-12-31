from gui import *
from board import *

display_surface = initBoard()
board = createBoard()

while True:
        drawBoard(board, display_surface)

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                break

        pg.display.update()