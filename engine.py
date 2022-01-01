def validMove(fromCoord, toCoord, board):
    if fromCoord[0] == toCoord[0] and fromCoord[1] == toCoord[1]:
        raise Exception("Error - Invalid move, same position")
    if board[fromCoord[0]][fromCoord[1]] == 0:
        raise Exception("Error - Invalid move, no piece selected")
    if board[toCoord[0]][toCoord[1]] != 0:
        raise Exception("Error - Invalid move, destination occupied")
    if abs(fromCoord[0] - toCoord[0]) > 1 or abs(fromCoord[1] - toCoord[1]) > 2:
        raise Exception("Error - Invalid move, too far")
    if abs(fromCoord[0] - toCoord[0]) == 2 and abs(fromCoord[1] - toCoord[1]) != 0:
        raise Exception("Error - Invalid move, not diagonal")
    return True

def doMove(fromCoord, toCoord, board, player):
    try: 
        validMove(fromCoord, toCoord, board)
        board[toCoord] = player
        board[fromCoord] = 0
        print("Move from", fromCoord, "to", toCoord, "successful")
    except Exception as e:
        raise e

def selectPiece(fromCoord, board):
    if board[fromCoord[0]][fromCoord[1]] != 0:
        board[fromCoord[0]][fromCoord[1]] = 10
    else:
        raise Exception("Error - No piece selected")