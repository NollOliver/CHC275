def drawBoard(board):
    print("\n  1 2 3 4 5 6 7")
    print(" ---------------")
    for row in board:
        line = "|"
        for cell in row:
            line += f" {cell}" 
        line += " |"
        print(line)
    print(" ---------------")
def switchPlayer(player):
    if player == "X":
        return "O"
    return "X"
def dropPiece(board, player, column):
    for r in range(len(board) - 1, -1, -1):
        if board[r][column] == 0:
            board[r][column] = player
            return True
    return False
def checkWinner(board, player):