<div align="center">
  
# KNAPSACK 0/1
<img src="https://github.com/Avcuongy/Avcuongy/blob/main/Pictures/Knapsack.svg.png" width="350" height="300">

</div>

---
## Mô tả bài toán

Bài toán **Knapsack** là một bài toán tối ưu hóa cổ điển trong đó mục tiêu là chọn một tập hợp các vật phẩm từ một danh sách sao cho tổng giá trị của chúng là lớn nhất, đồng thời tổng trọng lượng không vượt quá một giới hạn cho phép (khối lượng của ba lô). Mỗi vật phẩm có một giá trị và trọng lượng nhất định, và chúng ta cần tìm ra một tập hợp các vật phẩm tối ưu.

---

## Mô tả thuật toán di truyền (Genetic Algorithm)

Thuật toán di truyền (GA) được sử dụng để giải quyết bài toán này bằng cách mô phỏng quá trình tiến hóa của tự nhiên.

# Tham số bài toán 
- Danh sách chứa thông tin về các vật phẩm trong bài toán cái ba lô, bao gồm trọng lượng và giá trị của mỗi vật phẩm.
- Dung lượng tối đa của cái ba lô trong bài toán.
- Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

Các bước chính trong thuật toán di truyền bao gồm:

1. **Khởi tạo quần thể**:  
   Quần thể ban đầu gồm các cá thể được tạo ngẫu nhiên, mỗi cá thể đại diện cho một tập hợp các vật phẩm.
   
   Hàm initialize_population được thiết kế để thực hiện quá trình này.
   
   ```
   def initialize_population(num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(POPULATION_SIZE)]
   ```
   
2. **Tính toán**:
   Fitness của mỗi cá thể được tính dựa trên số vật phẩm được chọn và tính tổng value của số vật phẩm được chọn.
   
   Hàm fitness được thiết kế để thực hiện quá trình này.
   
   ```
   def fitness(individual):
    total_weight = sum(individual[i] * items[i][0] for i in range(len(items)))
    total_value = sum(individual[i] * items[i][1] for i in range(len(items)))
    return total_value if total_weight <= max_capacity else 0
   ```
   
3. **Chọn lọc (Selection)**:  
   Các cá thể có fitness tốt được chọn để sinh sản, dựa trên giá trị tổng hợp (sự phù hợp) của chúng đối với bài toán knapsack.
   
   Hàm select_population được thiết kế để thực hiện quá trình này.
   
   ```
   def select_population(population):
    sorted_population = sorted(population, key=lambda x: fitness(x), reverse=True)
    return sorted_population[:POPULATION_SIZE]
   ```
   
4. **Lai ghép (Crossover)**:  
   Các cá thể được lai ghép để tạo ra các cá thể con, mô phỏng sự kết hợp gene từ hai cá thể cha mẹ.
   
   Hàm crossover được thiết kế để thực hiện quá trình này.
   
   ```
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
   ```

5. **Đột biến (Mutation)**:  
   Một tỷ lệ nhất định các cá thể trong quần thể sẽ được đột biến, tức là thay đổi một phần tử trong gene của chúng để tăng tính đa dạng trong quần thể.
   
   Hàm mutate được thiết kế để thực hiện quá trình này.
   
   ```
   def mutate(individual):
    for i in range(len(individual)):
        if random.random() < MUTATION_RATE:
            individual[i] = 1 - individual[i]
    return individual
   ```
   
6. **Triễn khai thuật toán**:  
   Tối ưu hóa tổng giá trị của các vật phẩm và cập nhật quần thể qua từng thế hệ được chọn trong ba lô mà không vượt quá giới hạn trọng lượng cho phép .
   Và Cuối cùng trả về kết quả tốt nhất.

   Hàm genetic_algorithm triển khai thuật toán di truyền, thực hiện các bước cơ bản của quá trình tiến hóa để tìm kiếm giải pháp tối ưu.
   
   ```
   def genetic_algorithm():
    global fitness_history
    
    population = initialize_population(len(items))
    best_individual = max(population, key=lambda ind: fitness(ind))

    for gen in range(GENERATIONS):
        selected_population = select_population(population)
        
        offspring = []
        for i in range(0, len(selected_population), 2):
            if random.random() < CROSSOVER_RATE and i+1 < len(selected_population):
                child1, child2 = crossover(selected_population[i], selected_population[i+1])
                offspring.extend([child1, child2])
            else:
                offspring.extend([selected_population[i], selected_population[i+1]])

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
    ```

**Kết quả**:

   Quá trình tiến hóa tiếp tục cho đến khi đạt được số thế hệ tối đa, và cá thể có fitness cao nhất được chọn làm giải pháp tối ưu cho bài toán.


## Cài đặt
Clone repository về máy của bạn:
   ```bash
   git clone https://github.com/ThojTran/Knapsack-Problem-Genetic-Algorithm.git
