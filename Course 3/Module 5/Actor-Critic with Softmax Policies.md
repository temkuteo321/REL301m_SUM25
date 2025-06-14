# Softmax Policy trong Actor–Critic:
![image](https://github.com/user-attachments/assets/2b8be40c-6ea8-46fb-8c3f-94742372644b)
# Cập nhật Actor sử dụng softmax:
![image](https://github.com/user-attachments/assets/337ed775-3a18-4e1b-937c-a3ecdf2a858b)
# Ưu và hạn chế:
- Ưu điểm:
   + Softmax đảm bảo khám phá tự nhiên (không cần thêm noise).
   + Hành động thường được điều chỉnh theo mức lợi thế, đảm bảo gradient ổn định.
- Hạn chế:
   + Mô hình không suit cho action space lớn hoặc liên tục.
   + Cần tuning số học (learning rates, softmax temperature, bước học value/baseline) để tránh phân kỳ
# Ứng dụng và mở rộng:
- Softmax là bước cơ bản hướng tới các phiên bản nâng cao như A2C/A3C, TRPO/PPO.
- Softmax dễ tích hợp khi dùng tile coding, linear features, hoặc neural nets để định nghĩa 
ℎ
𝜃
(
𝑠
,
𝑎
)
h 
θ
​
 (s,a).
- Có thể xem softmax là baseline trước khi chuyển sang policy gradient cho không gian hành động liên tục hoặc entropy-regularized methods (PPO, SAC)
