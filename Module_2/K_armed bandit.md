K-ARMED BANDIT (hay còn gọi là multi-armed bandit problem) là một bài toán kinh điển trong học tăng cường (reinforcement learning) và ra quyết định dưới bất định.

Ví dụ 1: Chọn quán cà phê yêu thích
Bạn sống ở một khu phố có 5 quán cà phê (K = 5) gần nhà. Mỗi quán cho bạn trải nghiệm khác nhau (vị ngon, giá cả, phục vụ...), nhưng bạn không biết trước quán nào là tốt nhất.

❓ Vấn đề:
Mỗi ngày bạn chỉ được chọn 1 quán để uống (giống như chọn 1 arm).

Sau khi uống xong, bạn tự đánh giá mức độ hài lòng (reward) từ 0 đến 10.

Mục tiêu: Tối đa hóa tổng mức hài lòng sau 30 ngày.

💥 Thách thức:
Nếu bạn luôn chọn quán mà bạn thích nhất hiện tại → bạn khai thác (exploit), nhưng có thể bỏ lỡ quán tốt hơn.

Nếu bạn thử quán mới chưa biết rõ → bạn khám phá (explore), nhưng có thể hôm đó không vui.

→ Đây chính là bài toán K-armed bandit trong đời sống!

ACTION VALUES: 
Action value, ký hiệu là 
𝑄
(
𝑠
,
𝑎
)
Q(s,a), là một hàm giá trị hành động. Nó thể hiện giá trị kỳ vọng (expected return) khi agent:

đang ở trạng thái 
𝑠
s,

thực hiện hành động 
𝑎
a,

và sau đó làm theo chính sách 
𝜋
π.

![image](https://github.com/user-attachments/assets/e651da61-2e3c-45c1-a253-78f577783244)


