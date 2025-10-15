def find_path(N):
    solutions = []
    board = [-1] * N

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == N:
            solutions.append(board[:])
            return

        for col in range(N):
            if is_safe(row, col):
                board[row] = col        # đặt quân hậu
                backtrack(row + 1)      # thử hàng tiếp theo
                board[row] = -1         # quay lui (bỏ quân hậu)

    backtrack(0)
    return solutions
