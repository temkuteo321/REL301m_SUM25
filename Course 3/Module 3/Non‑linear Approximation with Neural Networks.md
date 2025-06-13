# Tại sao cần phi tuyến?
- Khi môi trường có không gian trạng thái phức tạp, tuyến tính không thể bắt hết được các quan hệ giữa trạng thái và giá trị/trả thưởng.
- Neural network (NN) giúp xấp xỉ các hàm phi tuyến phức tạp – là một bước tiến lớn so với các hàm tuyến tính hoặc tile coding
# Mạng neural trong RL:
- NN cung cấp khả năng representation learning: tự trích xuất đặc trưng từ trạng thái thay vì phải thiết kế feature thủ công
- Ước lượng giá trị 
𝑉
(
𝑠
)
V(s) hoặc 
𝑄
(
𝑠
,
𝑎
)
Q(s,a) – ví dụ trong các mô hình như DQN, Actor‑Critic
# Lý thuyết nền tảng:
- Định lý xấp xỉ toàn phương (Universal Approximation Theorem): Mạng feed‑forward 1 hidden layer với activation phi tuyến có thể xấp xỉ mọi hàm liên tục trên miền compact, nếu đủ neuron
- Tuy nhiên, thực hành không theo ý muốn lý thuyết: training NN trong RL dễ trở nên không ổn định, có thể mất hội tụ, vì:
   + Dữ liệu không i.i.d (dữ liệu phụ thuộc policy đang được học).
   + Mục tiêu học (target) phụ thuộc chính mạng đang được huấn luyện.
# Cách học mạng trong RL:
- Mạng được cập nhật bằng backpropagation kết hợp với gradient descent (hoặc SGD), train mạng để xấp xỉ giá trị hay Q-target.
- Các cải tiến như ReLU, SiLU, mạng sâu, batch‑norm… giúp ổn định và tăng tốc huấn luyện .

