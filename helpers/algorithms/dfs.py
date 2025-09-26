# helpers/algorithms/dfs.py
def find_path(N):
    solutions = []
    board = [-1] * N

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def dfs(row=0):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(row, col):
                board[row] = col
                dfs(row + 1)
                board[row] = -1

    dfs()
    return solutions
