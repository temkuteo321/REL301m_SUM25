# 1.Q-learning:
- Là một thuật toán reinforcement learning model‑free (không cần biết trước mô hình môi trường), dựa trên TD (Temporal‑Difference) để tìm chính sách tối ưu trong MDP hữu hạn
- “Q” trong Q‑learning là viết tắt của Quality: giá trị hay chất lượng của một hành động trong trạng thái cụ thể
# 2.On‑policy vs Off‑policy:
- Q‑learning là một thuật toán off‑policy: chính sách dùng để chọn hành động (thử nghiệm, exploration) khác với chính sách dùng để cập nhật Q (luôn chọn giá trị lớn nhất cho tương lai)
- Điều này giúp thuật toán học được giá trị hành động tối ưu bất chấp chính sách hiện tại của agent.
# 3.Bảng Q-table & Cập nhật giá trị: 
- Agent duy trì Q‑table, một bảng các cặp (trạng thái, hành động) với giá trị ước lượng Q(s,a)
- Công thức cập nhật Q‑value:
  ![image](https://github.com/user-attachments/assets/68d1c638-1162-444d-9b23-6e697be41247)
  ![image](https://github.com/user-attachments/assets/e2d11145-cae0-47ad-9520-bc4e5fa7af9f)
# 4. Quy trình thuật toán: 
- Khởi tạo Q‑table (thường là 0).
- Lặp mỗi bước:
   + Chọn hành động A theo chính sách (thường ε-greedy).
   + Thực hiện A, nhận reward R và chuyển sang S'.
   + Dùng phương pháp greedy: chọn 
max
⁡
𝑎
𝑄
(
𝑆
′
,
𝑎
)
max 
a
​
 Q(S 
′
 ,a) để cập nhật Q(S, A).
  + Tiếp tục bước tiếp theo cho đến khi kết thúc episode
# 5.Ưu điểm:
- Model‑free: không cần biết trước xác suất chuyển trạng thái hoặc hàm thưởng
- Off‑policy: linh hoạt trong khám phá môi trường (exploration), nhưng vẫn học chính sách tối ưu
- Đảm bảo hội tụ: trong điều kiện đủ xem xét mọi (s, a) nhiều lần và α giảm hợp lí, Q‑learning hội tụ đến hàm giá trị tối ưu
- Ứng dụng mạnh: có thể xử lý môi trường ngẫu nhiên, không yêu cầu mô hình ổn định

