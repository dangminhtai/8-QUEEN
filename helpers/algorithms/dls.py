def is_safe(board, row, col):
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def dls(board, row, limit, N, out):
    if row == limit:
        # reached depth limit; if limit==N and filled N rows, record solution
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
    Depth-Limited Search: increase limit from 1..N and enumerate solutions at depth N.
    Returns list of all valid solutions.
    """
    solutions = []
    board = [-1] * N
    for limit in range(1, N + 1):
        dls(board, 0, limit, N, solutions)
    # Remove duplicates (in case multiple passes recorded same complete boards)
    unique = []
    seen = set()
    for sol in solutions:
        t = tuple(sol)
        if len(sol) == N and t not in seen:
            seen.add(t)
            unique.append(sol)
    return unique
