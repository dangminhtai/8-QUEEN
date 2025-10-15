def find_path(N):
    solutions = []
    board = [-1] * N

    def forward_check(row, available_cols):
        if row == N:
            solutions.append(board[:])
            return

        for col in list(available_cols[row]):
            board[row] = col

            # Sao chép trạng thái hiện tại của available_cols
            new_available = [cols.copy() for cols in available_cols]

            # Cập nhật lại domain cho các hàng phía dưới
            for r in range(row + 1, N):
                if col in new_available[r]:
                    new_available[r].remove(col)
                diag1 = col + (r - row)
                diag2 = col - (r - row)
                if diag1 in new_available[r]:
                    new_available[r].remove(diag1)
                if diag2 in new_available[r]:
                    new_available[r].remove(diag2)

                # Nếu hàng nào hết cột hợp lệ → cắt tỉa
                if not new_available[r]:
                    break
            else:
                # Chỉ tiếp tục nếu không hàng nào bị “bít”
                forward_check(row + 1, new_available)

            board[row] = -1

    # Khởi tạo domain: hàng nào cũng có thể chọn cột 0..N-1
    available_cols = [set(range(N)) for _ in range(N)]
    forward_check(0, available_cols)
    return solutions
