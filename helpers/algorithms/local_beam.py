# helpers/algorithms/beam.py
import random

def conflicts(state):
    n = len(state)
    cnt = 0
    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == j - i:
                cnt += 1
    return cnt

def find_path(N, beam_width=5, max_steps=1000, seed=None):
    """
    Local Beam Search for N-Queens.
    Returns [solution] (one solution) or [] if not found.
    """
    rng = random.Random(seed)

    # khởi tạo beam gồm các trạng thái khác nhau
    beams = []
    seen = set()
    attempts = 0
    while len(beams) < beam_width and attempts < beam_width * 10:
        st = tuple(rng.randrange(N) for _ in range(N))
        if st not in seen:
            seen.add(st)
            beams.append(list(st))
        attempts += 1
    if not beams:
        beams = [ [rng.randrange(N) for _ in range(N)] ]

    # nếu bất kỳ beam ban đầu là nghiệm thì trả về luôn
    for b in beams:
        if conflicts(b) == 0:
            return [b]

    for step in range(max_steps):
        candidates = []
        # sinh neighbor của mọi beam (di chuyển 1 hậu sang cột khác)
        for b in beams:
            for row in range(N):
                for col in range(N):
                    if col == b[row]:
                        continue
                    nb = b.copy()
                    nb[row] = col
                    key = tuple(nb)
                    if key in seen:
                        continue
                    seen.add(key)
                    candidates.append((conflicts(nb), nb))

        # cũng cho phép giữ nguyên trạng thái hiện tại (không đổi)
        for b in beams:
            candidates.append((conflicts(b), b))

        if not candidates:
            break

        # sắp xếp theo score (số xung đột) thấp trước
        candidates.sort(key=lambda x: x[0])

        # chọn top-k duy nhất làm beam cho bước tiếp
        new_beams = []
        added = set()
        for score, state in candidates:
            k = tuple(state)
            if k in added:
                continue
            new_beams.append(state)
            added.add(k)
            if len(new_beams) >= beam_width:
                break

        beams = new_beams

        # kiểm tra nghiệm
        for b in beams:
            if conflicts(b) == 0:
                return [b]

    # không tìm được
    return []
