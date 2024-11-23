import tkinter as tk
from tkinter import messagebox
from Genetic_Algorithm import *  # Import tất cả từ Genetic_Algorithm

# Hàm xử lý sự kiện khi nhấn nút "Chạy giải thuật"
def run_algorithm():
    try:
        # Kiểm tra nhập liệu
        weights_input = weights_entry.get().strip()
        values_input = values_entry.get().strip()
        max_capacity_input = max_capacity_entry.get().strip()

        if not weights_input or not values_input or not max_capacity_input:
            raise ValueError("Vui lòng nhập đầy đủ thông tin!")

        # Chuyển đổi đầu vào thành danh sách
        weights = list(map(int, weights_input.split(",")))
        values = list(map(int, values_input.split(",")))
        
        global max_capacity, items
        
        # Cập nhật lại giá trị max_capacity và items
        max_capacity = int(max_capacity_input)
        if len(weights) != len(values):
            raise ValueError("Số lượng trọng lượng và giá trị không khớp!")

        items = list(zip(weights, values))

        # Gọi hàm trong G_A.py để thiết lập giá trị đầu vào
        set_problem_input(items, max_capacity)
        
        # Chạy thuật toán
        best_solution, best_fitness = genetic_algorithm()

        # Hiển thị kết quả
        result_text.set(
            f"Best solution: {best_solution}\n"
            f"Best value: {best_fitness}\n"
        )

    except ValueError as ve:
        messagebox.showerror("Lỗi nhập liệu", str(ve))
    except Exception as e:
        #import traceback
        #error_details = traceback.format_exc()  # Lấy thông tin chi tiết về lỗi
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}\n")

# Giao diện chính
root = tk.Tk()
root.title("Knapsack 0/1 (Genetic Algorithm)")
root.geometry("600x400")

# Các nhãn và ô nhập liệu 
tk.Label(root, text="Danh sách trọng lượng (cách nhau bằng dấu phẩy):", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
weights_entry = tk.Entry(root, width=50, font=("Arial", 11))
weights_entry.pack(anchor="w", padx=10)

tk.Label(root, text="Danh sách giá trị (cách nhau bằng dấu phẩy):", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
values_entry = tk.Entry(root, width=50, font=("Arial", 11))
values_entry.pack(anchor="w", padx=10)

tk.Label(root, text="Sức chứa tối đa:", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
max_capacity_entry = tk.Entry(root, width=50, font=("Arial", 11))
max_capacity_entry.pack(anchor="w", padx=10)

# Nút chạy giải thuật 
run_button = tk.Button(root, text="Run", command=run_algorithm, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"))
run_button.pack(pady=10)

# Khu vực hiển thị kết quả 
tk.Label(root, text="Kết quả:", font=("Arial", 11, "bold")).pack(anchor="w", padx=10, pady=5)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, fg="blue", justify="left", wraplength=500, font=("Arial", 11))
result_label.pack(anchor="w", padx=10, pady=5)

# Chạy giao diện
root.mainloop()
