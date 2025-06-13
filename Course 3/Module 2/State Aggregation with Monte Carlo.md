# 1. State aggregation là gì?
- State aggregation là cách đơn giản nhất để thực hiện function approximation: nhóm các trạng thái tương tự lại thành một “meta-state” và sử dụng một giá trị duy nhất 
𝑉
(
𝑥
)
V(x) cho cả nhóm đó
- Mục đích: giảm số lượng trạng thái cần học, từ đó giảm yêu cầu bộ nhớ và tăng tốc độ huấn luyện.

# 2.Cách hoạt động trong Monte Carlo:
- Với Monte Carlo, sau mỗi episode, ta tính giá trị trả về 
𝐺
𝑡
G 
t
​
  cho mỗi trạng thái đầu tiên của mỗi meta-state.
- Giá trị 
𝐺
𝑡
G 
t
​
  được lấy trung bình để cập nhật ước lượng 
𝑉
(
𝑥
)
V(x) cộng dồn theo độ tin cậy – tương đương supervised learning trên các nhóm trạng thái

# 3.Tổng quát hóa – Ưu và nhược:
![image](https://github.com/user-attachments/assets/d6689874-a642-4fc4-b0a2-01a9f1a2e78a)
