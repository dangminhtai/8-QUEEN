from collections import deque


def is_safe(partial, row, col):
    # partial: list of columns for rows [0..row-1]
    for r in range(row):
        c = partial[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def find_path(N):
    """
    Breadth-First Search over partial N-Queens placements.
    Returns list of complete solutions, each solution is a list where
    solution[row] = column of the queen in that row.
    """
    solutions = []
    # Queue holds partial placements (list of columns), level = number of rows placed
    q = deque()
    q.append([])

    while q:
        partial = q.popleft()
        row = len(partial)
        if row == N:
            solutions.append(partial)
            continue
        for col in range(N):
            if is_safe(partial, row, col):
                q.append(partial + [col])

    return solutions
