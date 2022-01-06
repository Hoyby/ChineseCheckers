import numpy as np

class Board:
    class Selection:
        def __init__(self, board):
            self.board = board
            self.coord = None
            self.legalMoves = None
            self.value = None
            self.selected = False

        def select(self, coord):
            if self.selected and coord == self.coord:
                self.deselect()
            elif not self.selected and self.board.array[coord] > 0:
                self.coord = coord
                self.value = self.board.array[coord] # save value of piece
                self.board.array[coord] = 10 # highlight selected piece
                self.legalMoves = self.board.findLegalMoves(coord, validMoves = []) # find legal moves
                for move in self.legalMoves:
                    self.board.array[move] = 11 # highlight legal moves
                self.selected = True
            else:
                raise Exception(
                    "Error - A piece already selected at ", self.coord)

        def deselect(self):
            if self.selected:
                self.board.array[self.coord] = self.value # restore value of piece
                for move in self.legalMoves:
                    self.board.array[move] = 0 # remove highlighted legal moves
                self.coord = None
                self.legalMoves = None # reset legal moves
                self.value = None
                self.selected = False
            else:
                raise Exception("Error - No piece selected")

        def handleMove(self, coord):
            if self.selected:
                self.board.array[self.coord] = 0
                for move in self.legalMoves:
                    self.board.array[move] = 0
                self.board.array[coord] = self.value
                self.coord = None
                self.legalMoves = None
                self.value = None
                self.selected = False
            else:
                raise Exception("Error - No piece selected")

    def __init__(self, players):

        self.selection = self.Selection(self)

        self.array = np.zeros((17, 25), dtype=int)
        self.array[:][:] = -1

        self.playersSets = dict()

        self.colorMapping = {
            1: "black",
            2: "white",
            3: "red",
            4: "blue",
            5: "green",
            6: "yellow"
        }

        initBoard = dict()
        initBoard[0] = [[4, 8], [4, 10], [4, 12], [4, 14], [4, 16], [5, 7], [5, 9], [5, 11], [5, 13], [5, 15], [5, 17], [6, 6], [6, 8], [6, 10], [6, 12], [6, 14], [6, 16], [6, 18], [7, 5], [7, 7], [7, 9], [7, 11], [7, 13], [7, 15], [7, 17], [7, 19], [7, 5], [7, 7], [7, 9], [7, 11], [7, 13], [7, 15], [7, 17], [7, 19], [8, 4], [8, 6], [8, 8], [8, 10], [8, 12], [8, 14], [8, 16], [8, 18], [8, 20], [9, 5], [9, 7], [9, 9], [9, 11], [9, 13], [9, 15], [9, 17], [9, 19], [10, 6], [10, 8], [10, 10], [10, 12], [10, 14], [10, 16], [10, 18], [11, 7], [11, 9], [11, 11], [11, 13], [11, 15], [11, 17], [12, 8], [12, 10], [12, 12], [12, 14], [12, 16]]
        initBoard[1] = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]
        initBoard[2] = [[13, 9], [13, 11], [13, 13], [13, 15], [14, 10], [14, 12], [14, 14], [15, 11], [15, 13], [16, 12]]
        initBoard[3] = [[9, 3], [10, 2], [10, 4], [11, 1], [11, 3], [11, 5], [12, 0], [12, 2], [12, 4], [12, 6]]
        initBoard[4] = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]]
        initBoard[5] = [[9, 21], [10, 20], [10, 22], [11, 19], [11, 21], [11, 23], [12, 18], [12, 20], [12, 22], [12, 24]]
        initBoard[6] = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]

        for key, val in initBoard.items():
            match(players):
                case 2:
                    if key <= 2 and key > 0:
                        self.playersSets[key] = val
                        for piece in val:
                            self.array[piece[0], piece[1]] = key
                    else:
                        for piece in val:
                            self.array[piece[0], piece[1]] = 0
                case 3:
                    if key % 2 == 0 and key > 0:
                        self.playersSets[key] = val
                        for piece in val:
                            self.array[piece[0], piece[1]] = key
                    else:
                        for piece in val:
                            self.array[piece[0], piece[1]] = 0
                case 4:
                    if key <= 4 and key > 0:
                        self.playersSets[key] = val
                        for piece in val:
                            self.array[piece[0], piece[1]] = key
                    else:
                        for piece in val:
                            self.array[piece[0], piece[1]] = 0
                case 6:
                    if key > 0:
                        self.playersSets[key] = val
                    
                    for piece in val:
                        self.array[piece[0], piece[1]] = key
                case _:
                    print("Error - Invalid number of players")

    def findNeighbors(self, piece):
        adjacent = dict()
        adjacent["right"] = (piece[0], piece[1] + 2)  # right
        adjacent["left"] = (piece[0], piece[1] - 2)  # left
        adjacent["upLeft"] = (piece[0] - 1, piece[1] - 1)  # up left
        adjacent["upRight"] = (piece[0] - 1, piece[1] + 1)  # up right
        adjacent["downLeft"] = (piece[0] + 1, piece[1] - 1)  # down left
        adjacent["downRight"] = (piece[0] + 1, piece[1] + 1)  # down right
        return adjacent

    def findLegalMoves(self, piece, validMoves, depth = 0, queue=[]):
        if piece not in validMoves:
            
            # for all neighbors
            for neighborPosition in self.findNeighbors(piece).values():

                # check if out of bounds
                try:
                    self.array[neighborPosition]
                except IndexError:
                    continue

                # add single moves from origin
                if depth == 0 and self.array[neighborPosition] == 0 and neighborPosition not in validMoves:
                    validMoves.append(neighborPosition)

                # if neighbor is occupied, check if jump is possible
                if self.array[neighborPosition] > 0:
                    newLocation = (neighborPosition[0] + (neighborPosition[0] - piece[0]), neighborPosition[1] + (neighborPosition[1] - piece[1]))

                    # check if newlocation is out of bounds or is empty
                    try:
                        self.array[newLocation]
                        if self.array[newLocation] == 0 and newLocation not in queue and newLocation not in validMoves:
                            queue.append(newLocation)
                    except IndexError:
                        continue

            validMoves.append(piece)
        
        # check if there is more nodes to explore
        if len(queue) > 0:
            piece = queue.pop(0)
            if not piece in validMoves:
                validMoves = self.findLegalMoves(piece, validMoves, depth + 1, queue)

        if self.selection.coord in validMoves:
            validMoves.remove(self.selection.coord)

        return validMoves

    def movePiece(self, moveTo):
        if moveTo in self.selection.legalMoves:
            self.selection.handleMove(moveTo)
            return True
        else:
            return False
