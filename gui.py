import pygame as pg
from pygame import surface


# color dictionary, represents white, red and blue
color = {
    "bg": (242, 213, 171),
    "empty": (213, 192, 155),
    "player1": (0, 0, 0),  # black
    "player2": (255, 255, 255),  # white
    "player3": (255, 0, 0),  # red
    "player4": (0, 0, 255),  # blue
    "player5": (0, 200, 0),  # green
    "player6": (243, 243, 14)  # yellow
}


WIDTH = 600
HEIGHT = 800
HIGHLIGHT = (0, 255, 255)

# costants of the board
MARGIN_DISTANCE = 20
CIRCLE_RADIUS = 20
CIRCLE_DIAMETER = 2 * CIRCLE_RADIUS
H_SPACING = 8
V_SPACING = 1
WINDOW_WIDTH = (MARGIN_DISTANCE * 2) + \
    (CIRCLE_DIAMETER * 13) + (H_SPACING * 12)
WINDOW_HEIGHT = (MARGIN_DISTANCE * 2) + \
    (CIRCLE_DIAMETER * 17) + (V_SPACING * 16)


def initBoard():
    pg.init()
    pg.display.set_caption('Chinese Checkers')
    screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    return screen


def drawBoard(board, display_surface):

    display_surface.fill(color["bg"])

    y_coord = MARGIN_DISTANCE + CIRCLE_RADIUS

    for row in range(0, 17):

        x_coord_long = MARGIN_DISTANCE + CIRCLE_RADIUS
        x_coord_short = int(MARGIN_DISTANCE +
                            CIRCLE_DIAMETER + (H_SPACING / 2))

        for circle_in_a_row in range(0, 13):
            if row % 2 == 0:

                board_value = board[row][circle_in_a_row * 2]
                color_circle(board_value, display_surface,
                             x_coord_long, y_coord)

                x_coord_long = x_coord_long + CIRCLE_DIAMETER + H_SPACING

            elif row % 2 != 0 and circle_in_a_row != 12:

                board_value = board[row][circle_in_a_row * 2 + 1]
                color_circle(board_value, display_surface,
                             x_coord_short, y_coord)

                x_coord_short = x_coord_short + CIRCLE_DIAMETER + H_SPACING

        y_coord = y_coord + CIRCLE_DIAMETER + V_SPACING


def color_circle(board_value, surface, xCoord, yCoord):

    if board_value == -1:
        pg.draw.circle(surface, color["bg"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 0:
        pg.draw.circle(surface, color["empty"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 1:
        pg.draw.circle(surface, color["player1"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 2:
        pg.draw.circle(surface, color["player2"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 3:
        pg.draw.circle(surface, color["player3"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 4:
        pg.draw.circle(surface, color["player4"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 5:
        pg.draw.circle(surface, color["player5"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
    if board_value == 6:
        pg.draw.circle(surface, color["player6"],
                       (xCoord, yCoord), CIRCLE_RADIUS, 0)
