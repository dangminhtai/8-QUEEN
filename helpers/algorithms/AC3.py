from collections import deque

def find_path(N):
    solutions = []
    vars = list(range(N))  # mỗi hàng là một biến
    domains = {v: set(range(N)) for v in vars}  # mỗi hàng có thể chọn cột 0..N-1

    # ràng buộc: không cùng cột, không cùng đường chéo
    def constraint(x, x_val, y, y_val):
        return x_val != y_val and abs(x - y) != abs(x_val - y_val)

    # tạo danh sách các cung (arc)
    def all_arcs():
        arcs = []
        for xi in vars:
            for xj in vars:
                if xi != xj:
                    arcs.append((xi, xj))
        return arcs

    # AC3 propagation
    def ac3(domains):
        queue = deque(all_arcs())
        while queue:
            xi, xj = queue.popleft()
            if revise(domains, xi, xj):
                if not domains[xi]:
                    return False  # domain rỗng → vô nghiệm
                for xk in vars:
                    if xk != xi and xk != xj:
                        queue.append((xk, xi))
        return True

    # revise: loại bỏ giá trị vi phạm ràng buộc
    def revise(domains, xi, xj):
        revised = False
        for x in list(domains[xi]):
            if not any(constraint(xi, x, xj, y) for y in domains[xj]):
                domains[xi].remove(x)
                revised = True
        return revised

    # backtracking + AC3
    def backtrack(assignment, domains):
        if len(assignment) == N:
            solutions.append([assignment[i] for i in range(N)])
            return

        # chọn biến chưa gán có domain nhỏ nhất (MRV heuristic)
        unassigned = [v for v in vars if v not in assignment]
        var = min(unassigned, key=lambda v: len(domains[v]))

        for value in list(domains[var]):
            new_assignment = assignment.copy()
            new_assignment[var] = value

            new_domains = {v: domains[v].copy() for v in vars}
            new_domains[var] = {value}

            if ac3(new_domains):
                backtrack(new_assignment, new_domains)

    backtrack({}, domains)
    return solutions
