# Khái niệm cơ bản về phương trình Bellman:
Phương trình Bellman là phương trình mô tả mối quan hệ đệ quy giữa giá trị của một trạng thái và giá trị của các trạng thái kế tiếp mà tác nhân có thể chuyển đến.
# Expectation form trong chính sách π:
![image](https://github.com/user-attachments/assets/5aa22f48-8b2f-4d8e-b8ef-a0a9d27268b3)
![Uploading image.png…]()

# Phương trình Bellman tối ưu: 
![image](https://github.com/user-attachments/assets/cc3ee5c9-fb0a-40fe-8e93-c36f0d43ce01)

Chúng là hệ phương trình phi tuyến với số ẩn bằng số trạng thái (cho 
𝑣
∗
v 
∗
 ) hoặc số trạng thái–hành động (cho 
𝑞
∗
q 
∗
 ). Nếu biết hàm động lực 
𝑝
(
𝑠
′
,
𝑟
∣
𝑠
,
𝑎
)
p(s 
′
 ,r∣s,a), có thể giải hệ này bằng các phương pháp số
 # Ý nghĩa và ứng dụng:

 Nếu đã có 
𝑣
∗
(
𝑠
)
v 
∗
 (s), ta có thể chọn hành động tối ưu bằng cách chọn hành động tối đa hóa kỳ vọng phần thưởng một bước:
 ![image](https://github.com/user-attachments/assets/e3ea482f-405f-4c1e-bfe3-d44832e4e302)

 đây gọi là "chính sách greedy" theo 
𝑣
∗
v 
∗
  – là chính sách tối ưu.

  Nếu đã có q*(s,a), thì việc chọn hành động tối ưu đơn giản hơn nữa: chọn a=argmax 
a
​
 q 
∗
 (s,a), không cần xét đến các trạng thái kế tiếp.


 

 
