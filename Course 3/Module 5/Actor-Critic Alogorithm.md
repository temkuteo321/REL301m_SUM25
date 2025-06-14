# Mục tiêu và ý chính:
![image](https://github.com/user-attachments/assets/9d7e3184-240f-4eb7-aa10-d6d7590daa82)
# Cơ chế hoạt động:
![image](https://github.com/user-attachments/assets/16218dc4-df9e-40fe-adfa-8c2c51ca1ccc)
# Ưu nhược điểm:
- Ưu điểm:
   + Giảm biến thiên so với REINFORCE nhờ lợi thế từ Critic
   + Cập nhật online, mỗi bước trực tiếp điều chỉnh policy
- Nhược điểm:
   + Dễ gặp bias nếu Critic ước lượng chưa chính xác hoặc dùng hàm tham số không tốt
   + Off-policy hoặc tham số không phù hợp có thể gây không ổn định/divergence
# Các cải tiến mở rộng:
- Advantage Actor‑Critic (A2C): dùng advantage function 
𝐴
(
𝑠
,
𝑎
)
=
𝑄
(
𝑠
,
𝑎
)
−
𝑉
(
𝑠
)
A(s,a)=Q(s,a)−V(s) để giảm phương sai
- Natural Actor‑Critic: sử dụng lần lượt Fisher information để định hướng gradient, giúp convergence ổn định hơn
- Double-Critic, Target Networks (e.g., trong SAC): giảm bias từ approximation error trong Critic
