# Neural Network:
Mạng nơ‑ron nhân tạo (neural network) là một mô hình toán học mô phỏng cách hoạt động của bộ não, gồm các nút (neurons) liên kết với nhau thông qua trọng số (weights). Chúng đặc biệt hữu ích để xấp xỉ các hàm không tuyến tính phức tạp
# Cấu trúc cơ bản:
- Input layer: nhận đặc trưng (features) từ trạng thái môi trường.
- Hidden layers: gồm nhiều lớp nơ‑ron xử lý và trích xuất đặc trưng (non-linear transformation).
- Output layer: cho kết quả cuối — có thể là giá trị 
𝑉
(
𝑠
)
V(s) hoặc giá trị hành động 
𝑄
(
𝑠
,
𝑎
)
Q(s,a)
# Cách hoạt động (Forward propagation):
![image](https://github.com/user-attachments/assets/15cc77f8-10f4-4508-be44-600081cf0885)
# Học bằng backpropagation (lan truyền ngược):
- Mạng được huấn luyện qua giảm thiểu lỗi giữa giá trị dự đoán và giá trị mục tiêu (supervised loss).
- Thuật toán backpropagation + gradient descent điều chỉnh các trọng số dựa trên đạo hàm của loss theo từng trọng số trong mạng
# Vai trò trong Reinforcement Learning:
- Thay vì feature tay (tile‑coding, coarse coding), mạng neural có thể tự học đặc trưng (representation learning) từ dữ liệu RL.
- Điển hình trong Deep RL như DQN, Actor‑Critic, nơi NN được sử dụng để ước lượng giá trị hoặc trực tiếp học chính sách
- Mạng bất kỳ (feedforward, MLP, CNN, RNN) đều phù hợp tùy đặc tính đầu vào (hình ảnh, chuỗi, cấu trúc) .

