# 1.Mục tiêu chính:
Dyna là bước phát triển từ Dyna-Q. Thuật toán này tiếp tục kết hợp việc học trực tiếp (model-free learning) và lập kế hoạch dựa trên mô hình (model-based planning) trong cùng một vòng lặp – giúp agent vừa học nhanh vừa tiết kiệm tương tác thực tế
# 2. Tabular Dyna-Q:
![image](https://github.com/user-attachments/assets/8557b8f4-6baf-4e0e-81c9-5defd896056a)
# 3.Ưu điểm của Dyna:
- Tăng hiệu suất mẫu học (sample efficiency): nhờ kế hoạch giả tưởng, agent học nhiều hơn từ ít lượt tương tác thật
- Cập nhật nhanh khi môi trường thay đổi: nhờ mô hình tái sử dụng, agent nhanh chóng thích ứng
- Điều chỉnh linh hoạt: có thể thay đổi số bước planning (k) dựa vào tài nguyên và tốc độ học .
# 4.Mở rộng:
- Dyna-Q+: thêm “exploration bonus” cho các trạng thái-action lâu không được cập nhật, để khuyến khích khám phá
- Nghiên cứu về cách chọn cặp (s̄,ā) trong planning – không chỉ random – như ưu tiên dựa vào “predecessors” hoặc các sampling nâng cao .


