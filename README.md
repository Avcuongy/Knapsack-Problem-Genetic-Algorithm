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

## Các bước chính trong thuật toán di truyền bao gồm

--- 

1. **Khởi tạo quần thể**:

   ``` initialize_population ``` Quần thể ban đầu gồm các cá thể được tạo ngẫu nhiên, mỗi cá thể đại diện cho một tập hợp các vật phẩm.
      
2. **Đánh giá quần thể**:
   ``` fitness ``` Fitness của mỗi cá thể được tính dựa trên số vật phẩm được chọn và tính tổng value của số vật phẩm được chọn.
   
3. **Chọn lọc (Selection)**:  
   ``` select_population ``` Các cá thể có fitness tốt được chọn để sinh sản, dựa trên giá trị tổng hợp (sự phù hợp) của chúng đối với bài toán knapsack.
   
4. **Lai ghép (Crossover)**:  
   ``` crossover ``` Các cá thể được lai ghép để tạo ra các cá thể con, mô phỏng sự kết hợp gene từ hai cá thể cha mẹ.
   
5. **Đột biến (Mutation)**:  
   ``` mutate ``` Một tỷ lệ nhất định các cá thể trong quần thể sẽ được đột biến, tức là thay đổi một phần tử trong gene của chúng để tăng tính đa dạng trong quần thể.
   
6. **Triển khai thuật toán**:  
   ``` genetic_algorithm ``` Tối ưu hóa tổng giá trị của các vật phẩm và cập nhật quần thể qua từng thế hệ được chọn trong ba lô mà không vượt quá giới hạn trọng lượng cho phép và cuối cùng sẽ trả về kết quả tốt nhất.

---
**Kết quả**:

   Quá trình tiến hóa tiếp tục cho đến khi đạt được số thế hệ tối đa, và cá thể có fitness cao nhất được chọn làm giải pháp tối ưu cho bài toán.

## Cài đặt
Clone repository về máy của bạn:
