<div align="center">
  
# KNAPSACK 0/1

</div>

</div>

---
## Mô tả bài toán

Bài toán **Knapsack** là một bài toán tối ưu hóa cổ điển trong đó mục tiêu là chọn một tập hợp các vật phẩm từ một danh sách sao cho tổng giá trị của chúng là lớn nhất, đồng thời tổng trọng lượng không vượt quá một giới hạn cho phép (khối lượng của ba lô). Mỗi vật phẩm có một giá trị và trọng lượng nhất định, và chúng ta cần tìm ra một tập hợp các vật phẩm tối ưu.

---

## Mô tả thuật toán di truyền (Genetic Algorithm)

Thuật toán di truyền (GA) được sử dụng để giải quyết bài toán này bằng cách mô phỏng quá trình tiến hóa của tự nhiên.

Điều đầu tiền mình cần phải có là:
- Danh sách chứa thông tin về các vật phẩm trong bài toán cái ba lô, bao gồm trọng lượng và giá trị của mỗi vật phẩm.
- Dung lượng tối đa của cái ba lô trong bài toán.
- Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

Các bước chính trong thuật toán di truyền bao gồm:

1. **Khởi tạo quần thể**:  
   Quần thể ban đầu gồm các cá thể được tạo ngẫu nhiên, mỗi cá thể đại diện cho một tập hợp các vật phẩm.

2. **Chọn lọc (Selection)**:  
   Các cá thể có fitness tốt được chọn để sinh sản, dựa trên giá trị tổng hợp (sự phù hợp) của chúng đối với bài toán knapsack.

3. **Lai ghép (Crossover)**:  
   Các cá thể được lai ghép để tạo ra các cá thể con, mô phỏng sự kết hợp gene từ hai cá thể cha mẹ.

4. **Đột biến (Mutation)**:  
   Một tỷ lệ nhất định các cá thể trong quần thể sẽ được đột biến, tức là thay đổi một phần tử trong gene của chúng để tăng tính đa dạng trong quần thể.

5. **Cập nhật quần thể**:  
   Các cá thể con thay thế các cá thể cũ, và quá trình tiếp tục qua nhiều thế hệ.

6. **Kết quả**:  
   Quá trình tiến hóa tiếp tục cho đến khi đạt được số thế hệ tối đa, và cá thể có fitness cao nhất được chọn làm giải pháp tối ưu cho bài toán.


## Cài đặt
Clone repository về máy của bạn:
   ```bash
   git clone https://github.com/ThojTran/Knapsack-Problem-Genetic-Algorithm.git
