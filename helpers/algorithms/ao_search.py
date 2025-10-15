def find_path(N):
    solutions = []
    
    def is_safe(board, row, col):
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    # OR-search: chọn một cột để đặt hậu ở hàng row
    def or_search(board, row):
        if row == N:
            solutions.append(board[:])
            return
        for col in range(N):
            if is_safe(board, row, col):
                board[row] = col
                # AND-search: phải giải quyết tiếp cho row+1..N-1
                and_search(board, row + 1)
                board[row] = -1

    # AND-search: giải cho phần còn lại của bàn cờ
    def and_search(board, row):
        if row == N:
            solutions.append(board[:])
            return
        or_search(board, row)

    or_search([-1]*N, 0)
    return solutions