from collections import deque


def is_safe(partial, row, col):
    for r in range(row):
        c = partial[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def find_path(N):
    """
    Uniform-Cost-like search where cost == depth (row). Equivalent to BFS by levels.
    Returns all complete solutions.
    """
    level = 0
    frontier = deque([[]])  # partial placements
    solutions = []

    while frontier:
        next_frontier = deque()
        while frontier:
            partial = frontier.popleft()
            row = len(partial)
            if row == N:
                solutions.append(partial)
                continue
            for col in range(N):
                if is_safe(partial, row, col):
                    next_frontier.append(partial + [col])
        level += 1
        frontier = next_frontier

    return solutions
