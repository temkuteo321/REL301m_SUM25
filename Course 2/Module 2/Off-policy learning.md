# Khái niệm:
- Off-policy learning là phương pháp học giá trị hoặc chính sách tối ưu từ dữ liệu sinh ra bởi một chính sách khác với chính sách đang được đánh giá hoặc cải thiện.

- Bao gồm 2 chính sách:

  + Target policy (π): chính sách ta muốn học.

  + Behavior policy (b): chính sách dùng để sinh dữ liệu.

  + Điều kiện quan trọng: mọi hành động mà π có thể chọn thì b cũng phải có xác suất chọn > 0 → gọi là assumption of coverage
# Mục tiêu: 
- Dùng để dự đoán giá trị kỳ vọng 
𝑣
𝜋
(
𝑠
)
v 
π
​
 (s) hoặc 
𝑞
𝜋
(
𝑠
,
𝑎
)
q 
π
​
 (s,a), khi ta chỉ có dữ liệu từ chính sách b.

- Khó khăn: 
𝐺
𝑡
G 
t
​
  thu được theo b thì không thể trực tiếp dùng để ước lượng cho π → cần importance sampling để điều chỉnh.

  ![image](https://github.com/user-attachments/assets/0157a586-62fd-4c93-ba48-30fb52a66323)
  ![image](https://github.com/user-attachments/assets/4dfec232-f635-4d5b-b690-31530d3f149c)
  ![image](https://github.com/user-attachments/assets/0e81996a-dd86-4aaa-a041-03287b61c867)


