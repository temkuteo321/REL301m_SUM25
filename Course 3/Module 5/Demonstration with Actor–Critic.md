# Mục đích của bài demo:
Trình diễn trực quan cách Actor–Critic hoạt động online: agent quan sát trạng thái, chọn hành động qua actor, nhận phần thưởng và trạng thái tiếp theo, rồi critic đánh giá để cập nhật cả hai mạng — actor và critic.
# Quy trình từng bước:
![image](https://github.com/user-attachments/assets/3ca52a4c-d39d-4871-a2b8-b75e6d28cd24)
# Lợi ích thực tế của demo:
- Cập nhật tức thời: actor và critic được cải thiện ngay từng bước, không phải chờ hết episode.
- Feedback nhanh: TD error giúp actor học điều chỉnh hành vi ngay tức thì.
- Tính minh họa: demo giúp người học trực quan hóa các thay đổi diễn ra trong suốt quá trình học.
# Khác biệt so với theory:
- Trong thực thi, bạn thường dùng neural net để biểu diễn cả actor và critic (phôi được chia đầu ra).
- Ngoài online learning, còn có phiên bản nâng cao như A2C, A3C, dùng function approximation phức tạp hơn và áp dụng kỹ thuật tối ưu nâng cao (như batch update, entropy regularization, parallel workers).

