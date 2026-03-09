"""
Name: Oliver Noll
Section:
Description: Lab  - Connect 4 
"""
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
    rows = len(board)
    cols = len(board[0])
    for r in range(rows):
        for c in range(cols - 3):
            if (board[r][c] == player and board[r][c+1] == player and
                board[r][c+2] == player and board[r][c+3] == player):
                return True
    for r in range(rows - 3):
        for c in range(cols):
            if (board[r][c] == player and board[r+1][c] == player and
                board[r+2][c] == player and board[r+3][c] == player):
                return True
    for r in range(rows - 3):
        for c in range(cols - 3):
            if (board[r][c] == player and board[r+1][c+1] == player and
                board[r+2][c+2] == player and board[r+3][c+3] == player):
                return True
    for r in range(rows - 3):
        for c in range(3, cols):
            if (board[r][c] == player and board[r+1][c-1] == player and
                board[r+2][c-2] == player and board[r+3][c-3] == player):
                return True
    return False
def boardFull(board):
    for row in board:
        if 0 in row:
            return False
    return True
def main():
    ROWS = 6
    COLUMNS = 7
    BOARD = [
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0],
    ]
    PLAYER = "X"
    while True:
        drawBoard(BOARD)
        print(f"\nPlayer {PLAYER}'s turn")
        user_col = input("Choose a column (1-7): ").strip()
        if not user_col.isdigit():
            print("Enter a number from 1 to 7.")
            continue
        col = int(user_col)
        if col < 1 or col > COLUMNS:
            print("Column must be 1-7.")
            continue
        col_index = col - 1
        if not dropPiece(BOARD, PLAYER, col_index):
            print("That column is full..")
            continue
        if checkWinner(BOARD, PLAYER):
            drawBoard(BOARD)
            print(f"\nPlayer {PLAYER} WINS!")
            break
        if boardFull(BOARD):
            drawBoard(BOARD)
            print("\nTie game! ")
            break
    PLAYER = switchPlayer(PLAYER)
if __name__ == "__main__":
     main() 
    