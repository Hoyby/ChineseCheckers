
def validMove(fromX, fromY, toX, toY, board):
    if fromX == toX and fromY == toY:
        print("Error - 1")
        return False
    if board[fromX][fromY] == 0:
        print("Error - 2")
        return False
    if board[toX][toY] != 0:
        print("Error - 3")
        return False
    if abs(fromX - toX) > 1 or abs(fromY - toY) > 2:
        print("Error - 4")
        return False
    if abs(fromX - toX) == 2 and abs(fromY - toY) != 0:
        print("Error - 5")
        return False
    return True

def doMove(fromX, fromY, toX, toY, board, player):
    if validMove(fromX, fromY, toX, toY, board):
        board[toX][toY] = player
        board[fromX][fromY] = 0
        return board
    else:
        return board
