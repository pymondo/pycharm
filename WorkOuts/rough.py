def solveNQ(n):
    board = []
    for i in range(n):
        board.append([0] * n)
    if nqueen_util(board, 0) == True:
        display_board(board)
        return
    print("solution is not possible")


def nqueen_util(board, col):
    N = len(board[0])
    if col >= N:
        return True

    for row in range(N):
        if isSafe(board, row, col):
            board[row][col] = 1

            if nqueen_util(board, col + 1) == True:
                return True
            board[row][col] = 0
    return False


def isSafe(board, row, col):
    N = len(board[0])
    # chck for same row one codition
    for i in range(col):
        if board[row][i] == 1:
            return False

    # check top diagonal stuff
    for i, j in zip(range(col, -1, -1), range(row, -1, -1)):
        if board[i][j] == 1:
            return False

    for i , j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] ==1:
            return False
    return True

def display_board(board):
    for i in board:
        print(i)


solveNQ(4)
