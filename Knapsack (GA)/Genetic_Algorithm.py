import random

POPULATION_SIZE = 200  # Kích thước quần thể
GENERATIONS = 200  # Số thế hệ
CROSSOVER_RATE = 0.8  # Tỷ lệ lai ghép
MUTATION_RATE = 0.02  # Tỷ lệ đột biến

items = [] # Vật phẩm chứa weights và values
max_capacity = 0 # maximum capacity
fitness_history = [] # Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

def get_user_input():
    global items, max_capacity
    
    weights_str = input("Nhập danh sách trọng lượng (phân tách bằng dấu phẩy): ")
    values_str = input("Nhập danh sách giá trị (phân tách bằng dấu phẩy): ")
    max_capacity = int(input("Nhập sức chứa tối đa: "))
    
    weights = list(map(int, weights_str.split(",")))
    values = list(map(int, values_str.split(",")))
    items = list(zip(weights, values))
    
    return items, max_capacity

def get_info():
    print("\nThông tin bài toán:\n")
    stt = 1
    for weight, value in items:
        print(f"Vật phẩm {stt}: Weight = {weight}, Value = {value}")
        stt += 1
    print(f"\nMaximum capacity = {max_capacity}")

def fitness(individual):
    total_weight = sum(individual[i] * items[i][0] for i in range(len(items)))
    total_value = sum(individual[i] * items[i][1] for i in range(len(items)))
    return total_value if total_weight <= max_capacity else 0

def initialize_population(num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(POPULATION_SIZE)]

# Chọn lọc elitism
def select_population(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:POPULATION_SIZE]

# Lai ghép One-point
def crossover(parent1, parent2):
    if len(parent1) <= 1 or len(parent2) <= 1:
        return parent1, parent2
    crossover_point = random.randint(1, len(parent1) - 1)
    child1 = parent1[:crossover_point] + parent2[crossover_point:]
    child2 = parent2[:crossover_point] + parent1[crossover_point:]
    return child1, child2

# Đột biến Bit-flip
def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual

def genetic_algorithm():
    global fitness_history
    
    population = initialize_population(len(items))
    best_individual = max(population, key=lambda ind: fitness(ind))

    for gen in range(GENERATIONS):
        selected_population = select_population(population)
        
        num_to_crossover = int(POPULATION_SIZE * CROSSOVER_RATE)
        selected_for_crossover = selected_population[:num_to_crossover]
        
        offspring = []
        for i in range(0, num_to_crossover, 2):
            if i + 1 < len(selected_for_crossover):
                child1, child2 = crossover(selected_for_crossover[i], selected_for_crossover[i + 1])
                offspring.extend([child1, child2])
        
        offspring = [mutate(ind) for ind in offspring]
        
        # Cắt tỉa quần thể để đảm bảo kích thước không vượt quá POPULATION_SIZE
        population.extend(offspring)
        population = sorted(population, key=lambda ind: fitness(ind), reverse=True)
        population = population[:POPULATION_SIZE]
        
        current_best = max(population, key=lambda ind: fitness(ind))
        fitness_history.append(fitness(current_best))
        
        if fitness(current_best) > fitness(best_individual):
            best_individual = current_best

    return best_individual, fitness(best_individual)
