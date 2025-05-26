# Markov Decision Processes:
Quy trình quyết định Markov (MDP) là một khuôn khổ toán học được sử dụng để mô hình hóa các vấn đề ra quyết định tuần tự trong đó kết quả một phần ngẫu nhiên và một phần có thể kiểm soát được. Đây là một quá trình ngẫu nhiên trong đó trạng thái tương lai của một hệ thống chỉ phụ thuộc vào trạng thái hiện tại và hành động được thực hiện, không phụ thuộc vào trạng thái trong quá khứ, một khái niệm được gọi là thuộc tính Markov. MDP rất cần thiết trong học tăng cường, robot và các lĩnh vực khác để đưa ra quyết định tối ưu trong các hệ thống động.
# Các thành phần chính của MDP:
State(S): Các trạng thái hoặc điều kiện có thể có của hệ thống

Action(A): Các lựa chọn mà tác nhân có thể thực hiện ở mỗi trạng thái.

Transition probability(p): Xác suất chuyển đổi từ trạng thái này sang trạng thái khác khi thực hiện một hành động cụ thể.

Reward(r): Phản hồi hoặc phần thưởng nhận được khi thực hiện một hành động ở trạng thái cụ thể.

Policy (π): Một chiến lược ánh xạ trạng thái thành hành động, xác định cách tác nhân sẽ hành xử.
# Cách hoạt động của MDP:
Observation: Tác nhân quan sát trạng thái hiện tại. 

Action Selection: Tác nhân chọn hành động dựa trên chính sách của mình.

State Transition: Hệ thống chuyển sang trạng thái mới dựa trên hành động đã chọn và xác suất chuyển đổi.

Reward: Hệ thống chuyển sang trạng thái mới dựa trên hành động đã chọn và xác suất chuyển đổi.

Repeat: Quá trình lặp lại, trong đó tác nhân quan sát trạng thái mới, chọn hành động, v.v. 
