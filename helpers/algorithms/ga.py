import random

def find_path(N, population_size=100, generations=1000, mutation_rate=0.1, seed=42):
    """
    Tìm nghiệm N-queen bằng thuật toán di truyền (GA).
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

    # Khởi tạo quần thể ngẫu nhiên
    population = [[rng.randrange(N) for _ in range(N)] for _ in range(population_size)]

    for gen in range(generations):
        # Tính fitness (số cặp queen không attack nhau)
        fitness = [N*(N-1)//2 - conflicts(ind) for ind in population]

        # Kiểm tra nghiệm hoàn hảo
        for i, fit in enumerate(fitness):
            if fit == N*(N-1)//2 and population[i] not in solutions:
                solutions.append(population[i][:])
                if len(solutions) >= 10:  # giới hạn số nghiệm lưu
                    return solutions

        # Chọn cha mẹ theo roulette wheel
        total_fitness = sum(fitness)
        if total_fitness == 0:
            continue
        probs = [f/total_fitness for f in fitness]

        new_population = []
        for _ in range(population_size):
            parents = rng.choices(population, probs, k=2)
            # Crossover 1 điểm
            point = rng.randrange(1, N)
            child = parents[0][:point] + parents[1][point:]
            # Mutation
            if rng.random() < mutation_rate:
                row = rng.randrange(N)
                child[row] = rng.randrange(N)
            new_population.append(child)

        population = new_population

    return solutions
