# 1. Kết hợp ưu điểm của Monte Carlo Và Dynamic Programming:
- Giống Monte Carlo, TD có thể học từ dữ liệu thực tế mà không cần biết trước mô hình môi trường.

- Giống Dynamic Programming, TD cập nhật từng bước (bootstrapping), không cần đợi kết thúc cả một episode
# 2. Học online, liên tục sau mỗi bước:
- TD cập nhật giá trị trạng thái liền ngay khi nhận được reward và quan sát trạng thái tiếp theo, giúp phản ứng gần như thời gian thực .

- Không cần chờ đến cuối episode như Monte Carlo, nên phù hợp với bài toán dài, mở (non-terminating).
# 3. Hiệu quả mẫu học (sample efficiency) tốt:
- Bootstrapping giúp giảm độ lệch (bias) và giảm phương sai (variance) so với Monte Carlo
- Sử dụng thông tin “trung gian” giữa các bước để cập nhật giúp nhanh hội tụ hơn .

# 4.Dễ đảm bảo hội tụ
- Với policy cố định và learning rate phù hợp, thuật toán như TD(0) có cơ sở toán học rõ ràng và có thể chứng minh hội tụ đến giá trị kỳ vọng
