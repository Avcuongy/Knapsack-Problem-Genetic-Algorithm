import random

# Dữ liệu cho bài toán Knapsack (Danh sách các vật phẩm với trọng lượng và giá trị)
def parse_items(weights_str, values_str):
    weights = list(map(int, weights_str.split(',')))
    values = list(map(int, values_str.split(',')))
    items = list(zip(weights, values))
    return items

# Input Problem
def get_user_input():
    weights_str = input("Nhập danh sách trọng lượng (phân tách bằng dấu phẩy): ")
    values_str = input("Nhập danh sách giá trị (phân tách bằng dấu phẩy): ")
    max_capacity = int(input("Maximum capacity: "))
    return parse_items(weights_str, values_str), max_capacity
   
# Lấy dữ liệu đầu vào và chuyển thành danh sách items và sức chứa
items, max_capacity = None, None
  
# Info Problem
def get_info(items,max_capacity):
    stt = 1;
    for weight, value in items:
        print(f"Vật phẩm {stt}: Weight = {weight}, Value = {value}")
        stt+=1
    print(f"\nMaximum capacity = {max_capacity}")
    
  
# Các tham số của thuật toán di truyền
population_size = 200
generations = 200
crossover_rate = 0.8
mutation_rate = 0.02
elitism = True
k = 3

# Lưu trữ giá trị fitness tốt nhất qua các thế hệ
fitness_history = []

# Hàm tính điểm thích nghi (fitness function)
def fitness(individual):
    total_weight = 0
    total_value = 0
    for i in range(len(individual)):
        if individual[i] == 1:
            total_weight += items[i][0]
            total_value += items[i][1]
    if total_weight > max_capacity:
        return 0 
    else:
        return total_value

# Khởi tạo quần thể ngẫu nhiên
def initialize_population():
    return [[random.randint(0, 1) for _ in range(len(items))] for _ in range(population_size)]

# Lựa chọn cá thể dựa trên Tournament Selection
def selection(population): 
    selected = []
    
    # Chọn lọc ưu tú (Elitism): Giữ lại cá thể tốt nhất
    selected.append(population[0])
    
    # Chọn lọc đấu giá (Tournament)
    for _ in range(population_size - 1):
        tournament = random.sample(population, k)
        winner = max(tournament, key=fitness)
        selected.append(winner)
    return selected

# Lai ghép (1-point crossover)
def crossover(parent1, parent2):
    if random.random() < crossover_rate:
        point = random.randint(1, len(items) - 1)
        child1 = parent1[:point] + parent2[point:]
        child2 = parent2[:point] + parent1[point:]
        return [child1, child2]
    else:
        return [parent1, parent2]

# Đột biến (Mutation)
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < mutation_rate:
            individual[i] = 1 - individual[i]
    return individual

# Hàm chính cho thuật toán di truyền
def genetic_algorithm():
    population = initialize_population()
    
    for generation in range(generations):
        # Đánh giá quần thể
        population = sorted(population, key=fitness, reverse=True)

        # Lưu lại cá thể tốt nhất
        best_solution = population[0]
        best_fitness = fitness(best_solution)

        parents = selection(population)

        # Tạo ra quần thể mới, bắt đầu với cá thể tốt nhất
        new_population = [best_solution]  # Giữ lại cá thể tốt nhất

        # Lai ghép các cá thể cha mẹ để tạo ra thế hệ mới
        for i in range(0, len(parents), 2):
            if i + 1 < len(parents):
                parent1, parent2 = parents[i], parents[i + 1]
                children = crossover(parent1, parent2)
                new_population.extend(children)
            else:
                new_population.append(parents[i])  # Nếu chỉ có 1 cá thể cha mẹ còn lại

        # Đột biến
        new_population = [mutate(individual) for individual in new_population]

        # Cập nhật quần thể
        population = new_population

        # Ghi lại lời giải tốt nhất mỗi thế hệ
        fitness_history.append(best_fitness)

    # Kết quả tốt nhất sau các thế hệ
    best_solution = max(population, key=fitness)
    print("\nBest solution:", best_solution)
    print("Best fitness:", fitness(best_solution))



