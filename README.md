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

### Tham số bài toán 
- Danh sách chứa thông tin về các vật phẩm trong bài toán cái ba lô, bao gồm trọng lượng và giá trị của mỗi vật phẩm.
- Dung lượng tối đa của cái ba lô trong bài toán.
- Danh sách lưu trữ giá trị fitness của các cá thể tốt nhất qua từng thế hệ.

## Các bước chính trong thuật toán di truyền bao gồm

--- 

1. **Khởi tạo quần thể**:  
   Quần thể ban đầu gồm các cá thể được tạo ngẫu nhiên, mỗi cá thể đại diện cho một tập hợp các vật phẩm.
   
   ``` initialize_population ``` được thiết kế để thực hiện quá trình này.
   
2. **Đánh giá quần thể**:
   Fitness của mỗi cá thể được tính dựa trên số vật phẩm được chọn và tính tổng value của số vật phẩm được chọn.
   
   ``` fitness ```được thiết kế để thực hiện quá trình này.
     
3. **Chọn lọc (Selection)**:  
   Các cá thể có fitness tốt được chọn để sinh sản, dựa trên giá trị tổng hợp (sự phù hợp) của chúng đối với bài toán knapsack.
   
   ``` select_population ``` được thiết kế để thực hiện quá trình này.
   
4. **Lai ghép (Crossover)**:  
   Các cá thể được lai ghép để tạo ra các cá thể con, mô phỏng sự kết hợp gene từ hai cá thể cha mẹ.
   
   ``` crossover ``` được thiết kế để thực hiện quá trình này.
   
5. **Đột biến (Mutation)**:  
   Một tỷ lệ nhất định các cá thể trong quần thể sẽ được đột biến, tức là thay đổi một phần tử trong gene của chúng để tăng tính đa dạng trong quần thể.
   
   ``` mutate ``` được thiết kế để thực hiện quá trình này.
   
6. **Triển khai thuật toán**:  
   Tối ưu hóa tổng giá trị của các vật phẩm và cập nhật quần thể qua từng thế hệ được chọn trong ba lô mà không vượt quá giới hạn trọng lượng cho phép và cuối cùng sẽ trả về kết quả tốt nhất.

   ``` genetic_algorithm ``` triển khai thuật toán di truyền, thực hiện các bước cơ bản của quá trình tiến hóa để tìm kiếm giải pháp tối ưu.

---
**Kết quả**:

   Quá trình tiến hóa tiếp tục cho đến khi đạt được số thế hệ tối đa, và cá thể có fitness cao nhất được chọn làm giải pháp tối ưu cho bài toán.

## Cài đặt
Clone repository về máy của bạn:
   ```bash
   git clone https://github.com/ThojTran/Knapsack-Problem-Genetic-Algorithm.git
