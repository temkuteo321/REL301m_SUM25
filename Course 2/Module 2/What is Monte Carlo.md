# Monte Carlo:
 Monte Carlo (MC) là phương pháp học trong Reinforcement Learning, không cần mô hình (model-free), chỉ dựa vào các trải nghiệm mẫu từ những tập episode hoàn chỉnh.

 Chỉ áp dụng được cho bài toán theo episode, vì cần đến phần trả về (return) sau khi kết thúc tập episode .

# Ước lượng giá trị trạng thái (State-Value):
 Ý tưởng rất đơn giản: lấy trung bình các tổng thưởng (returns) thu được từ mỗi lần truy cập trạng thái đó theo chính sách hiện tại π 


– Hai biến thể phổ biến:

First-visit MC: chỉ tính return đầu tiên khi trạng thái xuất hiện trong mỗi episode.

Every-visit MC: tính return cho mỗi lần trạng thái xuất hiện trong episode 

# Từ ước lượng sang cải thiện chính sách:
MC thuộc dạng Generalized Policy Iteration (GPI), bao gồm hai bước luân phiên:

- Policy Evaluation (ước lượng V eller Q).

- Policy Improvement (cập nhật chính sách greedy hơn)

Đối với tối ưu hóa (Control), ta ước lượng hàm giá trị hành động Q(s,a) và cải thiện chính sách để chọn hành động tốt nhất.

# Khám phá (Exploration):
MC có thể dùng “exploring starts”, tức đặt ngẫu nhiên điểm bắt đầu và hành động khác nhau, để đảm bảo đủ khám phá

Ngoài ra còn có sử dụng chính sách ε‑greedy để cân bằng giữa thăm dò và khai thác.

# On policy & Off policy:
- On-policy MC: sử dụng chính sách đang được đánh giá để lấy dữ liệu.

- Off-policy MC: sử dụng một chính sách khác (behavior policy) để lấy dữ liệu, sau đó điều chỉnh lại (via importance sampling) để đánh giá chính sách mục tiêu
