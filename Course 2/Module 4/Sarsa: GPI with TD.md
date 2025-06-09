# 1.Kế thừa từ Temporal-Difference và GPI:
- Sarsa là thuật toán điều khiển trên-policy dựa trên TD (Temporal Difference), thực hiện Generalized Policy Iteration (GPI): lặp lại giữa việc ước lượng giá trị hành động (policy evaluation) và cải thiện chính sách (policy improvement)
- Cập nhật giá trị sau mỗi bước (bootstrapping):
  
![image](https://github.com/user-attachments/assets/941c0e20-c76e-43c2-9c3f-d6cfe5b027ed)


trong đó 
𝐴
′
A 
′
  là hành động được chọn theo chính sách ε‑greedy
# 2.Cơ chế hoạt động:
- Bắt đầu từ trạng thái S, chọn hành động A theo ε-greedy, thực hiện, nhận phần thưởng R và trạng thái S'.

- Lập tức chọn hành động kế tiếp A' theo ε-greedy (on-policy), rồi cập nhật Q(S,A).

- Quá trình tiếp tục cho đến khi kết thúc (terminal)
# 3. Ưu thế:
- On-policy: luôn học và thực thi theo cùng chính sách, giúp mô hình phản ứng chính xác với cách hành xử thực tế .
- Bootstrapping & cập nhật tức thời: giúp Sarsa học trực tuyến nhanh chóng sau mỗi bước, phù hợp với các task dài hoặc không kết thúc rõ ràng 
- Hiệu quả từ GPI: kết hợp lợi ích của TD và cải thiện chính sách liên tục giúp hội tụ nhanh hơn so với Monte Carlo thuần túy
# 4. So sánh với Q‑learning & Expected Sarsa:
- Q‑learning (off-policy): cập nhật nhắm vào giá trị tối đa 
max
⁡
𝑎
𝑄
(
𝑆
′
,
𝑎
)
max 
a
​
 Q(S 
′
 ,a), không phụ thuộc vào hành vi thực thi. Vì vậy, sai số định kiến (bias) có thể tăng do “maximization bias”
- Expected Sarsa: sử dụng kỳ vọng theo phân phối ε‑greedy thay vì giá trị thực nghiệm của A', giúp giảm phương sai cập nhật, nhưng tốn phép tính hơn
