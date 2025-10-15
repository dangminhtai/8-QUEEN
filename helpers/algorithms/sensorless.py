
def find_path(N):
    solutions = []

    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True
    def transition(belief, row, col):
        next_belief = []
        for board in belief:
            if is_safe(board, row, col):
                new_board = board[:]
                new_board[row] = col
                next_belief.append(new_board)
        return next_belief

    def dfs(row, belief):
        if row == N:
            # Nếu tất cả board trong belief đều full N quân
            if all(-1 not in board for board in belief):
                solutions.extend(belief)
            return

        for col in range(N):
            new_belief = transition(belief, row, col)
            if new_belief:  
                dfs(row + 1, new_belief)

    initial_belief = [[-1] * N]
    dfs(0, initial_belief)
    return solutions

