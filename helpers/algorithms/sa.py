# helpers/algorithms/sa.py
import random
import math

def conflicts(state):
    """Đếm số cặp quân hậu tấn công nhau"""
    n = len(state)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                cnt += 1
    return cnt


def find_path(N, max_steps=100000, seed=42):
    rng = random.Random(seed)

    # Khởi tạo trạng thái ngẫu nhiên
    state = [rng.randrange(N) for _ in range(N)]
    current_conf = conflicts(state)

    # Nhiệt độ ban đầu
    T = N * N

    for step in range(max_steps):
        if current_conf == 0:
            return [state]   # trả về dạng list để đồng bộ với dfs

        # Chọn hàng random và cột mới random
        row = rng.randrange(N)
        new_col = rng.randrange(N)
        old_col = state[row]

        if new_col == old_col:
            continue

        # Tạo trạng thái mới
        new_state = state[:]
        new_state[row] = new_col
        new_conf = conflicts(new_state)

        delta = new_conf - current_conf
        # Quyết định chấp nhận
        if delta < 0 or rng.random() < math.exp(-delta / T):
            state = new_state
            current_conf = new_conf

        # Giảm nhiệt độ
        T *= 0.995
        if T < 1e-6:
            break

    # Nếu không tìm thấy nghiệm hợp lệ
    return []
