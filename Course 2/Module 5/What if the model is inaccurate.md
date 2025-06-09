# Nguyên nhân mô hình không chính xác:
Mẫu mô hình có thể sai do một trong các lý do:
- Môi trường có tính ngẫu nhiên (stochastic) và chỉ thu thập được lượng dữ liệu hạn chế.
- Mô hình được học qua hàm xấp xỉ (function approximation) gây sai số trong việc khái quát hóa.
- Môi trường thay đổi theo thời gian mà các trạng thái mới chưa được quan sát
# Tác động tiêu cực khi mô hình sai:
- Nếu mô hình sinh ra hallucinated states (trạng thái ảo, không tồn tại trong môi trường thật), việc cập nhật giá trị Q từ các trạng thái này sẽ dẫn đến định hướng chính sách sai lệch (“Hallucinated Value Hypothesis”)
- Khi môi trường thay đổi (ví dụ: mở đường tắt hoặc dời chướng ngại), Dyna-Q dễ bị mắc kẹt trong chính sách cũ, không phản ánh cập nhật mới .
# Giải pháp nâng cao: Dyna-Q+ và lọc dữ liệu mô phỏng:
Dyna‑Q+:
- Thêm exploration bonus vào phần thưởng mô phỏng cho các cặp (s, a) lâu không được trải nghiệm thực tế. Điều này kích thích agent khám phá lại khi môi trường có biến động
Out-of‑Distribution (OOD) Data Filter:
- Loại bỏ các dữ liệu mô phỏng quá khác biệt so với trải nghiệm thực tế (ngoài phân phối).
- Giúp hạn chế lỗi từ mô hình không chính xác, nâng cao chất lượng cập nhật Q 
