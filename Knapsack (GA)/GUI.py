import tkinter as tk
from tkinter import messagebox
from Genetic_Algorithm import *

# Hàm xử lý sự kiện khi nhấn nút "Chạy giải thuật"
def run_algorithm():
    try:
        weights_input = weights_entry.get().strip()
        values_input = values_entry.get().strip()
        max_capacity_input = max_capacity_entry.get().strip()

        if not weights_input or not values_input or not max_capacity_input:
            raise ValueError("Vui lòng nhập đầy đủ thông tin!")

        weights = list(map(int, weights_input.split(",")))
        values = list(map(int, values_input.split(",")))

        global max_capacity, items
        max_capacity = int(max_capacity_input)

        # Kiểm tra điều kiện max_capacity > 0
        if max_capacity <= 0:
            raise ValueError("Sức chứa tối đa phải lớn hơn 0!")

        if len(weights) != len(values):
            raise ValueError("Số lượng trọng lượng và giá trị không khớp!")

        items = list(zip(weights, values))

        set_problem_input(items, max_capacity)
        best_solution, best_fitness = genetic_algorithm()

        # Kiểm tra nếu không tìm ra giải pháp
        if best_fitness == 0:
            result_text.set("Không tìm ra giải pháp phù hợp.")
        else:
            result_text.set(
                f"Best solution: {best_solution}\n"
                f"Best value: {best_fitness}\n"
            )

    except ValueError as ve:
        messagebox.showerror("Lỗi nhập liệu", str(ve))
    except Exception as e:
        messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}\n")

# Hàm xử lý sự kiện khi nhấn nút "Reset"
def reset_fields():
    weights_entry.delete(0, tk.END)
    values_entry.delete(0, tk.END)
    max_capacity_entry.delete(0, tk.END)
    result_text.set("")

# Giao diện chính
root = tk.Tk()
root.title("Knapsack 0/1 (Genetic Algorithm)")
root.geometry("450x400")

# Các nhãn và ô nhập liệu 
tk.Label(root, text="Danh sách trọng lượng (cách nhau bằng dấu phẩy):", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
weights_entry = tk.Entry(root, width=50, font=("Arial", 11), relief="flat")
weights_entry.pack(anchor="w", padx=10)

tk.Label(root, text="Danh sách giá trị (cách nhau bằng dấu phẩy):", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
values_entry = tk.Entry(root, width=50, font=("Arial", 11), relief="flat")
values_entry.pack(anchor="w", padx=10)

tk.Label(root, text="Sức chứa tối đa:", font=("Arial", 11)).pack(anchor="w", padx=10, pady=5)
max_capacity_entry = tk.Entry(root, width=50, font=("Arial", 11), relief="flat")
max_capacity_entry.pack(anchor="w", padx=10)

# Khu vực chứa nút
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

# Nút "Run"
run_button = tk.Button(button_frame, text="Run", command=run_algorithm, bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), relief="flat")
run_button.pack(side="left", padx=10)

# Nút "Reset"
reset_button = tk.Button(button_frame, text="Reset", command=reset_fields, bg="#f44336", fg="white", font=("Arial", 12, "bold"), relief="flat")
reset_button.pack(side="left", padx=10)

# Khu vực hiển thị kết quả 
tk.Label(root, text="Kết quả:", font=("Arial", 11, "bold")).pack(anchor="w", padx=10, pady=5)
result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text, fg="blue", justify="left", wraplength=500, font=("Arial", 11))
result_label.pack(anchor="w", padx=10, pady=5)

# Chạy giao diện
root.mainloop()
