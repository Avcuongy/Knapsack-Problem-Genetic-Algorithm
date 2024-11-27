import random

POPULATION_SIZE = 200  # Kích thước quần thể
GENERATIONS = 200  # Số thế hệ
CROSSOVER_RATE = 0.8  # Tỷ lệ lai ghép
MUTATION_RATE = 0.04  # Tỷ lệ đột biến

items = [] # Vật phẩm chứa weights và values
max_capacity = 0 # maximum capacity
fitness_history = [] # Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

# Khởi tạo quần thể
def initialize_population(num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(POPULATION_SIZE)]

# Tính fitness của cá thể
def fitness(individual):
    total_weight = sum(individual[i] * items[i][0] for i in range(len(items)))
    total_value = sum(individual[i] * items[i][1] for i in range(len(items)))
    return total_value if total_weight <= max_capacity else 0

# Chọn lọc elitism
def select_population(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:POPULATION_SIZE]

# Lai ghép Uniform
def crossover(parent1, parent2):
    child1, child2 = parent1[:], parent2[:]
    for i in range(len(parent1)):
        coin_flip = random.choice([0, 1])
        if coin_flip == 0:
            child1[i] = parent1[i]
            child2[i] = parent2[i]
        else:
            child1[i] = parent2[i]
            child2[i] = parent1[i]
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
