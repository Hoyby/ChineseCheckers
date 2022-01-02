import numpy as np


class Board:
    class Selection:
        def __init__(self, board):
            self.board = board
            self.coord = None
            self.value = None
            self.selected = False

        def select(self, coord):
            if not self.selected:
                self.coord = coord
                self.value = self.board.array[coord[0]][coord[1]]
                self.board.array[coord[0]][coord[1]] = 10
                self.selected = True
                return True
            else:
                raise Exception(
                    "Error - A piece already selected at ", self.coord)

        def deselect(self):
            if self.selected:
                self.board.array[self.coord[0]][self.coord[1]] = self.value
                self.coord = None
                self.value = None
                self.selected = False
                return True
            else:
                raise Exception("Error - No piece selected")

        def postMove(self):
            if self.selected:
                self.board.array[self.coord[0]][self.coord[1]] = 0
                self.coord = None
                self.value = None
                self.selected = False
                return True
            else:
                raise Exception("Error - No piece selected")

    def __init__(self):

        self.selection = self.Selection(self)

        self.array = np.zeros((17, 25), dtype=int)

        self.array[:][:] = -1

        self.array[0][12] = 1
        self.array[1][11] = 1
        self.array[1][13] = 1
        self.array[2][10] = 1
        self.array[2][12] = 1
        self.array[2][14] = 1
        self.array[3][9] = 1
        self.array[3][11] = 1
        self.array[3][13] = 1
        self.array[3][15] = 1

        self.array[4][18] = 2
        self.array[4][20] = 2
        self.array[4][22] = 2
        self.array[4][24] = 2
        self.array[5][19] = 2
        self.array[5][21] = 2
        self.array[5][23] = 2
        self.array[6][20] = 2
        self.array[6][22] = 2
        self.array[7][21] = 2

        self.array[9][21] = 3
        self.array[10][20] = 3
        self.array[10][22] = 3
        self.array[11][19] = 3
        self.array[11][21] = 3
        self.array[11][23] = 3
        self.array[12][18] = 3
        self.array[12][20] = 3
        self.array[12][22] = 3
        self.array[12][24] = 3

        self.array[13][9] = 4
        self.array[13][11] = 4
        self.array[13][13] = 4
        self.array[13][15] = 4
        self.array[14][10] = 4
        self.array[14][12] = 4
        self.array[14][14] = 4
        self.array[15][11] = 4
        self.array[15][13] = 4
        self.array[16][12] = 4

        self.array[9][21 - 18] = 5
        self.array[10][20 - 18] = 5
        self.array[10][22 - 18] = 5
        self.array[11][19 - 18] = 5
        self.array[11][21 - 18] = 5
        self.array[11][23 - 18] = 5
        self.array[12][18 - 18] = 5
        self.array[12][20 - 18] = 5
        self.array[12][22 - 18] = 5
        self.array[12][24 - 18] = 5

        self.array[4][18 - 18] = 6
        self.array[4][20 - 18] = 6
        self.array[4][22 - 18] = 6
        self.array[4][24 - 18] = 6
        self.array[5][19 - 18] = 6
        self.array[5][21 - 18] = 6
        self.array[5][23 - 18] = 6
        self.array[6][20 - 18] = 6
        self.array[6][22 - 18] = 6
        self.array[7][21 - 18] = 6

        self.array[4][8] = 0
        self.array[4][10] = 0
        self.array[4][12] = 0
        self.array[4][14] = 0
        self.array[4][16] = 0

        self.array[5][7] = 0
        self.array[5][9] = 0
        self.array[5][11] = 0
        self.array[5][13] = 0
        self.array[5][15] = 0
        self.array[5][17] = 0

        self.array[6][6] = 0
        self.array[6][8] = 0
        self.array[6][10] = 0
        self.array[6][12] = 0
        self.array[6][14] = 0
        self.array[6][16] = 0
        self.array[6][18] = 0

        self.array[7][5] = 0
        self.array[7][7] = 0
        self.array[7][9] = 0
        self.array[7][11] = 0
        self.array[7][13] = 0
        self.array[7][15] = 0
        self.array[7][17] = 0
        self.array[7][19] = 0

        self.array[7][5] = 0
        self.array[7][7] = 0
        self.array[7][9] = 0
        self.array[7][11] = 0
        self.array[7][13] = 0
        self.array[7][15] = 0
        self.array[7][17] = 0
        self.array[7][19] = 0

        self.array[8][4] = 0
        self.array[8][6] = 0
        self.array[8][8] = 0
        self.array[8][10] = 0
        self.array[8][12] = 0
        self.array[8][14] = 0
        self.array[8][16] = 0
        self.array[8][18] = 0
        self.array[8][20] = 0

        self.array[9][5] = 0
        self.array[9][7] = 0
        self.array[9][9] = 0
        self.array[9][11] = 0
        self.array[9][13] = 0
        self.array[9][15] = 0
        self.array[9][17] = 0
        self.array[9][19] = 0

        self.array[10][6] = 0
        self.array[10][8] = 0
        self.array[10][10] = 0
        self.array[10][12] = 0
        self.array[10][14] = 0
        self.array[10][16] = 0
        self.array[10][18] = 0

        self.array[11][7] = 0
        self.array[11][9] = 0
        self.array[11][11] = 0
        self.array[11][13] = 0
        self.array[11][15] = 0
        self.array[11][17] = 0

        self.array[12][8] = 0
        self.array[12][10] = 0
        self.array[12][12] = 0
        self.array[12][14] = 0
        self.array[12][16] = 0

    def findLegalMoves(self, piece, frontier=[], visited=[], firstCall=True):
        if piece not in visited:
            adjacent = dict()
            adjacent["right"] = (piece[0], piece[1] + 2)  # right
            adjacent["left"] = (piece[0], piece[1] - 2)  # left
            adjacent["upLeft"] = (piece[0] - 1, piece[1] - 1)  # up left
            adjacent["upRight"] = (piece[0] - 1, piece[1] + 1)  # up right
            adjacent["downLeft"] = (piece[0] + 1, piece[1] - 1)  # down left
            adjacent["downRight"] = (piece[0] + 1, piece[1] + 1)  # down right

            for key, val in adjacent.items():
                try:
                    self.array[val]
                except IndexError:
                    continue

                if firstCall:
                    if self.array[val] == 0:
                        print(val)
                        visited.append(val)

                if self.array[val] != 0 and self.array[val] != -1:
                    match(key):
                        case "right":
                            newLocation = val[0], val[1] + 2
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                        case "left":
                            newLocation = val[0], val[1] - 2
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                        case "upLeft":
                            newLocation = val[0] - 1, val[1] - 1
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                        case "upRight":
                            newLocation = val[0] - 1, val[1] + 1
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                        case "downLeft":
                            newLocation = val[0] + 1, val[1] - 1
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                        case "downRight":
                            newLocation = val[0] + 1, val[1] + 1
                            try:
                                if self.array[newLocation] == 0:
                                    frontier.append(newLocation)
                            except Exception as e:
                                continue

                # elif firstCall and self.array[val] != -1:
                #     legalMoves.append(val)

            visited.append(piece)
        if len(frontier) > 0:
            piece = frontier.pop(0)
            if not piece in visited:
                self.findLegalMoves(piece, frontier, visited, firstCall=False)

        return visited

    def movePiece(self, toCoord):
        if toCoord in self.findLegalMoves(self.selection.coord, frontier=[], visited=[], firstCall=True):
            self.array[toCoord] = self.selection.value
            self.selection.postMove()
            return True
        else:
            return False

    def selectPiece(self, coord):
        if self.array[coord[0]][coord[1]] != 0:
            self.selection.select(coord)
        else:
            raise Exception("Error - No piece selected")

    def deselectPiece(self):
        self.selection.deselect()
