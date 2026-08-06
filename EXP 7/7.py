N = 4

board = [[0] * N for _ in range(N)]


def is_safe(board, row, col):

    for i in range(col):
        if board[row][i]:
            return False

    i = row
    j = col
    while i >= 0 and j >= 0:
        if board[i][j]:
            return False
        i -= 1
        j -= 1

    i = row
    j = col
    while i < N and j >= 0:
        if board[i][j]:
            return False
        i += 1
        j -= 1

    return True


def solve(board, col):

    if col >= N:
        return True

    for i in range(N):

        if is_safe(board, i, col):

            board[i][col] = 1

            if solve(board, col + 1):
                return True

            board[i][col] = 0

    return False


if solve(board, 0):

    print("Solution:")

    for row in board:
        print(row)

else:
    print("No Solution")
