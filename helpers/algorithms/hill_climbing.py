import random

def find_path(N, max_steps=100000, seed=42):
    """
    Tìm nghiệm N-queen bằng thuật toán hill climbing.
    Trả về list các state nếu tìm được, hoặc [] nếu không tìm được.
    """
    rng = random.Random(seed)
    solutions = []

    def conflicts(state):
        cnt = 0
        for i in range(len(state)):
            for j in range(i + 1, len(state)):
                if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                    cnt += 1
        return cnt

    attempts = N * 5  # thử nhiều lần để tìm nhiều nghiệm
    for _ in range(attempts):
        state = [rng.randrange(N) for _ in range(N)]
        current_conf = conflicts(state)

        for step in range(max_steps):
            if current_conf == 0:
                if state not in solutions:
                    solutions.append(state[:])
                break

            # Tìm nước đi tốt nhất trong cùng hàng
            best_move = None
            best_conf = current_conf

            for row in range(N):
                for col in range(N):
                    if col == state[row]:
                        continue
                    new_state = state[:]
                    new_state[row] = col
                    new_conf = conflicts(new_state)
                    if new_conf < best_conf:
                        best_conf = new_conf
                        best_move = (row, col)

            # Nếu không tìm được bước cải thiện => local optimum
            if best_move is None:
                break

            # Cập nhật trạng thái
            row, col = best_move
            state[row] = col
            current_conf = best_conf

    return solutions
