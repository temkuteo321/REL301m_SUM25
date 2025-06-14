# Khó khăn của khám phá (exploration) trong function approximation:
- Khi sử dụng các hàm tham số (tuyến tính, neural nets…), agent tổng quát hóa từ ít dữ liệu — giúp học nhanh nhưng dễ bị định hướng sai nếu không thăm đủ trạng thái quan trọng. Điều này gây ra bias và dẫn đến học không tốt
- Môi trường có reward rất hiếm hoặc gây nhiễu (ví dụ như “Noisy-TV”) làm cho việc khám phá trở nên phức tạp hơn nhiều
# Bổ sung intrinsic reward (bonus khám phá):
![image](https://github.com/user-attachments/assets/cea0a6b0-e3e8-467f-9996-a92e730cc76b)
# Ứng dụng trong không gian liên tục bằng approximation:
- Sử dụng pseudo-counts trong không gian feature: biến đổi state bằng feature (tile/neural), đếm số lần xuất hiện, và thưởng các vùng chưa được khám phá — phù hợp với môi trường lớn .
- Phương pháp như RND, ICM, NoisyNet, Bootstrapped DQN cũng dùng kỹ thuật bổ sung noise hoặc estimate bất định để tăng cường khám phá
# Thiết kê chiến lược khám phá:
- Chính sách epsilon-greedy (lấy random action với xác suất epsilon) là đơn giản nhất và phổ biến
- Các chiến lược năng cao:
   + Entropy bonus: thêm vào loss term nhằm khuyến khích chọn đa dạng action
   + Noise-based exploration: thêm nhiễu vào state/action/parameters (ví dụ NoisyNet)
# Kết luận:
- Trong môi trường lớn và sử dụng function approximation, khám phá không thể chỉ dựa vào random — cần thêm intrinsic reward, thiết kế chính sách đặc biệt, hoặc thêm yếu tố ngẫu nhiên có cấu trúc.
- Các giải pháp như chi phí bonus, entropy, noise in parameters, và pseudo-counts giúp agent khám phá hiệu quả hơn và tránh bị kẹt tại các vùng ít giá trị.
