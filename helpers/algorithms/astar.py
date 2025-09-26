def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def find_path(N):
    """
    Heuristic-guided DFS (A*-like ordering) for N-Queens.
    Returns list of all valid solutions.
    """
    solutions = []
    board = [-1] * N

    def heuristic_order(row):
        # Prefer center columns first to reduce branching on average
        cols = list(range(N))
        center = (N - 1) / 2.0
        cols.sort(key=lambda c: abs(c - center))
        return cols

    def search(row=0):
        if row == N:
            solutions.append(board[:])
            return
        for col in heuristic_order(row):
            if is_safe(board, row, col):
                board[row] = col
                search(row + 1)
                board[row] = -1

    search()
    return solutions
