# 1.Kiến trúc tích hợp: Học – Lập kế hoạch – Thực thi:
- Dyna kết hợp cả model-free learning (học trực tiếp) và model-based planning (lập kế hoạch dựa trên mô hình) trong cùng một vòng lặp
- Sau khi agent nhận tuple kinh nghiệm (s, a, r, s'), nó:
   + Cập nhật mô hình (learning): học xác suất chuyển trạng thái và phần thưởng dựa vào kinh nghiệm thực tế.
   + Thực hiện cập nhật Q-learning trực tiếp từ kinh nghiệm đó.
   + Tiếp đó, mô phỏng thêm k bước dựa trên mô hình để thực hiện nhiều round cập nhật Q giả tưởng (planning)
# 2. Mục tiêu:
- Mục tiêu chính là cải thiện sample efficiency bằng cách kết hợp cả kinh nghiệm thực và kinh nghiệm mô phỏng.
- Thay vì chỉ học qua môi trường thực, agent còn "mơ" ra các bước bổ sung nhờ mô hình để cập nhật thông tin mà không cần tương tác thậ
- Thư viện replay buffer trong các DQN cũng có thể coi là dạng mô hình đơn giản, cho phép cập nhật từ “giả tưởng” lưu trữ .
# 3. Hoạt động chi tiết:
- Sau mỗi kinh nghiệm thật:
  + Cập nhật mô hình (transition & reward).
  + Cập nhật Q(s,a) bằng công thức Q-learning:
    ![image](https://github.com/user-attachments/assets/11471df0-202f-477f-b9b4-82ca44b25d20)
  + Lặp k lần: lấy một cặp ngẫu nhiên (s̄, ā), dùng mô hình để sinh (r̄, s̄′), sau đó cập nhật Q(s̄,ā) tương tự
# 4.ưu điểm & Ứng dụng   
- Nhanh hội tụ hơn Q-learning dạng thuần, cần ít tương tác thực hơn .
- Linh hoạt trong sử dụng tài nguyên: có thể điều chỉnh số bước mô phỏng k dựa trên khả năng xử lý và tốc độ thu thập dữ liệu .
- Ứng dụng thực tế: Đặc biệt hữu ích trong robotics, môi trường mà tương tác thật tốn kém. Cũng nằm trong các ứng dụng của Dyna-Q và Dyna-Q+ như trong môi trường Maze .

