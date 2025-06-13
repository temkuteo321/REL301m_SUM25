# Deep Neural Networks:
- Là mô hình nhiều lớp (deep neural network – DNN), mở rộng từ mạng neural cơ bản bằng cách thêm nhiều hidden layers, giúp xấp xỉ các hàm phi tuyến phức tạp từ dữ liệu RL .
# Cấu trúc cơ bản & forward propagation:
![image](https://github.com/user-attachments/assets/620743a0-1baa-4eb0-aad9-f3511cb25b93)
# Huấn luyện & backpropagation:
![image](https://github.com/user-attachments/assets/65e619a2-20d2-434a-95e5-5d14aa30912d)
# Ứng dụng trong Deep RL:
Trong các mô hình như DQN, Actor‑Critic, policy-gradient… mạng deep dùng để tự học đặc trưng từ raw input (hình ảnh, sensor…) và thực hiện học giá trị/chính sách trực tiế
# Ưu & nhược khi dùng DNN:
![image](https://github.com/user-attachments/assets/23aec319-605f-4939-be52-d10f4f108ea3)
# Các kỹ thuật làm ổn định Deep RL:
- Experience Replay: lưu lại replay buffer và sampling ngẫu nhiên để phá vỡ sự tương quan giữa dữ liệu
- Target Network: dùng một bản sao mạng cũ để tính target, giảm dao động training



