def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def dls(board, row, limit, N, out):
    if row == limit:
        if limit == N:
            out.append(board[:])
        return
    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            dls(board, row + 1, limit, N, out)
            board[row] = -1


def find_path(N):
    """
    Iterative Deepening over depth (rows) until reaching N; record complete solutions.
    Returns list of all valid solutions.
    """
    solutions = []
    seen = set()
    board = [-1] * N
    for limit in range(1, N + 1):
        level_solutions = []
        dls(board, 0, limit, N, level_solutions)
        for sol in level_solutions:
            t = tuple(sol)
            if len(sol) == N and t not in seen:
                seen.add(t)
                solutions.append(sol)
    return solutions
