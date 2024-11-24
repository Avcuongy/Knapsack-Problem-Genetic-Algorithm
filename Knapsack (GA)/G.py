import tkinter as tk
from tkinter import ttk, messagebox
import tkinter.font as tkFont
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Các tham số thuật toán di truyền
POPULATION_SIZE = 200
GENERATIONS = 200
CROSSOVER_RATE = 0.8
MUTATION_RATE = 0.02

items = []  # Vật phẩm chứa weights và values
max_capacity = 0  # maximum capacity
fitness_history = [] # Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

# Hàm tính fitness cho một cá thể
def fitness(individual):
    total_weight = sum(individual[i] * items[i][0] for i in range(len(items)))
    total_value = sum(individual[i] * items[i][1] for i in range(len(items)))
    return total_value if total_weight <= max_capacity else 0

# Khởi tạo quần thể ban đầu
def initialize_population(num_items):
    return [[random.randint(0, 1) for _ in range(num_items)] for _ in range(POPULATION_SIZE)]

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

# Thuật toán di truyền
def genetic_algorithm():
    global fitness_history

    population = initialize_population(len(items))
    best_individual = max(population, key=lambda ind: fitness(ind))

    for gen in range(GENERATIONS):
        selected_population = select_population(population)

        offspring = []
        for i in range(0, len(selected_population), 2):
            if random.random() < CROSSOVER_RATE and i + 1 < len(selected_population):
                child1, child2 = crossover(
                    selected_population[i], selected_population[i + 1]
                )
                offspring.extend([child1, child2])
            else:
                offspring.extend([selected_population[i], selected_population[i + 1]])

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

class KnapsackGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Knapsack 0/1")
        self.root.geometry("350x290")

        default_font = tkFont.nametofont("TkDefaultFont")
        default_font.configure(family="Roboto", size=10)
        root.option_add("*Font", default_font)

        title_label = ttk.Label(root, text="Knapsack 0/1 Problem", font=("Roboto", 16, "bold"))
        title_label.pack(pady=10)

        input_frame = ttk.LabelFrame(root, text="Data", padding=10)
        input_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(input_frame, text="Weights (comma-separated):").pack(anchor="w")
        self.weights_entry = ttk.Entry(input_frame, width=50)
        self.weights_entry.pack(fill="x", pady=(0, 5))

        ttk.Label(input_frame, text="Values (comma-separated):").pack(anchor="w")
        self.values_entry = ttk.Entry(input_frame, width=50)
        self.values_entry.pack(fill="x", pady=(0, 5))

        ttk.Label(input_frame, text="Maximum Capacity:").pack(anchor="w")
        self.capacity_entry = ttk.Entry(input_frame, width=50)
        self.capacity_entry.pack(fill="x", pady=(0, 5))

        button_frame = ttk.Frame(root)
        button_frame.pack(pady=10)

        self.solve_button = ttk.Button(button_frame, text="Solve", command=self.solve)
        self.solve_button.pack(side="left", padx=5)

        self.reset_button = ttk.Button(button_frame, text="Reset", command=self.reset)
        self.reset_button.pack(side="left", padx=5)

    def validate_input(self):
        try:
            weights = [int(x.strip()) for x in self.weights_entry.get().split(",")]
            values = [int(x.strip()) for x in self.values_entry.get().split(",")]
            capacity = int(self.capacity_entry.get())

            if len(weights) != len(values):
                raise ValueError("Number of weights must match number of values.")
            if len(weights) == 0:
                raise ValueError("Please enter at least one item.")
            if capacity <= 0:
                raise ValueError("Capacity must be > than 0.")
            if any(w <= 0 for w in weights) or any(v <= 0 for v in values):
                raise ValueError("All weights and values must be > than 0.")

            return weights, values, capacity
        except ValueError as e:
            messagebox.showerror("Input Error", str(e))
            return None

    def solve(self):
        result = self.validate_input()
        if result is None:
            return

        weights, values, capacity = result
        global items, max_capacity, fitness_history
        items = list(zip(weights, values))
        max_capacity = capacity
        fitness_history = []

        best_solution, best_fitness = genetic_algorithm()

        if best_fitness == 0:
            messagebox.showwarning("Warning", "No valid solution found.")
            return

        total_weight = sum(best_solution[i] * items[i][0] for i in range(len(items)))

        self.show_solution(best_solution, best_fitness, total_weight)

    def show_solution(self, best_solution, best_fitness, total_weight):
        solution_window = tk.Toplevel(self.root)
        solution_window.title("Solution")
        solution_window.geometry("800x500")

        left_frame = ttk.Frame(solution_window, width=450, padding=10)
        left_frame.pack(side="left", fill="both", expand=True)
        right_frame = ttk.Frame(solution_window, width=450, padding=10)
        right_frame.pack(side="right", fill="both", expand=True)

        solution_text = "Selected items:\n\n"
        for i, (selected, (weight, value)) in enumerate(zip(best_solution, items)):
            if selected:
                solution_text += f"Item {i+1}: Weight={weight}, Value={value}\n"

        solution_text += f"\nSolution vector: {best_solution}\n"
        solution_text += f"Total Value: {best_fitness}\n"
        solution_text += f"Total Weight: {total_weight}/{max_capacity}"
        
        separator = ttk.Separator(left_frame, orient="horizontal")

        solution_label = ttk.Label(left_frame, text=solution_text, anchor="w", justify="left", wraplength=450)
        solution_label.pack(fill="both", expand=True)

        self.plot_fitness_history(right_frame)

    def plot_fitness_history(self, parent_frame):
        if not fitness_history:
            return

        fig, ax = plt.subplots(figsize=(6, 4))
        ax.plot(fitness_history, "b-", label="Fitness over generations")
        ax.set_title("Fitness History")
        ax.set_xlabel("Generation")
        ax.set_ylabel("Best Fitness")
        ax.grid(True)
        ax.legend()

        canvas = FigureCanvasTkAgg(fig, master=parent_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill="both", expand=True)

    def reset(self):
        self.weights_entry.delete(0, tk.END)
        self.values_entry.delete(0, tk.END)
        self.capacity_entry.delete(0, tk.END)

        global items, max_capacity, fitness_history
        items = []
        max_capacity = 0
        fitness_history = []

if __name__ == "__main__":
    root = tk.Tk()
    app = KnapsackGUI(root)
    root.mainloop()